//I think I know how to solve the large, but I'd use max flow (because of max flow min cut), and I don't really have a good library at the moment, and I'm a bit short on time to find one

#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int ta=1;ta<=t;++ta)
	{
		cout << "Case #" << ta << ": ";
		int n;
		cin >> n;
		string s;
		getline(cin,s);
		vector<vector<int> > inp(n);
		int next_id=0;
		map<string,int> trans;
		for(int i=0;i<n;++i)
		{
			getline(cin,s);
			stringstream ss(s);
			while(ss>>s)
			{
				if(!trans.count(s)) trans[s]=next_id++;
				inp[i].push_back(trans[s]);
			}
		}
		/*
		for(int i=0;i<n;++i){
			for(int j=0;j<inp[i].size();++j)
				cout << inp[i][j] << ' ';
			cout << endl;
		}
		*/
		int base=0;
		vector<int> sets(next_id,0);
		for(int j=0;j<inp[0].size();++j)
			sets[inp[0][j]]=1;
		for(int j=0;j<inp[1].size();++j)
		{
			if(sets[inp[1][j]]==1)
				base++;
			sets[inp[1][j]] |= 2;
		}
		
		//for(int i=0;i<next_id;++i)cout << sets[i] << ' '; cout << endl;
		
		vector<int> added(next_id,0);
		vector<int> w(next_id,0);
		int best=next_id;
		for(int bm=(1<<(n-2));bm<(1<<(n-1));++bm)
		{
			int resp=0;
			for(int i=2;i<n;++i)
				for(int j=0;j<inp[i].size();++j)
				{
					int a=inp[i][j];
					if(added[a]<bm) added[a]=bm,w[a]=0;
					int va = sets[a]|w[a];
					if((1<<(n-1-i))&bm)
					{
						if(!(va&2))
						{
							if(va&1)
							{
								resp++;
							}
							w[a] |= 2;
						}
					}
					else
					{
						if(!(va&1))
						{
							if(va&2)
							{
								resp++;
							}
							w[a] |= 1;
						}
					}
				}
			if(resp<best)
			{
				//cout << bm << ' ' << resp << ' ' << base << endl;
				best=resp;
			}
		}
		cout << best+base << endl;
	}
}
