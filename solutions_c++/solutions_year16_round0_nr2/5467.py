#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <sstream>

using namespace std; 

int main() {
	vector<string> vec; 
	vector<int> result; 

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

		int count = 0; 
		char cur = data[0]; 

		for (int i = 1; i < data.length(); ++i)
		{
			if (data[i] != cur)
			{
				cur = (cur == '+') ? '-' : '+'; 
				count++; 
			}
		}

		count += (cur == '+') ? 0 : 1; 
		
		result.push_back(count); 
	}

	for (int i = 0; i < result.size() - 1; ++i)
		cout << "Case #" << (i + 1) << ": " << result[i] << endl; 
	cout << "Case #" << (result.size()) << ": " << result[result.size() - 1]; 

	return 0; 
}