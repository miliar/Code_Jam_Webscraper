#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <cmath>
#include <cstdlib>
#include <string>

using namespace std;


bool isGood(string s) {
	for(string::iterator it = s.begin(); it != s.end() ; it++){
		if( *it == '-')
			return false;
	}
	return true;
}

int main() {
        int cases=0;
        cin >> cases;

        for(int casesIter=1;casesIter<cases+1;casesIter++) {
                string s;
		cin>>s;
		int tries=0;
		char prev;
		
		while(isGood(s) == false) {
			prev = '*';
			for(string::iterator it = s.begin(); it != s.end() ; it++){

				if(prev == '*')
					prev = *it;
				else if(prev != *it)
					break;

				if(*it == '-')	
					*it = '+';
				else
					*it = '-';
				

			}
			tries++;			

		}
		cout<<"Case #"<<casesIter<<": "<<tries<<endl;
	}

	return 0;
}
