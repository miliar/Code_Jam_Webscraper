#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		string s;
		
		cin >> s;
		
		string front_str;
		string back_str;
		
		char curr_front = (char) 0;
		
		for(int j = 0; j < s.size(); j++)
			if(curr_front <= s[j])
			{
				curr_front = s[j];
				front_str.push_back(s[j]);
			}
			else
				back_str.push_back(s[j]);
				
		reverse(front_str.begin(), front_str.end());
		
		cout << "Case #" << i << ": " << front_str << back_str << endl;
	}
	
	return 0;
}