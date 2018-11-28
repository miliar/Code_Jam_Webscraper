#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 1000000


int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
	int tcase,t,i,len;
	scanf("%d",&tcase);
	string str,ans;
	for(t=1;t<=tcase;t++)
	{
		cin>>str;
		ans="";
		len = str.size();
		for(i=0;i<len;i++)
		{
			if(i==0) 
			ans += str[i];
			if(i>0)
			{
				if(str[i]>=ans[0])
				ans = str[i]+ans;
				else
				ans += str[i];
			}
			
			
			
		}
		printf("Case #%d: ",t);
			cout<<ans<<endl;
	}
}

