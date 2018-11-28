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
int n, m;
int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc , cas = 1;
	cin>>tc;
	while(tc--)
	{
		PF("Case #%d:\n", cas ++);
		cin>>n>>m;
		for(ll msk=0; msk<1ll<<(n-2); msk++)
		{
			if(m == 0)
			{
				break;
			}
			vector<int> bits;
			bits.push_back(1);
			Rep(i, n-2)
			{
				if(msk&(1ll<<i)) bits.push_back(1);
				else bits.push_back(0);
			}
			bits.push_back(1);
			vector<ll> div;
			bool OK = 1;
			For(j, 2, 11)
			{
				bool prime = 1;
				for(ll z=2; z<1001; z++)
				{
					ll num = 0, pw = 1;
					Rep(k, bits.size())
					{
						num += (pw * bits[k]) % z;
						num %= z;
						pw *= j;
						pw %= z;
					}
					if(num == 0)
					{
						prime = 0;
						div.push_back(z);
						break;
					}
				}
				if(prime)
				{
					OK = 0;
					break;
				}
			}
			if(OK)
			{
				m--;
				for(int j = bits.size() - 1; j >= 0; j--) cout<<bits[j];
				Rep(j, div.size()) cout<<" "<<div[j];
				cout<<endl;
			}
		}
		
	}
	return 0;
}