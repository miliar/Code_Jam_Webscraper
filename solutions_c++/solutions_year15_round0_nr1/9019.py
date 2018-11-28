#include <iostream>
#include <string>

using namespace std;
int main() {
	int T,t=0;
	char c;
	int no=0;
	int no_standing=0;
	int no_required=0;
	string s;
	cin >> T;

	while ( t<T) {
	    no_standing = 0;
	    no_required = 0;
	    cin >> s;
	    cin >> s;
	    no_standing = s[0] - '0';
	    for(int i=1 ; i<s.size() ; i++) {
	        no = s[i] - '0';
	        if (no_standing < i){
	            no_required = no_required + (i - no_standing);
	            no_standing +=  i - no_standing;
	        }
	        no_standing = no_standing + no;
	    }
	    cout << "Case #"<<t+1<<": "<<no_required<<"\n";
	    t++;
	}
}
