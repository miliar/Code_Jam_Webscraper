#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <queue>
#include <string>
#include <set>
#include <vector>

using namespace std;
typedef long long ll;

int main()
{
    int T;
    scanf("%d", &T);

    for ( int t = 0; t < T; t++ ) {
	string s;
	cin >> s;
	int size = s.size();
	string ret = "";
	for ( int i = 0; i < size; i++ ) {
	    if ( i == 0 ) ret += s[i];
	    else {
		if ( s[i] >= ret[0] ) {
		    ret = s[i] + ret;
		}
		else {
		    ret += s[i];
		}
	    }
	}
	
	cout << "Case #" << (t+1) << ": " << ret << endl;
    }
    
    return 0;
}
