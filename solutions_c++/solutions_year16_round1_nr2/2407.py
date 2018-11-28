#include <iostream>
using namespace std;
#include <stdio.h>
#include <string.h>
int main() {
	int h[2500];
	int c =0; 
	cin >> c;
	for(int i =0; i < c;++i)
	{
		memset(h, 0, sizeof(h));
		cout << "Case #" << i +1 << ":";
		int a;
		cin >> a;
		for(int j  =0; j < (2*a -1) * a ; ++j )
		{
			int t;
			cin >> t;
			h[t] +=1;
		}
		for(int j =0; j < 2500;++j)
		{
			if(h[j] % 2)
			{
				cout << " " << j;
			}
		}
		cout << "\n";
	}
	// your code goes here
	return 0;
}
