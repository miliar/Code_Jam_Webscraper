#include <iostream>
#include <cstdio>
#include <string> 


using namespace std;

int ans,n,T,cur;
string s;
int main()
{
	cin>>T;
	for(int ii=0;ii<T;ii++)
	{
		ans=0;
			cout<<"Case #"<<ii+1<<": ";
			cin>>n>>s;
			cur=0;
			for(int i=0;i<1+n;i++)
			{
				if(i<=cur)cur+=s[i]-'0';
				else if(s[i]!='0'){ans+=i-cur;cur=i+s[i]-'0';}
			}

			cout<<ans<<endl;






	}


	return 0;
}