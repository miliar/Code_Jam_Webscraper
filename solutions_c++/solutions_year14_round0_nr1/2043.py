//============================================================================
// Name        : Google.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>
#include <map>
using namespace std;
#define cin fin
#define cout fout
ifstream fin("in.in");
ofstream fout("out.out");
void inp(int a[4][4])
{
	for(int i = 0; i < 4; i ++)
		for(int j = 0; j < 4; j++)
			cin >> a[i][j];
}
int main() {
	int a[4][4];
	int T, first, second;
	cin >> T;
	for(int i = 1; i <= T; i++){
		map<int, int> m;
		int count = 0;
		cin >> first;
		inp(a);
		for(int j = 0; j < 4; j++)
			m[a[first-1][j]] = 1;
		cin >> second;
		inp(a);
		for(int j = 0; j < 4; j++)
					if(m[a[second-1][j]] == 1)
					{
						count++;
						first = a[second-1][j];
					}
		cout<<"Case #"<<i<<": ";
		if(count == 0) cout<<"Volunteer cheated!";
		else if(count == 1) cout<<first;
		else if(count > 1) cout<<"Bad magician!";
		cout<<endl;
	}
}
