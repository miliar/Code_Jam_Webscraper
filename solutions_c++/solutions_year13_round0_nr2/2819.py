#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>

#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define decltype(X) __typeof(X)
#define REP(i, n) for(int i=0; i<(int)n; i++)
#define FOR(it, c) for(decltype((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define ALL(c) (c).begin(), (c).end()

using namespace std;

void print_lawn(vector< vector<int> > &lawn)
{
    cout << "===lawn===" << endl;
    for(int n=0;n<lawn.size();n++){
        for(int m=0;m<lawn[0].size();m++){
            cout << lawn[n][m] << " ";
        }
        cout << endl;
    }
}
bool dfs(vector< vector<int> > &lawn, vector<int>&rows, vector<int>&cols, int n, int m, int N, int M)
{
    if(m==M){
        m = 0;
        n++;
    }
    
#if 0
    cout << "n=" << n << ",m=" << m << endl;
    cout << "rows:";
    for(int r=0;r<rows.size();r++){
        cout << rows[r] << " ";
    }
    cout << endl;
    cout << "cols:";
    for(int c=0;c<cols.size();c++){
        cout << cols[c] << " ";
    }
    cout << endl;
#endif

    if(n==N){
        return true;
    }
    
    if((rows[n]!=0 && rows[n]<lawn[n][m]) || (cols[m]!=0 && cols[m]<lawn[n][m]) ){
        ;
    }else if(rows[n]==lawn[n][m] || cols[m]==lawn[n][m]){
        if(dfs(lawn, rows, cols, n, m+1, N, M)){
            return true;
        }
    }else{
        if(rows[n]==0){
            bool b_ok = true;
            for(int m2=0;m2<m;m2++){
                if(lawn[n][m2]>lawn[n][m]){
                    b_ok = false;
                }
            }
            if(b_ok){
                rows[n] = lawn[n][m];
                if(dfs(lawn, rows, cols, n, m+1, N, M)){
                    return true;
                }
                rows[n] = 0;
            }
        }
        if(cols[m]==0){
            bool b_ok = true;
            for(int n2=0;n2<n;n2++){
                if(lawn[n2][m]>lawn[n][m]){
                    b_ok = false;
                }
            }
            if(b_ok){
                cols[m] = lawn[n][m];
                if(dfs(lawn, rows, cols, n, m+1, N, M)){
                    return true;
                }
                cols[m] = 0;
            }
        }
    }
    return false;
}
void testcase(int t)
{
	string result_str = "OK";
    int N, M;
    cin >> N >> M;
    vector< vector<int> > lawn;
    for(int n=0;n<N;n++){
        vector<int> line;
        for(int m=0;m<M;m++){
            int h;
            cin >> h;
            line.push_back(h);
        }
        lawn.push_back(line);
    }
    // print_lawn(lawn);
    vector<int> rows(N, 0);
    vector<int> cols(M, 0);
    bool ret = dfs(lawn, rows, cols, 0, 0, N, M);
    if(ret){
        result_str = "YES";
    }else{
        result_str = "NO";
    }
    
	cout << "Case #" << (t+1) << ": " << result_str << endl;
}

int main(int argc, char *argv[]) {
	int T;
    if(argc >= 2){
        int fd = open(argv[1], O_RDONLY);
        if(fd == -1){
            fprintf(stderr, "failed to open [%s]\n", argv[1]);
            exit(1);
        }
        int ret = dup2(fd, 0);
        if(ret == -1){
            fprintf(stderr, "failed to dup2[%s]\n", argv[1]);
            exit(1);
        }
    }
	cin >> T;
	for(int t=0;t<T;t++){
		testcase(t);
	}
	return 0;
}

