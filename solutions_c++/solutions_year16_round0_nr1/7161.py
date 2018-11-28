/*

-------------------------------------------------------------------------------------------------\
 \       |AUTHOR: RAGHU PAAVAN(rap)  :D ---------------------------------------------------------- \
 /       |        NIT CALICUT  ------------------------------------------------------------------- /
---------|----------------------------------------------------------------------------------------/

*/
#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define ll    long long int
#define all(c) c.begin(),c.end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define scan(x) scanf("%d", &x)
#define scanl(x) scanf("%lld", &x)
#define print(a) printf("%d\n",a)
#define printl(a) printf("%lld\n",a)
#define pb push_back
#define maxn 100005
ll a[maxn];
ll rap[10],rapb[26];
int main()
{
    ll i,n,t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
		ll count=0;
		memset(rap,0,sizeof(rap));
        cin>>n;
        if(n==0)cout<<"Case #"<<k<<": "<<"INSOMNIA\n";
        else 
        {
			i=1;
			while(count!=10)
			{
				ll temp=i*n;
				while(temp>0)
				{
					ll temp2=temp%10;
					rap[temp2]++;
					if(rap[temp2]==1)count++;
					temp=temp/10;
					}
					i++;
				}
			cout<<"Case #"<<k<<": "<<(i-1)*n<<endl;
		}
    }
    return 0;
}
