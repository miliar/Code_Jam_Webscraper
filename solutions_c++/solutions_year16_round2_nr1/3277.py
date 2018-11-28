#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

int isPresent(string s, char t) {
	int count=0;
	for ( std::string::iterator it=s.begin(); it!=s.end(); ++it) {
		if(*it == t){
			count++;
		}	
	}
	return count;
}

void removeChars(string& target, string s) {
	for ( std::string::iterator it=s.begin(); it!=s.end(); ++it) {
		for( std::string::iterator it1=target.begin(); it1!=target.end(); ++it1) {
			if(*it==*it1) {
				target.erase(it1);
				break;
			}
		}
	}
}

int main() {
        int cases=0;
        cin >> cases;

        for(int casesIter=0;casesIter<cases;casesIter++) {
		char sOrig[2000];
                scanf("%s\n", sOrig);
		string s = sOrig;
		string seq="GZWXSHVIRO";
		string target="8026735941";
		string ans;
		std::map<char, string> m;
		m.insert(std::pair<char, string>('G', "EIGHT"));
		m.insert(std::pair<char, string>('Z', "ZERO"));
		m.insert(std::pair<char, string>('W', "TWO"));
		m.insert(std::pair<char, string>('X', "SIX"));
		m.insert(std::pair<char, string>('S', "SEVEN"));
		m.insert(std::pair<char, string>('H', "THREE"));
		m.insert(std::pair<char, string>('V', "FIVE"));
		m.insert(std::pair<char, string>('I', "NINE"));
		m.insert(std::pair<char, string>('R', "FOUR"));
		m.insert(std::pair<char, string>('O', "ONE"));

		for ( std::string::iterator it=seq.begin(),itTarget=target.begin(); itTarget!=target.end(); ++it, ++itTarget) {
			int count=0;
			count = isPresent(s,*it);
			if(count) {
				while(count>0){
					ans += *itTarget;
					removeChars(s, m.find(*it)->second);
					count--;
				}
			
			}
		std::sort(ans.begin(), ans.end());
		}
		cout<<"Case #"<<casesIter+1<<": "<<ans<<endl;
	}
	return 0;
}

		
