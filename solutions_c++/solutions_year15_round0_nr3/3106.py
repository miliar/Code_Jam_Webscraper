#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <stack>
#include <deque>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <climits>
#include <cfloat>
#include <cstdio>
#define x first
#define y second
#define IN(x, n) (0 <= (x) && (x) < n)
#define MAX 10010
#define MOD 1000000007
#define GET(s) (s-'i'+2)
using namespace std;

int tabla[5][5] = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3},
{0, 3, -4, -1, 2}, {0, 4, 3, -2, -1} };
int dp[MAX][MAX];

const char* solve(int n, long long int X, char s[]){
    int ant;
    long long int may = n*X;
    memset(dp, 0, sizeof(dp));
    for(int i = 0, k = 0; k < may; i = (i+1)%n, k++){
        ant = dp[k][k] = GET(s[i]);

        for(int j = (i+1)%n, a = k+1; a < may; j = (j+1)%n, a++){
            int act = GET(s[j]);
            if(ant < 0){
                dp[k][a] = -tabla[-ant][act];
            }
            else{
                dp[k][a] = tabla[ant][act];
            }
            ant = dp[k][a];
        }
    }
/*    for(int i = 0; i < may; i++){
        for(int j = 0; j < may; j++){
            printf("%02d%c", dp[i][j], j+1 == may ? '\n' : ' ');
        }
    }//*/
    for(int i = 0; i < (may-2); i++){
        for(int j = i+1; j < (may-1); j++){
//            printf("(0 %d) (%d %d) (%d %d)\n", i, i+1, j, j+1, may-1);
            if(dp[0][i] == 2 && dp[i+1][j] == 3 && dp[j+1][may-1] == 4){
                return "YES";
            }
        }
    }
    return "NO";
}

int main(){
	int n, L, casos;
	long long int X;
	char s[MAX];
	scanf("%d", &casos);
	for(int i = 1; i <= casos; i++){
        scanf("%d%lld%s", &L, &X, s);
        printf("Case #%d: %s\n", i, solve(L, X, s));
	}
	return 0;
}
