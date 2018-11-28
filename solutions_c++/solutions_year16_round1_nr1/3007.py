#include <iostream>
#include <cmath>
#include <iomanip>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <deque>

using namespace std;

int main()
{
	int times;
	int loopcount = 1;
	cin >> times;
	string temp;
	getline(cin,temp);

	while(times--)
	{
		deque<char> data;
		string s;
		getline(cin,s);
		data.push_back(s[0]);
		char flag = s[0];
		for(int i = 1; i < s.size(); i++)
		{
			if(s[i] >= flag)
			{
				data.push_front(s[i]);
				flag = s[i];
			}
			else
			{
				data.push_back(s[i]);
			}
		}


		cout << "Case #" << loopcount << ": ";
		for(int i = 0; i < data.size(); i++)
		{
			cout << data[i];
		}
		cout << endl;
		loopcount++;

		data.clear();

	}

	

	return 0;
}
