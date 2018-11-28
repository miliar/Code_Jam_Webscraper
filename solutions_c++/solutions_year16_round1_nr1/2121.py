//By SCJ
#include<iostream>
#include<deque>
using namespace std;
int main()
{
ios::sync_with_stdio(0);
cin.tie(0);
	int T;cin>>T;
	for(int no=1;no<=T;++no)
	{
		string s;cin>>s;
		bool b[1005];
		for(int i=0;i<1005;++i) b[i]=0;
		int ed=s.size()-1;
		for(int x='Z';x>='A';--x)
		{
			for(int i=ed;i>=0;--i)
			{
				if(s[i]==x) b[i]=1,ed=i;
			}
		}
		deque<char> dq;
		for(int i=0;i<s.size();++i)
		{
			if(b[i]) dq.push_front(s[i]);
			else dq.push_back(s[i]);
		}
		cout<<"Case #"<<no<<": ";
		for(int i=0;i<s.size();++i) cout<<dq[i];
		cout<<'\n';
	}
}
