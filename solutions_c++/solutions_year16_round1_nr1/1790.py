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
	vector<string> vec; 
	vector<string> results; 

	string buf; 
	getline(cin, buf); 
	while (getline(cin, buf))
	{
		string s = buf; 
		vec.push_back(s); 
	}

	for (int idx = 0; idx < vec.size(); ++idx) 
	{
		string data = vec[idx]; 

		string result = string(1, data[0]); 

		for (int i = 1; i < data.length(); ++i) 
		{
			char c = data[i]; 
			if (c >= result[0])
				result = string(1, c) + result; 
			else
				result = result + string(1, c); 
		}
		
		results.push_back(result); 
	}

	for (int i = 0; i < results.size() - 1; ++i)
		cout << "Case #" << (i + 1) << ": " << results[i] << endl; 

	cout << "Case #" << results.size() << ": " << results[results.size() - 1]; 

	return 0; 
}











