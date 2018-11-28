#include<fstream>
#include<windows.h>
#include<iostream>
using namespace std;

int main ( ) {
	ifstream fin("B-large.in");
	ofstream fout("B-large-output.out");
	
	int test; fin >> test; fin.ignore();
	for ( int tc=1; tc<=test; ++tc ) {
		string str; getline(fin, str);
		
		int turn = 0;
		while ( str[str.size()-1] == '+' ) str = str.substr(0, str.size()-1);
		
		if ( str.size() > 0 ) {
			turn = 1;
			char ch = str[0];
			for ( int i=0; i<str.size(); ++i ) {
				if ( ch != str[i] ) {
					ch = str[i];
					++turn;
				}
			}
		}
		
		cout << "Case #" << tc << ": " << turn << endl;
		fout << "Case #" << tc << ": " << turn << endl;
	}
}
