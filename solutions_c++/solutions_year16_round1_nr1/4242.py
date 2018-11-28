#include<fstream>
#include<iostream>
using namespace std;

int main ( ) {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	
	int test; fin >> test; fin.ignore();
	for ( int tc=1; tc<=test; ++tc ) {
		string str; getline(fin, str);
		
		string tmp;
		tmp += str[0];
		for ( int i=1; i<str.size(); ++i ) {
			if ( str[i] < tmp[0] ) tmp += str[i];
			else {
				string newStr; 
				newStr += str[i];
				newStr += tmp;
				tmp = newStr;
			}
		}
		
		cout << "Case #" << tc << ": " << tmp << endl;
		fout << "Case #" << tc << ": " << tmp << endl;
	}
}
