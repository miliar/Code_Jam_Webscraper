#include <iostream>
using namespace std;
#include <string>
int main() {
	int c;
	cin >> c;
	for(int i =0; i < c;++i)
	{
		cout << "Case #" << i +1 << ": ";
		string s;
		cin >> s;
		string r(s.c_str(), 1);
		for(unsigned j =1; j < s.size();++j)
		{
			if(s[j] >= r[0])
			{
				r = string(1, s[j]) + r;
			}
			else
			{
				r += s[j];
			}
			
		}
		cout << r << "\n";
	}
	// your code goes here
	return 0;
}
