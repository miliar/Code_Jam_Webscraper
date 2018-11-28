#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <bitset>
#include <climits>
#include <stack>
#include <cctype>
#include <sstream>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int A[105][105];

int main()	{
    int T, N, M, i, j, k, l, mn;
    bool small = true;

	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);

	scanf("%d", &T);
	for(i=1; i<=T; i++) {
        scanf("%d %d", &N, &M);
        for(j=0; j<N; j++)
            for(k=0; k<M; k++)
                scanf("%d", &A[j][k]);

        small = true;
        for(j=0; small && j<N; j++)  {   //for each row
            for(k=0; small && k<M; k++)  {   // for each column
                mn = A[j][k];
                for(l=0; l<M; l++)
                    if(A[j][l] > mn)    { small = false; break; }
                if(!small)  {
                    for(l=0; l<N; l++)
                        if(A[l][k] > mn)    { small = false; break;}
                    if(l == N) small = true;
                }
            }
        }
        if(small)
            printf("Case #%d: YES\n", i);
        else
            printf("Case #%d: NO\n", i);
	}
	return 0;
}
