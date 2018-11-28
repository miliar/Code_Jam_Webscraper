#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	//freopen("in.txt ","r",stdin);
	//freopen("out.txt","w",stdout);
	int t,T;
	scanf("%d",&t);
	T=t;
	while(t--)
	{
		string s;
		int a;
		cin>>a;
		cin>>s;
		int i,ans=0,stand=0;
		stand=stand+(s[0]-48);
		for(i=1;s[i]!='\0';i++)
		{
			if(stand>=i)
			{
				stand=stand+s[i]-48;
			}
			else
			{
				stand=stand+1+s[i]-48;
				ans=ans+1;
			}
			
		}
		cout<<"Case #"<<T-t<<": "<<ans<<endl;
	}
	return 0;
}
