#include <bits/stdc++.h>

using namespace std;

map<int, string> mad;

string func(int aa)
{
	int i,j,k,no;

	string b;

	no = aa;

	b = "";

	do {
		i = no % 10;
		no = no /10;

		b = b+(mad[i]);

	} while (no != 0);

	sort(b.begin(), b.end());

	return b;
}

int main()
{
	mad[1] = "ONE";
	mad[2] = "TWO";
	mad[3] = "THREE";
	mad[4] = "FOUR";
	mad[5] = "FIVE";
	mad[6] = "SIX";
	mad[7] = "SEVEN";
	mad[8] = "EIGHT";
	mad[9] = "NINE";
	mad[0] = "ZERO";

	string abc;
	int i,j,k,tt,tcase;

	cin >> tcase;

	tt = 1;

	while (tcase--) {
		abc.clear();
		cout << "Case #" << tt << ": ";
		++tt;

		cin >> abc;
		
		sort(abc.begin(), abc.end());
		
		for (i = 0; i < 1000000; ++i) {
			if (func(i) == abc) {
				break;
			}
		}

		if (i < 1000000) {
//			string bk = std::to_string(i);

		stringstream convert; // stringstream used for the conversion

convert << i;//add the value of Number to the characters in the stream

string bk = convert.str();//set Result to the content of the stream
	
			sort(bk.begin(), bk.end());

			cout << bk << endl;
		} else {
			i = abc.length()/4;

			for (j = 1; j <= i; ++j)
				cout << 0;
			cout << endl;
		}			
		
	}
	
	return 0;
}
