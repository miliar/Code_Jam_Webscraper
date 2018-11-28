#include<string>
#include<fstream>
#include<iostream>
#include<windows.h>
using namespace std;

string func ( string exp ) {
	if ( exp == "1*1" ) return "1";
	else if ( exp == "1*i" || exp == "i*1" || exp == "-1*-i" || exp == "-i*-1" ) return "i";
	else if ( exp == "1*j" || exp == "j*1" || exp == "-1*-j" || exp == "-j*-1" ) return "j";
	else if ( exp == "1*k" || exp == "k*1" || exp == "-1*-k" || exp == "-k*-1" ) return "k";
	else if ( exp == "-1*i" || exp == "1*-i" ) return "-i";
	else if ( exp == "-1*j" || exp == "1*-j" ) return "-j";
	else if ( exp == "-1*k" || exp == "1*-k" ) return "-k";
	else if ( exp == "i*i" || exp == "-i*-i" ) return "-1";
	else if ( exp == "i*-i" || exp == "-i*i" ) return "1";
	else if ( exp == "i*j" || exp == "-i*-j" ) return "k";
	else if ( exp == "i*-j" || exp == "-i*j" ) return "-k";
	else if ( exp == "i*k" || exp == "-i*-k" ) return "-j";
	else if ( exp == "i*-k" || exp == "-i*k" ) return "j";
	else if ( exp == "j*j" || exp == "-j*-j" ) return "-1";
	else if ( exp == "j*-j" || exp == "-j*j" ) return "1";
	else if ( exp == "j*i" || exp == "-j*-i" ) return "-k";
	else if ( exp == "j*-i" || exp == "-j*i" ) return "k";
	else if ( exp == "j*k" || exp == "-j*-k" ) return "i";
	else if ( exp == "j*-k" || exp == "-j*k" ) return "-i";
	else if ( exp == "k*k" || exp == "-k*-k" ) return "-1";
	else if ( exp == "k*-k" || exp == "-k*k" ) return "1";
	else if ( exp == "k*i" || exp == "-k*-i" ) return "j";
	else if ( exp == "k*-i" || exp == "-k*i" ) return "-j";
	else if ( exp == "k*j" || exp == "-k*-j" ) return "-i";
	else if ( exp == "k*-j" || exp == "-k*j" ) return "i";
}

int main ( )
{
	ifstream fin ("C-small-attempt1.in");
	ofstream fout ("output2.out");
	
	int test;
	fin >> test;
	
	for ( int t=1; t<=test; ++t ) 
	{
		int len, concatenate;
		fin >> len >> concatenate;
		
		string tmp;
		fin >> tmp;
		
		int read = 0;
		for ( int i=0; i<tmp.size(); ++i ) {
			if ( read == 1 ) {
				tmp.insert(i, "*");
				read = 0;
			}
			else ++read;
		}
		
		tmp += '*';
		
		string str;
		for ( int i=1; i<=concatenate; ++i ) str += tmp;
		
		str = str.substr(0,str.size()-1);
		
		string exp;
		int index = 0, chread = 0;
		bool ifi = false, ifj = false, ifk = false;
		while ( str[index] != '\0' ) {
			if ( str[index] == 'i' && !ifi && exp.size() == 0 ) {
				ifi = true;
				str = str.substr(2, str.size());
			}
			if ( str[index] == 'j' && ( ifi && !ifj ) && exp.size() == 0 ) {
				ifj = true;
				str = str.substr(2, str.size());
			}
			if ( str[index] == 'k' && ( ifi && ifj && !ifk ) && str.size() == 1 ) ifk = true;
			
			if ( ifi && ifj && ifk ) break;
			
			
			if ( str[index] != '-' && str[index] != '*' ) ++chread;
			exp += str[index];
			
			if ( chread == 2 ) {
				string tmp = func(exp);
				exp = "";
				chread = 0;
				
				if ( tmp.size() > 1 ) {
					str[index] = tmp[1];
					str.insert(index, "-");
					str = str.substr(2, str.size());
				}
				else {
					str[index] = tmp[0];
					str = str.substr(2, str.size());
				}
				
				if ( str[0] == '*' ) str = str.substr(1, str.size());
				index = -1;
			}
		
			++index;
		}
		
		cout << "Case #" << t << ": ";
		fout << "Case #" << t << ": ";
		if ( ifi && ifj && ifk ) { cout << "YES" << endl; fout << "YES" << endl; }
		else { cout << "NO" << endl; fout << "NO" << endl; }
	}
	
	fin.close();
	fout.close();
}
