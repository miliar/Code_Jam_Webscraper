#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <algorithm>
#include <list>
#include <ctime>
#include <cstdio>
#include <stack>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <functional>
#include <sstream>
#include <map>
#include <set>

#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-8
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
typedef unsigned long long ll;
typedef pair<int, int> pii;
int n;
bool vis[11];
int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc , cas = 1;
	cin>>tc;
	while(tc--)
	{
		PF("Case #%d: ", cas ++);
		cin>>n;
		if(n == 0)
		{
			PF("INSOMNIA\n");
			continue;
		}
		Set(vis, 0);
		int cnt = 0;
		ll num = 0;
		while (cnt < 10)
		{
			num += n;
			ll t = num;
			while(num > 0)
			{
				if(vis[num%10] == 0)
				{
					cnt++;
					vis[num%10] = 1;
				}
				num /= 10;
			}
			num = t;
		}
		cout<<num<<endl;
	}
	return 0;
}