#include "iostream"
using namespace std;
int main(int argc, char const *argv[])
{
	int t;
	string s;
	cin >> t;
	int count;
	for (int i = 0; i < t; ++i)
	{
		cin >> s;
		s = s + "+";
		count = 0;
		int size = s.size();
		for (int j = 0; j < size-1; ++j)
		{
			if(s[j]!=s[j+1])
			{
				count++; 
			}
		}

		cout << "Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}