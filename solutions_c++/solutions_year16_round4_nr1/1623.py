#include <bits/stdc++.h>
#define PB push_back
#define FT first
#define SD second
#define MP make_pair
#define INF 0x3f3f3f3f
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int>  P;
const int N = 23333,MOD = 7+1e9;
int n, rd, a[N];
char ch[N];
void init()
{
	for(int i = 1;i <= n;i ++) a[i] = i;
}
char get(char s1, char s2)
{
	if(s1 > s2) swap(s1, s2);
	if(s1 == 'p' && s2 == 'r') return 'p';
	else if(s1 == 'p' && s2 == 's') return 's';
	else if(s1 == 'r' && s2 == 's') return 'r';
}
char tmps[N];
bool isok()
{
	char tmp[N];
	for(int i = 1;i <= n;i ++)
	{
		tmp[a[i]] = tmps[a[i]] = ch[i];
	}
	int NN = n;
	for(int o = 1;o <= rd;o ++)
	{
		for(int j = 1;j <= NN;j += 2)
		{
			if(tmp[j] == tmp[j+1])
			{
				return 0;
			}
			else 
			{
				tmp[(j+1)/2] = get(tmp[j], tmp[j+1]);
			}
		}
		
		NN /= 2;
	}
	return 1;
}
bool work()
{
	do{
		if(isok())
		{
			for(int i = 1;i <= n;i ++)
			{
				printf("%c", 'A' + (tmps[i] - 'a'));
			}
			return 1;
		}
	}while(next_permutation(a + 1, a + 1 + n));
	return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T, ca = 0;
    scanf("%d", &T);
    while(T --)
    {
    	int r, p, s;
    	scanf("%d%d%d%d", &rd, &r, &p, &s);
    	n = r + p + s;
    	init();
    	for(int i = 1;i <= p;i ++) ch[i] = 'p';
    	for(int i = 1;i <= r;i ++) ch[i + p] = 'r';
    	for(int i = 1;i <= s;i ++) ch[i + r + p] = 's';
    	printf("Case #%d: ", ++ ca);
    	if(!work())
    	{
			printf("IMPOSSIBLE");
    	}
    	puts("");
    }
    return 0;
}