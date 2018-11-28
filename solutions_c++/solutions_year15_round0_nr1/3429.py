#include<iostream>
#include<cstring>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int T,L;
	char s[5000];
	while(cin>>T)
	{
		int count=0;
		while(T--)
		{
			cin>>L;
			cin>>s;
			int ans=0;
			int E=(int)s[0]-48;
			cout<<"Case #"<<++count<<": ";
			for(int i=1;i<=L;i++)
			{
				if(E==0)
				{
					++E;
					ans++;
				}
				if(E>0)
				{
					--E;
					E+=(int)s[i]-48;
				}
				
			}
			cout<<ans<<endl;
		}
	
	}
}
