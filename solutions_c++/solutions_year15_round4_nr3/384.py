#include <stdio.h>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for (int kase=1;kase<=T;kase++)
	{
		int N;
		cin >> N;
		string tmp;
		getline(cin,tmp);
		vector<vector<string> > SR(N);
		vector<string> dict;
		for (int q=0;q<N;++q)
		{
			getline(cin,tmp);
			stringstream ss(tmp);
			string x;
			while (ss >> x) 
			{
				SR[q].push_back(x);
				dict.push_back(x);
			}
		}
		sort(dict.begin(),dict.end());
		vector<vector<int> > S(N);
		for (int q=0;q<N;q++)
			for (int w=0;w<SR[q].size();w++)
				S[q].push_back(lower_bound(dict.begin(),dict.end(), SR[q][w]) - dict.begin());
		int ret = 987654321;
		for (int s=0;s<(1<<(N-2));s++)
		{
			vector<int> mark(dict.size());
			for (auto& i : S[0]) mark[i]|=1;
			for (auto& i : S[1]) mark[i]|=2;
			for (int i=2;i<N;i++)
			{
				if (s&(1<<(i-2))) for (auto& x : S[i]) mark[x]|=1;
				else for (auto& x : S[i]) mark[x]|=2;
			}
			int a = 0;
			for (auto& w : mark)
				if (w == 3)
					a++;
			if (a<ret) ret = a;
		}
		printf("Case #%d: %d\n",kase,ret);
	}
	return 0;
}