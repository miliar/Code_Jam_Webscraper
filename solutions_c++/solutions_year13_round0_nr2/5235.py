#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

void run()
{
	
	int n,m;
	cin>>n>>m;
	vector<pair<int,pair<int,int> > > Q(n*m);
	vector<vector<int> > H(n,vector<int>(m));
	//vector<vector<int> > a(n,vector<int>(m,100));

	int h;
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cin>>h;
			H[i][j]=h;
			Q[m*i+j] = make_pair(h,make_pair(i,j));
		}
	}

	//sort(Q.begin(),Q.end(),greater<pair<int,pair<int,int> > >());

	int curi,curj;
	for(int i=0;i<Q.size();i++)
	{
		h = Q[i].first;
		curi = Q[i].second.first;
		curj = Q[i].second.second;

		//check vetical
		bool can=true;
		for(int x=0;x<n;x++)
		{
			if(H[x][curj]>h)
			{
				can = false;
				break;
			}
		}
		if(can)
		{
			continue;			
		}

		//check horizontal
		can=true;
		for(int x=0;x<m;x++)
		{
			if(H[curi][x]>h)
			{
				can = false;
				break;
			}
		}
		if(can)
		{
			continue;			
		}

		cout<<"NO\n";
		return;
	}

	cout<<"YES\n";	
}

int main()
{
	string input_name = "B-large(2).in";
	string output_name = "output.txt";

	freopen(input_name.c_str(),"r",stdin);
	freopen(output_name.c_str(),"w",stdout);

	int test;
	cin>>test;
	for(int i = 1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		run();
	}
	return 0;
}