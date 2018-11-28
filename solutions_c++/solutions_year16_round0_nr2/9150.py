#include <iostream>
using namespace std;

int main(){
	int t;
	string str;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int patches=1;
		cin >> str;
		for (int j = 0; j < str.size()-1; ++j)
		{
			if(str[j]!=str[j+1])
				patches++;
		}
		if(str[str.size()-1]=='+')
			patches--;

		cout <<"Case #" << i << ": " << patches << endl;
	}
}