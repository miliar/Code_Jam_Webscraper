#include <iostream>
#include <sstream>
#include <functional>
#include <climits>
#include <cstddef>
#include <numeric>
#include <string>
#include <string.h>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <set>
#include <map>

using namespace std;
typedef long long ll;


int main()
{
	int T;cin>>T;
	for (int CASE = 1; CASE <= T; CASE++)
	{
		int a1,a2,b1[5][5],b2[5][5];
		cin>>a1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>b1[i][j];
			}
		}
		cin>>a2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin>>b2[i][j];
			}
		}

		vector<int> ans;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (b1[a1-1][i]==b2[a2-1][j]) ans.push_back(b1[a1-1][i]);
			}
		}

		if (ans.size()==0) cout<<"Case #"<<CASE<<": "<<"Volunteer cheated!"<<endl;
		else if (ans.size()>=2) cout<<"Case #"<<CASE<<": "<<"Bad magician!"<<endl;
		else cout<<"Case #"<<CASE<<": "<<ans[0]<<endl;
	}
	return 0;
}