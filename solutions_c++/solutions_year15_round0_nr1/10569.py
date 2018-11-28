#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int main()
{
    ll test,ss,sum,need;
    scanf("%lld",&test);
    string s;
    ll x=0;
    while(test--)
    {   x++;
        need=0;
        scanf("%lld",&ss);
        cin>>s;
        sum=(ll)s[0]-48;
        for(ll i=1;i<=ss;i++)
        {   if((ll)s[i]-48==0)
             continue;
            else if(sum<i)
             {
              need=need+i-sum;
              sum=i+(ll)s[i]-48;
             }
             else
             sum=sum+(ll)s[i]-48;
        }

        printf("Case #%lld: %lld\n",x,need);


    }
    return 0;
}
