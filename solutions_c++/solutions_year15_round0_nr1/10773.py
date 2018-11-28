#include <bits/stdc++.h>
using namespace std;

int main(){

	int t;
	cin >> t;
	int max;
	
	for (int i = 0; i < t; ++i)
	{	
		int soma = 0, cont = 0;
		cin >> max;
		char s[max+1];
		bool b[max+1];
		for (int j = 0; j < max+1; ++j)
		{
			cin >> s[j];		
		}
		for (int j = 0; j < max; ++j)
		{
			soma += s[j] - '0';
			if (soma < j+1)
				{cont++; soma++;}
			
		}
		
		cout << "Case #" << i+1 << ": " << cont << endl;
	}
	
	return 0;
}

