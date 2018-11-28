#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <sstream>

using namespace std; 

string ltos(long num)
{
	string rev; 
	stringstream ss; 
	ss << num; 
	ss >> rev; 

	return rev; 
}

string itos(int num)
{
	string rev; 
	stringstream ss; 
	ss << num; 
	ss >> rev; 

	return rev; 
}

int main() {
	vector<long> vec; 
	vector<string> result; 

	string buf; 
	getline(cin, buf); 
	while (getline(cin, buf))
	{
		long num = stol(buf, NULL); 
		vec.push_back(num); 
	}

	for (int idx = 0; idx < vec.size(); ++idx) 
	{
		long num = vec[idx]; 
		if (num == 0)
		{
			string s = "Case #" + ltos(idx + 1) + ": " + "INSOMNIA"; 
			result.push_back(s); 
			continue; 
		}

		unordered_set<char> seen; 
		int i = 0; 

		while (seen.size() < 10)
		{
			long cur = num * (i + 1); 
			++i; 

			string n = ltos(cur); 
			for (int j = 0; j < n.length(); ++j) 
			{
				char c = n[j]; 
				if (!seen.count(c))
					seen.insert(c); 
			}
		}

		string s = "Case #" + itos(idx + 1) + ": " + ltos(i * num); 
		result.push_back(s); 
	}

	for (int i = 0; i < result.size() - 1; ++i)
		cout << result[i] << endl; 
	cout << result[result.size() - 1]; 

	return 0; 
}