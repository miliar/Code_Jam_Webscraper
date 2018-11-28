#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <sstream>
#include <bitset>

using namespace std; 

int isPrime(long num)
{
	for (long i = 2; i < sqrt(num); ++i)
		if (num % i == 0)
			return i; 
	return 0; 
}

int main() {
	vector<pair<int, int>> vec; 
	vector<vector<pair<string, vector<int>>>> results; 

	string buf; 
	getline(cin, buf); 
	while (getline(cin, buf))
	{
		string s = buf; 
		istringstream ss(s); 
		getline(ss, s, ' '); 
		int n = stoi(s); 
		getline(ss, s, ' '); 
		int j = stoi(s); 
		vec.push_back(make_pair(n, j)); 
	}

	for (int idx = 0; idx < vec.size(); ++idx) 
	{
		vector<pair<string, vector<int>>> result; 
		auto data = vec[idx]; 

		int n = data.first; 
		int j = data.second; 

		int _max = stoi(string(n - 2, '1'), NULL, 2); 

		for (int i = 0; i < _max; ++i)
		{
			if (result.size() == j)
				break; 

			string num = "1" + bitset<64>(i).to_string().substr(64 - (n - 2)) + "1"; 

			vector<int> evidence; 
			bool flag = true; 

			for (int j = 2; j < 11; ++j)
			{
				long number = stol(num, NULL, j); 

				int rev = isPrime(number); 
				if (!rev)
				{
					flag = false; 
					break; 
				}
				else
				{
					evidence.push_back(rev); 
				}
			}

			if (flag)
			{
				result.push_back(make_pair(num, evidence)); 
			}
		}
		
		results.push_back(result); 
	}

	for (int i = 0; i < results.size() - 1; ++i)
	{
		cout << "Case #" << (i + 1) << ": " << endl; 
		for (int j = 0; j < results[i].size(); ++j)
		{
			cout << results[i][j].first << ' '; 
			for (int k = 0; k < results[i][j].second.size() - 1; ++k)
				cout << results[i][j].second[k] << ' '; 
			cout << results[i][j].second[results[i][j].second.size() - 1] << endl; 
		}
	}

	cout << "Case #" << results.size() << ": " << endl; 
	for (int j = 0; j < results.back().size() - 1; ++j)
	{
		cout << results.back()[j].first << ' '; 
		for (int k = 0; k < results.back()[j].second.size() - 1; ++k)
			cout << results.back()[j].second[k] << ' '; 
		cout << results.back()[j].second[results.back()[j].second.size() - 1] << endl; 
	}

	cout << results.back().back().first << ' '; 
	for (int k = 0; k < results.back().back().second.size() - 1; ++k)
		cout << results.back().back().second[k] << ' '; 
	cout << results.back().back().second[results.back().back().second.size() - 1]; 

	return 0; 
}











