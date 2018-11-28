#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <iostream>
#include <cstring>

using namespace std;

int Z[3], N;
char E[3] = {'P', 'R', 'S'};
int pos;
char res[5000];

int cnt[3][20][3];

string print(int x, int d = 0){
	if(d == N){
		char t[3] = "\0\0";
		t[0] = E[x];
		return string(t);
	}
	string a, b;
	if(x == 0){
		a = print(0, d+1);
		b = print(1, d+1);
	}else if(x == 1){
		a = print(1, d+1);
		b = print(2, d+1);
	}else if(x == 2){
		a = print(0, d+1);
		b = print(2, d+1);
	}
	if(a < b)
		return a+b;
	else
		return b+a;
}

int main(){
	int tcn, tc;
	cin >> tcn;
	cnt[0][0][0] = 1;
	cnt[1][0][1] = 1;
	cnt[2][0][2] = 1;
	for(int i=1; i<13; ++i){
		for(int k=0; k<3; ++k){
			cnt[0][i][k] += cnt[0][i-1][k] + cnt[1][i-1][k];
			cnt[1][i][k] += cnt[1][i-1][k] + cnt[2][i-1][k];
			cnt[2][i][k] += cnt[0][i-1][k] + cnt[2][i-1][k];
		}
	}
	for(tc = 1; tc <= tcn; ++tc){
		cin >> N >> Z[1] >> Z[0] >> Z[2];
		printf("Case #%d: ", tc);
		if(cnt[0][N][0] == Z[0] && cnt[0][N][1] == Z[1] && cnt[0][N][2] == Z[2]){
			cout << print(0);
		}else if(cnt[2][N][0] == Z[0] && cnt[2][N][1] == Z[1] && cnt[2][N][2] == Z[2]){
			cout << print(2);
		}else if(cnt[1][N][0] == Z[0] && cnt[1][N][1] == Z[1] && cnt[1][N][2] == Z[2]){
			cout << print(1);
		}else{
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}
}
