#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

void solve() {
	int N;cin >> N;cin.ignore();
	vector<string> strings;
	vector<vector<char> > groups;
	vector<vector<int> > groupLengths;
	vector<int> averages;
	strings.resize(N);
	groups.resize(N);
	groupLengths.resize(N);
	for (int i = 0; i < N; ++i)
	{
		getline(cin, strings[i], '\n');
		char current;
		int currentGroup = 0;
		groups[i].push_back(strings[i][0]);
		//cout << groups[i][0];

		for (int j = 0; j < strings[i].length(); ++j)
		{
			current = strings[i][j];
			if(current == groups[i][currentGroup]) {
				continue;
			}
			currentGroup++;
			groups[i].push_back(current);
			//cout << current;
		}
		//cout << endl;
		groupLengths[i].resize(groups[i].size());
		int pos = 0;
		for (int j = 0; j < groups[i].size(); ++j)
		{
			groupLengths[i][j] = 0;
			while(pos < strings[i].length() && strings[i][pos] == groups[i][j]) {
				groupLengths[i][j]++;
				pos++;
			}
		}
	}

	for (int i = 0; i < N-1; ++i)
	{
		if(groups[i] != groups[i+1]) {
			cout << "Fegla Won";
			return;
		}
	}

	averages.resize(groups[0].size());
	for (int i = 0; i < groups[0].size(); ++i)
	{
		float counter = 0;
		for (int j = 0; j < N; ++j)
		{
			counter += groupLengths[j][i];
		}
		averages[i] = round(counter/N);
	}

		int counter = 0;
	for (int i = 0; i < N; ++i)
	{	
		for (int j = 0; j < groups[i].size(); ++j)
		{
			counter += abs(averages[j] - groupLengths[i][j]);
		}
	}
		cout << counter;

}

int main()
{
	int T; cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
