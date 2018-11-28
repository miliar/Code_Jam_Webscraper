#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;



void main(){


	int T;
	int Smax;


	fstream cin;
	cin.open("in.txt", ios::binary | ios::in);

	fstream cout;
	cout.open("out.txt", ios::trunc | ios::out);

	cin >> T;

	vector<int> S;

	for (int i = 1; i <= T; i++){
	
		cin >> Smax;
		char temp;
		
		S.clear();

		for (int j = 0; j <= Smax; j++){
		
			cin >> temp;
			S.push_back(temp - '0');

		}

		int current = S[0];
		int required = 0;
		for (int j = 1; j < S.size(); j++){
		
			if (j > current){
			
				required += j - current;
				current += j - current;
			}
			current += S[j];

		}
		cout << "Case #" << i << ": " << required << endl;
	}

	system("pause");
}