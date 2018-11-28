#include <iostream>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
	int lines;
	int len;
	int total = 0;
	int min = 0;
	string aud;

	cin >> lines;
	
	for(int i = 0; i < lines; i++)
	{
		cin >> len;
		cin >> aud;

		for(int j = 0; j <= len; j++)
		{
			min += aud[j]-'0';
			if(total >= j){
				total += aud[j] - '0';
			}
			else{
				total += j - total;
				total += aud[j]-'0';
			}
		}

		cout << "Case #" << i+1 << ": " << total-min << endl;

		// reinitialize values
		len = 0;
		aud = "";
		total = 0;
		min = 0;


	}	
	

	return 0;
}


