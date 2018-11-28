#include <iostream>
using namespace std;
void flip(string &s,int top);
int main()
{
	int t;
	cin>>t;
	string s;
	int ans;
	for(int i=0;i<t;i++)
	{
		ans=0;
		cin>>s;
		int p=s.length();
		int q;
		bool f;
		while(true)
		{
			f=false;
			for(int j=0;j<s.length();j++)
			{
				if(s[j]=='-')
				{
					f=true;
					break;
				}
			}
			if(f==false)
				break;
			while(s[p-1]=='+')
				p--;
			q=0;
			while(s[q]=='+')
				q++;
			if(q!=0)
			{
				flip(s,q);
				ans++;
			}
			flip(s,p);
			ans++;
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}
void flip(string &s,int top)
{
	for(int i=0;i<top;i++)
	{
		if(s[i]=='+')
			s[i]='-';
		else
			s[i]='+';
	}
	for(int i=0;i<top/2;i++)
	{
		char temp=s[i];
		s[i]=s[top-1-i];
		s[top-1-i]=temp;
	}
	//cout<<s<<endl;
}
