	/* asif_mak
	codejam */
     
     
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
    #include <limits.h>
    #include <iomanip>
    using namespace std;
    typedef long long ll;
    #define MP make_pair
    #define pb push_back
    #define rep(i,n) for(ll i=0;i<n;i++)
    #define REP(i,a,b) for(ll i=a;i<=b;i++)
    #define repi(i,n) for(ll i=n-1;i>=0;i--)
    #define REPI(i,a,b) for(ll i=a;i>=b;i--)
    typedef vector<int> vi;
    typedef vector< vi > vvi;
    typedef pair< int,int > ii;
    #define sz(a) int((a).size())]
    #define clr(a) memset(a,0,sizeof(a))
    #define ini(a) memset(a,-1,sizeof(a))
    #define inp(n) scanf("%d",&n)
    #define inp2(n,m) scanf("%d%d",&n,&m)
    #define ins(s) scanf("%s",s);
    #define out(n) printf("%d\n",n)
    #define out2(n,m) printf("%d %d\n",n,m)
    #define inc(n) scanf("%c",&n)
    #define MOD 1000000007
    #define MOD_INV 1000000006
    #define MAX 100009
    #define INF 999999999
     
    #define si(n) scanf("%d",&n)
    #define sll(n) scanf("%lld",&n)
     
    int main()
    {
        std::ios_base::sync_with_stdio(false);
       	int t;
       	cin>>t;
       	for(int i=1;i<=t;i++)
       	{
       		ll sum=0;
       		ll count=0;
       		string str;
       		int n;
       		cin>>n>>str;
       		for(int j=1;j<=n;j++)
       		{
       			sum=sum+str[j-1]-'0';
       			if(sum>=j)
       			continue;
       			else
       			{
       			sum=sum+1;
       			count++;
				}
       			
       			
			   }
			   cout<<"Case #"<<i<<": "<<count<<endl;
		}
        return 0;
    }