#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string shrink(string s)
{
	auto end = unique(s.begin(), s.end());
	return s.substr(0, end - s.begin());
}

int main()
{
	int T;
	cin>>T;

	for (int i = 1; i <= T; ++i)
	{
		int N;
		cin>>N;

		bool good = true;
		string meta;
		vector<string> vs;
		for (int j = 0; j < N; ++j)
		{
			string s;
			cin>>s;

			string tmp = shrink(s);
			if (j == 0)
				meta = tmp;
			else if (tmp != meta)
				good = false;

			vs.push_back(s);
		}

		if (!good)
		{
			cout<<"Case #"<<i<<": Fegla Won"<<endl;
			continue ;
		}

		int count[110][110] = {0};
		for (int j = 0; j < vs.size(); ++j)
		{
			int pos = 0;
			string s = vs[j];
			for (int k = 0; k < meta.length(); ++k)
			{
				char c = meta[k];

				int cnt = 0;
				while (pos < s.length() && s[pos] == c)
				{
					++pos;
					++cnt;
				}

				count[j][k] = cnt;
			}
		}

		// calc ret
		int ret = 0;
		for (int j = 0; j < meta.length(); ++j)
		{
			int sum = 0;
			for (int k = 0; k < vs.size(); ++k)
				sum += count[k][j];

			double middle = sum*1.0/vs.size();
			int target = count[0][j];
			for (int k = 0; k < vs.size(); ++k)
				if (abs(middle - count[k][j]) < abs(middle -target))
					target = count[k][j];

			for (int k = 0; k < vs.size(); ++k)
				ret += abs(target - count[k][j]);
		}

		cout<<"Case #"<<i<<": "<<ret<<endl;
	}
}