#include <algorithm>
#include <bitset>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>
// q.push(el);
// q.front(); q.pop(); 

#include <sstream>
// ostringstream buf;

#include <cstdio>
// sscanf(time.c_str(), "%d:%d:%d", &H, &M, &S);

#include <limits>
// std::numeric_limits<long long>::max();

typedef long long ll;
#include <fstream>

int main() {
    std::string line;
    std::ifstream fin ("Asmall.in");

    ll T;
    fin >> T;

    for (ll icase = 1; icase<=T; icase++) {
	ll n;
	fin >> n;

	std::string s;
	fin >> s;

	ll need_invite  = 0;
	ll n_standing   = 0;

	for (size_t sl = 0; sl<s.size(); sl++) {
	    ll  n_guest = s[sl] - '0';
	    //	    std::cout << "n_st: " << sl << ' ' << n_guest <<
	    //		' ' << n_standing <<
	    //		' ' << need_invite << '\n';	    
	    if (n_standing < sl && n_guest>0) {
		need_invite += sl - n_standing;
		n_standing  += sl - n_standing;
	    }
	    n_standing += n_guest;
	}
	std::cout << "Case #" << icase << ": " << need_invite << '\n';
    }
}
