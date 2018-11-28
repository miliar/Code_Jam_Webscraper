#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <math.h>
#include <string>
#include <sstream>
#include <map>
#include <algorithm>
#include <limits>

#define maxN(a,b) ((a>b)?(a):(b))
#define minN(a,b) ((a<b)?(a):(b))
#define INF (int)10e9
#define ABS(n)	((n>0)? n:(-1*n))
#define NINF -(int)10e9
#define eps 10e-9
#define WORDSIZE 31

using namespace std;

typedef vector<int> V;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;
typedef vector<pair<int, int> > VPII;

//U  D  L  R
int dx[] = {0, 0, 1, -1};
int dy[] = {1,-1, 0, 0};
// numeric_limits<int>::min();

char str[1005];

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 0; i < t; i++) {
        int len;
        scanf("%d", &len);
        scanf("%s", str);
        int aux = 0, cum = 0;
        for(int idx = 0; idx < len+1; idx++) {
            int t1 = str[idx]-'0';
            int t2 = idx - cum;
            //printf("%d %d %d %d\n",t1, t2, idx, cum);
            int t3 = (t2>0)?(t2):0;
            aux += t3;
            cum += t3+t1;
        }
        printf("Case #%d: %d\n",i+1, aux);
    }

    return 0;
}


