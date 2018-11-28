/***********************
coded By Keshav Goel(kshetra718)
*************************/
#include<bits/stdc++.h>
using namespace std;

int main()
{
	int T,t,len,i,left,ans;
	char a[1005];
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>len;
		cin>>a;
		ans = 0;
		left = a[0]-'0';
		for(i=1;i<=len;i++)
		{
			if(a[i]-'0')
			{
			if(i <= left)
			{
				left += (a[i]-'0');
			}
			else
			{
				
				ans += (i-left);
				left = i;
				left += (a[i]-'0');
			}
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
 	return 0;
}


