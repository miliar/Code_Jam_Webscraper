#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main()
{
	int t, sm, i = 0;
	string str;
	ofstream fo;
	fo.open ("A-large - Output.txt");
	fstream fi("A-large.in.txt", std::ios_base::in);
	fi >> t;
	while(t--){
		fi >> sm;
		fi >> str;

		unsigned long long s = 0, n = 0;
		int ite = 0;
		for(std::string::size_type it = 0; it < str.size(); it++, ite++){
		//char *it = str;
		//for(; *it; it++, ite++){
			if(s < ite){
				n++; s++;
				s += str[it] -'0';
			} else{
				s += str[it] -'0';
				//fo << s << " ";
			}
		}
		//fo << endl;
		fo << "Case #" << i+1 << ": " << n << endl;
		i++;
	}
	return 0;
}
