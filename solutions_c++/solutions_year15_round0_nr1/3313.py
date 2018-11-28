#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long ll;
#define INF 1e9
#define maxn 1005
#define maxm 10000+10
#define mod 1000000007
#define eps 1e-7
#define PI acos(-1.0)
#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%I64d",&n)
#define scan2(n,m) scanf("%d%d",&n,&m)
#define scanll2(n,m) scanf("%I64d%I64d",&n,&m)
#define scans(s) scanf("%s",s);
#define ini(a) memset(a,0,sizeof(a))
#define out(n) printf("%d\n",n)
#define outll(n) printf("%I64d\n",n)
using namespace std;
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
char s[maxn];
int n;
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif      
	int T;
	cin>>T;
	int cas = 1;
	while(T--)
	{
		cin>>n;
		scans(s);
		int ans = 0;
		int sum = 0;
		rep(i, n+1)
		{
			int num = s[i] - '0';
			if(sum < i)
			{
				ans += i - sum;
				sum = i;
			}
			sum += num;
		}
		printf("Case #%d: %d\n",cas++, ans);
	}
	return 0;
}
