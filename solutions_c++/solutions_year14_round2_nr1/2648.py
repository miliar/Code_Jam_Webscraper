#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int t,n;


int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out","w",stdout);
	cin>>t;
	for(int g=0;g<t;g++)
	{
		bool chk=false;
		cout<<"Case #"<<g+1<<": ";
		cin>>n;
		vector <pair<char,int> > p [111];
		string s;
		for(int i=0;i<n;i++)
		{
			cin>>s;
			for(int j=0;j<s.size()-1;j++)
			{
				char k=s[j];
				int raod=1;
				while(k==s[j+1])
				{
					raod++;
					j++;
					if(j==s.size()-1)break;
				}
				p[i].push_back(make_pair(k,raod));
			}
			if(s.size()==1)
			{
				p[i].push_back(make_pair(s[0],1));
			}
			if(s.size()>1&&s[s.size()-1]!=s[s.size()-2])
			{
				p[i].push_back(make_pair(s[s.size()-1],1));
			}
		}
		for(int i=0;i<n-1;i++)
		{
			if(p[i].size()!=p[i+1].size())
			{
				cout<<"Fegla Won"<<endl;
				chk=true;
				break;
			}
		}
		if(chk)continue;
		for(int i=0;i<p[0].size();i++)
		{
			for(int j=0;j<n-1;j++)
			{
				if(p[j][i].first!=p[j+1][i].first)
				{
					cout<<"Fegla Won"<<endl;
					chk=true;
					break;
				}
			}
			if(chk)break;
		}
		if(chk)continue;
		long long ans=0;
		for(int i=0;i<p[0].size();i++)
		{
			vector <int> k(110,0);
			long long tmp=0;
			for(int j=0;j<n;j++)
			{
				tmp+=p[j][i].second;
				k[p[j][i].second]++;
			}
			if(tmp%n==0)
			{
				tmp=tmp/n;
			}
			else
			{
				int r=0;
				for(int q=0;q<tmp/n+1;q++)
				{
					r+=k[q];
				}
				if(tmp-r>r)
				{
					tmp=tmp/n+1;
				}
				else tmp=tmp/n;
			}
			for(int j=0;j<n;j++)
			{
				ans+=abs(tmp-p[j][i].second);
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}