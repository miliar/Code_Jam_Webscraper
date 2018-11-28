#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cstdio>

using namespace std;

set <char> st;

#define SMALL
//#define LARGE

string IntToString (int a)
{
    ostringstream temp;
    temp << a;
    return temp.str();
}

int main(){

	#ifdef SMALL
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	#endif
	#ifdef LARGE
		freopen("B-large.in","rt",stdin);
		freopen("B-large.out","wt",stdout);
	#endif

    int i, j, t, n, x;
    long long mul;
    string s;
    ostringstream temp;  //temp as in temporary


    cin >> t;
    for(x = 1; x<=t; x++){
        st.clear();
        cin>> n;
        if(n == 0){
           cout<< "Case #"<< x <<": "<< "INSOMNIA" << endl;
            continue;
        }
        for(i=1; ; i++){

            mul = i*n;

            s = IntToString(mul);

            for(j =0; j<s.length(); j++){
                st.insert(s[j]);
            }
            if(st.size() == 10){
                break;
            }
        }
        cout<< "Case #"<< x <<": "<< s << endl;
    }

	return 0;
}
