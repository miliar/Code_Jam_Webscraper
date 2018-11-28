#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <memory.h>

using namespace std;

// Input macros
#define s(n)                        scanf("%d",&n)
#define sl(n)						scanf("%I64d", &n)
#define sc(n)                       scanf("%c",&n)
#define sf(n)                       scanf("%lf",&n)
#define ss(n)                       scanf("%s",n)

// Useful container manipulation / traversal macros
#define forall(i,a,b)               for(int i=a;i<b;i++)
#define foreach(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                    memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair

typedef vector<int> vi;
typedef vector<string> vs;

#define INF 2147483647
#define UINF 0xffffffff

int main()
{
	int t;
	s(t);
	forall(z, 0, t)
	{
		char data[1100];
		int n, k, ans = 0;
		ss(data);
		n = strlen(data);
		s(k);
		forall(i, 0, n - k + 1)
		{
			if (data[i] == '-')
			{
				ans++;
				forall(j, i, i + k)
				{
					data[j] = (data[j] == '-') ? '+' : '-';
				}
			}
		}

		bool flag = true;
		forall(i, n - k + 1, n)
		{
			if (data[i] == '-')
			{
				flag = false;
				break;
			}
		}
		printf("Case #%d: ", z + 1);
		if (flag)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
}