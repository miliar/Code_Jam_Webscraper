#include <iostream>
#include <string>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;
	int possibles[4];
	string str;
	for(int i=0; i<numCases; ++i)
	{
		//FIRST SET
		int test = 0;
		int cur;
		int firstAnswer;
		cin >> firstAnswer;

		for (int r=0; r<firstAnswer; ++r) getline(cin, str); //skip empty lines
		for (int r=0; r<4; ++r) cin >> possibles[r]; //read in important ones
		for (int r=firstAnswer; r<=4; ++r) getline(cin, str); //skip more empty lines

		//SECOND SET
		cin >> firstAnswer;

		for (int r=0; r<firstAnswer; ++r) getline(cin, str); //skip empty lines
		for (int r=0; r<4; ++r)
		{
			cin >> cur;
			for (int c=0; c<4; ++c) 
				if (cur==possibles[c] && !test) test=cur;
				else if (cur==possibles[c] && test) test = 100;
		}
		for (int r=firstAnswer; r<=4; ++r) getline(cin, str); //skip more empty lines

		cout << "Case #" << i+1 << ": ";
		if (test == 100) cout << "Bad Magician!" << endl;
		else if (test) cout << test << endl;
		else cout << "Volunteer cheated!" << endl;
	}
	//cout << possibles[0] << endl;
}