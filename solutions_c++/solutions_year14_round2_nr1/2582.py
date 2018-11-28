#include <vector>
#include <string>
#include <iostream>
using namespace std;

int best_target_sum( vector<int> & num )
{
	int mid = (int)num.size()/2;
	int best = 0;
	int cur = 0;
	for(int n = 0; n < (int)num.size(); n++)
		cur += abs(num[n]-num[mid]);
	best = cur;
	cur = 0;
	mid++;
	if( mid >= num.size() )
		return best;

	for(int n = 0; n < (int)num.size(); n++)
		cur += abs(num[n]-num[mid]);
	best = min(best, cur);
	return best;
}

int main()
{
	int num_cases;
	cin >> num_cases;
	for(int c = 0; c < num_cases; c++)
	{
		cout << "Case #" << c+1 << ": ";

		int num_str;
		cin >> num_str;
		vector<string> strs(num_str);
		vector<int> indices(num_str, 0), next(num_str, 0), num(num_str, 0);
		for(int n = 0; n < num_str; n++)
		{
			cin >> strs[n];
			//cout << n << " " << strs[n] << endl;
		}

		bool failed = false;
		int ans = 0;
		while( indices[0] < strs[0].size() ) // TODO check afterwards
		{
			char cur = strs[0][indices[0]];
			//cout << "CUR " << cur << endl;
			for(int n = 0; n < num_str; n++)
			{
				if( strs[n][indices[n]] != cur )
				{
					failed = true;
					break;
				}
				num[n] = 0;
				while( strs[n][indices[n] + num[n]] == cur )
					num[n]++;
				next[n] = indices[n] + num[n];
				
				indices[n] = next[n];
			}
			/*for(int n = 0; n < num_str; n++)
			{
				cout << "STR NR " << n << " " << num[n] << endl;
			}*/

			if( failed )
				break;

			ans += best_target_sum(num);
		}

		for(int n = 0; n < num_str; n++)
			if( indices[n] < (int)strs[n].size() )
			{
				failed = true;
				break;
			}

		if( failed )
			cout << "Fegla Won";
		else
			cout << ans;

		cout << endl;
	}

	return 0;
}
