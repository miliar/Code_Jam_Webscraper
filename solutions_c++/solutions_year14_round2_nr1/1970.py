#include<iostream>
#include<cmath>
#include<vector>
#include<string>
#include<list>
using namespace std;


#define INVALID_STRING "Fegla Won"
int main()
{
//	freopen("p1sample.txt","r",stdin);
	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		cout<<"Case #"<<T<<": ";
		int n;
		cin>>n;
		vector<string> S(n);
		for(int i=0;i<n;i++)
			cin>>S[i];
			
		
		vector<vector<pair<char,int> > > characterCount(n);
		for(int i=0;i<n;i++)
		{
			characterCount[i].push_back(make_pair(S[i][0],1));
			for(int j=1;j<S[i].size();j++)
				if(characterCount[i].back().first==S[i][j])
					characterCount[i].back().second++;
				else
					characterCount[i].push_back(make_pair(S[i][j],1));
		}
		
		
		//validy check
		bool isValid=true;
		for(int i=0;i<n;i++)
			if(characterCount[i].size()!=characterCount[0].size())
			{
				isValid=false;
				break;
			}
		
		if(!isValid)
		{
			cout<<INVALID_STRING<<endl;
			continue;
		}
			
		for(int i=0;i<n;i++)
			for(int j=0;j<characterCount[0].size();j++)	
				if(characterCount[i][j].first!=characterCount[0][j].first)
				{
					isValid=false;
					break;
				}
		if(!isValid)
		{
			cout<<INVALID_STRING<<endl;
			continue;
		}
		int totalSteps=0;
		for(int i=0;i<characterCount[0].size();i++)
		{
			int median=0;
			for(int j=0;j<n;j++)
				median+=characterCount[j][i].second;
			median/=n;
			
			for(int j=0;j<n;j++)
				totalSteps+=abs(median-characterCount[j][i].second);
		}
		cout<<totalSteps<<endl;
	}
}
