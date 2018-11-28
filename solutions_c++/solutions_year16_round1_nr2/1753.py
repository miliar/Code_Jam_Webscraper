#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
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
	vector<vector<vector<int>>> vec; 
	vector<vector<int>> results; 

	string buf; 
	getline(cin, buf); 
	int cases = stoi(buf); 

	for (int i = 0; i < cases; ++i)
	{
		getline(cin, buf); 
		int n = stoi(buf); 

		vector<vector<int>> local; 
		for (int j = 0; j < 2 * n - 1; ++j)
		{
			getline(cin, buf); 
			istringstream ss(buf); 

			vector<int> temp; 
			while(getline(ss, buf, ' ')) {
			    int entry = stoi(buf); 
			    temp.push_back(entry); 
			}
			local.push_back(temp); 
		}

		vec.push_back(local); 
	}

	for (int idx = 0; idx < vec.size(); ++idx) 
	{
		auto data = vec[idx]; 
		vector<int> result; 
	
		unordered_map<int, int> record; 
		for (auto l : data)
		{
			for (auto num : l)
			{
				if (!record.count(num))
					record[num] = 1; 
				else
					record[num]++; 
			}
		}

		// cout << record[2] << endl; 

		for (auto item : record)
			if (item.second % 2 != 0)
				result.push_back(item.first); 

		sort(result.begin(), result.end()); 
		results.push_back(result); 
	}

	for (int i = 0; i < results.size() - 1; ++i)
	{
		cout << "Case #" << (i + 1) << ": "; 
		for (int j = 0; j < results[i].size() - 1; ++j)
			cout << results[i][j] << " "; 
		cout << results[i][results[i].size() - 1] << endl; 
	}

	cout << "Case #" << results.size() << ": "; 
	for (int j = 0; j < results[results.size() - 1].size() - 1; ++j)
		cout << results[results.size() - 1][j] << " "; 
	cout << results[results.size() - 1][results[results.size() - 1].size() - 1]; 

	return 0; 
}











