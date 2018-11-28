#include <string>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

long num(vector<long> v)
{
	long result = 0;

	long currsum = 0;
	for(long i = 0; i < v.size(); ++i)
	{
		while(v[i] > currsum)
		{
			++result;
			++currsum;
		}
		++currsum;
	}

	return result;
}

int main()
{
	long cases;
	long k;
	string s;                 
	cin >> cases;                   
	for(long c=1; c<=cases; c++)      
	{
		cin >> k; 
		cin >> s;
		vector<long> v;
		for(long i = 0; i < s.length(); ++i)
		{
			string st;
			st.push_back(s[i]);
			long b = atoi(st.c_str());
			for(long j = 0; j < b; ++j)
			{
				v.push_back(i);
			}
		}  
		/*for (long i = 0; i < v.size(); ++i)
		{
			cout << v[i];
		}
		cout << endl;*/
		cout << "Case #" << c << ": " << num(v) << endl;     
	}

	return 0;
}
