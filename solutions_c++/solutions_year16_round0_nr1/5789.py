#include <cstdio> 
#include <cmath>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <fstream>
using namespace std;


int main()
{
	int t;
	cin >> t;
	int test = 1;
	ofstream myfile("codejam.txt");
	while(t--)
	{
		
		int x;
		cin >> x;
		set<char> digits;
		int total = 0;
		if (x == 0)
			myfile << "Case #" << test << ": " << "INSOMNIA" << endl;
		else
		{
			int i = 1;
			while (digits.size() < 10)
			{
				string num = to_string(x*i);
				//cout << num << endl;
				for (int j = 0; j < num.size(); ++j)
				{
					digits.insert(num[j]);
					if(digits.size() == 10)
						break;
				}
	
				total = x*i;
				i++;
			}
			myfile << "Case #" << test << ": " << total << endl;
		}
		test++;
	}
	myfile.close();

	return 0;
}
