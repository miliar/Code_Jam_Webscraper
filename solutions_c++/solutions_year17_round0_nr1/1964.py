#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <set>
#include <limits.h>
#include <assert.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define null NULL
#define ll long long

#define fast cin.sync_with_stdio(0);cin.tie(0);
#define tr(c, itr) for(itr = (c).begin(); itr != (c).end(); itr++)
#define present(container, element) (container.find(element) != container.end()) //for set,map,etc
#define cpresent(container, element) (find(all(container),element) != container.end()) //for vectors
#define all(c) c.begin(),c.end() //eg sort(all(v));
//Initialization
#define clr(a) memset(a,0,sizeof(a))
#define ini(a) memset(a,-1,sizeof(a))

//Input Output
#define inp(n) scanf("%d",&n)
#define inp2(n,m) inp(n), inp(m)
#define inps(s) scanf("%s",s)
#define inpc(n) scanf("%c",&n)
#define inplf(n) scanf("%lf",&n)
#define inpll(n) scanf("%lld",&n)
#define inpll2(n,m) scanf("%lld%lld",&n,&m)

#define out(n) printf("%d\n",n)
#define out2(n,m) printf("%d %d\n",n,m)
#define outs(d) printf("%s\n",d)
#define sout(n) printf("%d ",n)
#define outll(n) printf("%lld\n",n)
#define soutll(n) printf("%lld ",n)
#define outll2(n,m) printf("%lld %lld\n",n,m)
#define nl printf("\n");

//loops
#define rep(i,n) for(long long i=0;i<n;i++)
#define REP(i,a,b) for(long long i=a;i<=b;i++)
#define PER(i,a,b) for(long long i=b;i>=a;i--)

//const
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 1000000009
#define INF 1000000000000
#define PI 3.14159265358979323846264338327

//cases
#define aaa ll t;cin>>t;while(t--)

ll modpow(ll base, ll exp, ll modulus) {base %= modulus;ll result = 1;while (exp > 0){if (exp & 1) result = (result * base) % modulus;
base = (base * base) % modulus;exp >>= 1;}return result;}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int p = 1;
	while(p<=t)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		int tot = s.size();
		int ans = 0;
		for(int i=0;i<=tot-k;i++)
		{
			if(s[i] == '-')
			{
				
				for(int j=i;j<i+k;j++)
				{
					if(s[j] == '-')
					{
						s[j] = '+';
					}
					else
					{
						s[j] = '-';
					}
				}
				ans++;
			}
		}
		int sw = 0;
		for(int i=0;i<tot;i++)
		{
			if(s[i] == '-')
			{
				
				sw = 1;
				break;
			}
		}
		if(sw == 1)
		{
			cout<<"Case #"<<p<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<p<<": "<<ans<<endl;
		}
		p++;
	}
	return 0;
}

