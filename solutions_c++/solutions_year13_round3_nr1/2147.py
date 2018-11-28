#include <iostream>
#include <fstream>
#include <string.h>
#include <map>
#include <vector>
#include <cmath>
#include <list>
#include <string>
#include <sstream>

using namespace std;

bool isconsonant(char c){
	if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u')
		return true;
	else return false;
}

bool startend(string &str, unsigned int subsize, int first, int &s, int &e){
	for(unsigned int i=first; i<str.length(); i++){
		s = i;
		if(isconsonant(str[i]))
		for(unsigned int j=i; j < str.length(); j++){
			e = j;
			if(isconsonant(str[e])){
				if(j-i + 1 == subsize)
					return true;
			}
			else{
				i = j;
				break;
			}
		}
	}
	return false;
}

int main(int argc, char **argv)
{
	istream &in  = (argc>1)?*(new ifstream(argv[1])):cin;
	ostream &out = (argc>2)?*(new ofstream(argv[2])):cout;

	int T;
	in >> T;

	for(int t=0; t<T; t++){
		int n;
		string name;
		in >> name >> n;

		int first = 0;
		int s, e;
		int total = 0;
		int counter = -1;
		while(startend(name, n, first, s, e)){
//			out << "Start " << s << " end " << e << endl;
			total += (s-counter)*(name.length()-e);
			counter=s;
			first = s+1;
		}
		out << "Case #" << t+1 << ": " << total <<endl;
	}

	return 0;
}


