#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    freopen("input1.in","r",stdin);
    //freopen("ouput1.txt","w",stdout);
	ll t;
	char strng[1005];
	scanf("%lld",&t);
	for(ll st=1;st<=t;st++)
	{
	    ll temp=0;
	    ll result=0;
	    ll len;
	    ll k=0;
	    cin>>len;
	    for(int i=0;i<=len;i++)
	    {
            cin>>strng[i];
            if(i==0)
                temp+=(int)strng[i]-48;
            else
            {
                if(temp<i)
                {
                    result+=i-temp;
                    k=i-temp;
                    temp+=k;
                }
	        temp+=(int)strng[i]-48;
            }
	    }
	    cout<<"Case #"<<st<<": "<<result<<endl;

	}
	return 0;
}
