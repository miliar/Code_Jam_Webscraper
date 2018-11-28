#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define rep2(i,m,n) for(int i=(int)m;i<(int)n;i++)

#define SMALL
//#define LARGE

using namespace std;

string solution() {
    string result = "Unknown";
    int N, M;
    
    scanf("%d %d\n", &N, &M);

#ifdef SMALL
    int posMatrix[10][10];
    int maxElement[2][10] = {0};
#endif
#ifdef LARGE
    int posMatrix[100][100];
    int maxElement[2][100] = {0};
#endif

    rep(i,N) {
        rep(j,M) {
            scanf("%d", &posMatrix[i][j]);
            if(posMatrix[i][j] > maxElement[0][i]) maxElement[0][i] = posMatrix[i][j];
            if(posMatrix[i][j] > maxElement[1][j]) maxElement[1][j] = posMatrix[i][j];
        }
    }
        
    int cnt = 0;
    rep(i,N) {
        rep(j,M) {
            if(maxElement[0][i] == posMatrix[i][j]) { posMatrix[i][j] = 0; cnt++; }
            else if(maxElement[1][j] == posMatrix[i][j]) { posMatrix[i][j] = 0; cnt++; }
        }
    }
    
    if(cnt == N*M) result = "YES";
    else result = "NO";
    
    return result;
}

int main() {
    int tc;
    scanf("%d\n", &tc);
    rep(i,tc) {
        printf("Case #%d: %s\n", i+1, solution().c_str());
    }
	return 0;
}