#include <bits/stdc++.h>

using namespace std;
#define ll long long
//set<ll> s;
int main()
{
    freopen("inp.in","r",stdin);
    freopen("opt.out","w",stdout);
	ll t,n,j,i,temp,num,ex;
//	cin>>t;
	scanf("%lld",&t);
	j =1;
	while(j <= t)
	{

//		cin>>n;
		scanf("%lld",&n);
		if(n == 0)
		 {
//		     cout<<"Case #"<<j<<": INSOMNIA\n";
		     printf("Case #%lld: INSOMNIA\n",j);
		     j++;
		     continue;
		 }
		 ll arr[10] = {0};
		 i=1;
		ll  maxi = 1;
		while(1)
		{

		    if(maxi > 10)
		    {
//		        cout<<"Case #"<<j<<": "<<ex<<"\n";
		        printf("Case #%lld: %lld\n",j,ex);
		        break;
		    }
		    else
		    {
		        temp = i*n;
		        ex = temp;
		        i++;
		        while(temp)
		        {
		            num = temp%10;
//		            s.insert(num);
		            if(arr[num] == 0)
		            {
		                arr[num] = maxi;
		                maxi++;
		            }
		            temp = temp/10;
		        }
		    }
		}
		j++;
//		s.clear();
	}

}
