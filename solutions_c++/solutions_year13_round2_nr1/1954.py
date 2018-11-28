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
#define SIZE 105
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

ll sizes[SIZE];
int increases[SIZE];

int steps(ll &cur, ll target)  {
    for(int i=0; i<32; i++) {
        cur = (cur << i) - (1 << i) + 1;
        if(cur > target) return i;
    }
}

int main()	{
	int T, i, j, N, rem;
	ll A, cur;

	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	for(i=1; i<=T; i++)	{
        scanf("%lld %d", &A, &N);
        for(j=0; j<N; j++)
            scanf("%lld", &sizes[j]);
        sort(sizes, sizes+N);

        memset(increases, 0, SIZE*sizeof(int));
        rem = 0; cur = A;
        for(j=0; j<N; j++) {
            while(cur <= sizes[j])  {
                if(cur == 1)    { rem++; break; }
                cur += cur - 1;
                rem++; increases[j]++;
            }
            if(cur > sizes[j])
                cur += sizes[j];
        }

        for(j = N-1; j >= 0; j--)   {
			if(increases[j] >= (N-j))   {
				rem -= increases[j];
				rem += (N - j);
				N = j;
			}
		}

        printf("Case #%d: %d\n", i, rem);
	}

	return 0;
}
