#include <bits/stdc++.h>
using namespace std;
#define ll  long long int

ll dp[300000]={0};

ll calc(ll R,ll C,ll i)
{
    ll temp=0,a,b;
	for(a=0;a<=(R-1);a++)
        for(b=0;b<C;b++)
		{
			ll copy_cat=1<<(a*C+b);
            ll tc1=a*C+b;
            tc1-=1;
            ll tc2=a*C+b;
            tc2-=C;

            if(i&copy_cat)
            {
                if((i&(1<<tc2)) && a>=1)
                    temp+=1;
            }

            if((i&copy_cat))
            {
                if((i&(1<<tc1)) && b>=1)
                        temp+=1;
            }
		}
	return temp;
}


int main()
{
    int t,x=1;
    scanf("%d",&t);
    while(t--)
    {
        ll ans_temp=0,t1=0,t2=0,R,N,C,i,ans=0,lp=0;  // lp for fenwick formula
        cin>>R>>C>>N;
        ans=R*C*N;
        ans=ans*100;
        t1=R*C;
        t2=(1<<(t1));
        t2-=1;
        for(i=1;i<=t2;i++)
        {
            lp=i&(-i);
            dp[i]=dp[i-lp]+1;

            if(dp[i]==N)
            {
                ans_temp=calc(R,C,i);
                if(ans>ans_temp)
                    ans=ans_temp;
            }
        }
        cout<<"Case #"<<x<<": "<<ans<<endl;
        x++;
    }
    return 0;
}
