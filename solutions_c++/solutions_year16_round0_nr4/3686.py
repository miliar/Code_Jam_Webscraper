#include<bits/stdc++.h>
using namespace std;

#define s(x) scanf("%d",&x)
#define s1(x) scanf("%lld",&x)
#define p(x) printf("%d\n",x)
#define p1(x) printf("%lld\n",x)
#define ps(x) printf("%d ",x)
#define p1s(x) printf("%lld ",x)
#define st(x) scanf("%s",x)
#define pt(x) printf("%s",x)
#define Y printf("YES\n")
#define N printf("NO\n")
#define mod 1000000007
#define ll long long

ll power(ll b, ll e)
{
    ll p = 1;
    while (e > 0)
    {
       if(e&1)
        {
          p=(p*b)%mod;
        }
        e=e>>1;
        b=(b*b)%mod;
    }
    return p;
}

int main()
{
    //freopen("inp.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    ll k,c,s,t,t1=1,q=1,i;

	s1(t);
	while(t--)
	{

		s1(k);s1(c);s1(s);

		if(k==1)
		{
			cout<<"Case #"<<q++<<": "<<k<<endl;
		}
		else if((c==1 && k!=s) || s<k-1)
		{
            cout<<"Case #"<<q++<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			if(c==1 && k==s)
			{
            cout<<"Case #"<<q++<<": ";
			for(i=1;i<=k;i++)
			{
                cout<<i<<" ";
			}
			cout<<endl;
			}
			else
			{
                cout<<"Case #"<<q++<<": ";
				for(i=1;i<=s && i<k;i++)
				{
				cout<<i+1<<" ";
			    }
			    cout<<endl;
			}
		}
	}

	return 0;
}
