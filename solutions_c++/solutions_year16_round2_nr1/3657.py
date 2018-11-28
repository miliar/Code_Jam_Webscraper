#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	int T;
	cin >> T;
	vector<int> num;

	for (int i = 0; i < T; i++)
	{
		string entry;
		cin >> entry;
		char freq[26];
		for (int k = 0; k < 26; k++)
		{
			freq[k] = 0;
		}
		for (int j = 0; j < entry.length(); j++)
		{
			if (entry[j] == 'A') {freq[0] += 1;}
			if (entry[j] == 'B') {freq[1] += 1;}
			if (entry[j] == 'C') {freq[2] += 1;}
			if (entry[j] == 'D') {freq[3] += 1;}
			if (entry[j] == 'E') {freq[4] += 1;}
			if (entry[j] == 'F') {freq[5] += 1;}
			if (entry[j] == 'G') {freq[6] += 1;}
			if (entry[j] == 'H') {freq[7] += 1;}
			if (entry[j] == 'I') {freq[8] += 1;}
			if (entry[j] == 'J') {freq[9] += 1;}
			if (entry[j] == 'K') {freq[10] += 1;}
			if (entry[j] == 'L') {freq[11] += 1;}
			if (entry[j] == 'M') {freq[12] += 1;}
			if (entry[j] == 'N') {freq[13] += 1;}
			if (entry[j] == 'O') {freq[14] += 1;}
			if (entry[j] == 'P') {freq[15] += 1;}
			if (entry[j] == 'Q') {freq[16] += 1;}
			if (entry[j] == 'R') {freq[17] += 1;}
			if (entry[j] == 'S') {freq[18] += 1;}
			if (entry[j] == 'T') {freq[19] += 1;}
			if (entry[j] == 'U') {freq[20] += 1;}
			if (entry[j] == 'V') {freq[21] += 1;}
			if (entry[j] == 'W') {freq[22] += 1;}
			if (entry[j] == 'X') {freq[23] += 1;}
			if (entry[j] == 'Y') {freq[24] += 1;}
			if (entry[j] == 'Z') {freq[25] += 1;}
		}

		while (freq[25] > 0)
		{
			freq[25] -= 1;
			freq[4] -= 1;
			freq[17] -= 1;
			freq[14] -= 1;
			num.push_back(0);
		}

		while (freq[23] > 0)
		{
			freq[18] -= 1;
			freq[8] -= 1;
			freq[23] -= 1;	
			num.push_back(6);		
		}

		while (freq[20] > 0)
		{
			freq[5] -= 1;
			freq[14] -= 1;
			freq[20] -= 1;		
			freq[17] -= 1;	
			num.push_back(4);		
		}

		while(freq[17] > 0)
		{
			freq[19] -= 1;
			freq[7] -= 1;
			freq[17] -= 1;		
			freq[4] -= 2;
			num.push_back(3);				
		}

		while(freq[6] > 0)
		{
			freq[4] -= 1;
			freq[8] -= 1;
			freq[6] -= 1;		
			freq[7] -= 1;		
			freq[19] -= 1;
			num.push_back(8);	
		}

		while(freq[5] > 0)
		{
			freq[5] -= 1;
			freq[8] -= 1;
			freq[21] -= 1;		
			freq[4] -= 1;
			num.push_back(5);
		}

		while(freq[22] > 0)
		{
			freq[19] -= 1;
			freq[22] -= 1;
			freq[14] -= 1;	
			num.push_back(2);
		}

		while(freq[21] > 0)
		{
			freq[18] -= 1;
			freq[4] -= 1;
			freq[21] -= 1;		
			freq[4] -= 1;
			freq[13] -= 1;
			num.push_back(7);
		}

		while(freq[14] > 0)
		{
			freq[14] -= 1;
			freq[13] -= 1;
			freq[4] -= 1;	
			num.push_back(1);
		}

		while(freq[8] > 0)
		{
			freq[8] -= 1;
			freq[13] -= 2;
			freq[4] -= 1;
			num.push_back(9);
		}

		int arewedone = 1;

		for (int k = 0; k < 26; k++)
		{
			if (freq[k] != 0)
			{
				arewedone = 0;
				cout << k << endl;
			}
		}
		sort(num.begin(), num.begin() + num.size());

		if (arewedone == 0)
		{
			cout << "WE ARE IN BIG FUCK" << endl;
		}

		cout << "Case #" << i+1 << ": ";
		for (int j = 0; j < num.size(); j++)
		{
			cout << num[j];
		}

		cout << endl;

		for (int j = 0; j < num.size(); j++)
		{
			num.erase(num.begin(), num.begin()+num.size());
		}
	}

}