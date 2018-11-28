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
    std::ifstream fin ("Dsmall.in");

    ll T;
    fin >> T;

    for (ll icase = 1; icase<=T; icase++) {
	ll X, R, C;
	fin >> X >> R >> C;
	std::string ans = "RICHARD";

	if (C>R) std::swap(C, R);
	//	std::cout << '\n';
	//	std::cout << X << ' ' << R << ' ' << C << '\n';
	if (X == 1)
	    ans = "GABRIEL";
	else if (X == 2) {
	    if ( ( R==2 && C==1) ||
		 ( R==2 && C==2) || 
		 ( R==3 && C==2) ||
		 ( R==4        )
		 )
		ans = "GABRIEL";
	} else if (X == 3) {
	    if ( ( R==3 && C==2) ||
		 ( R==3 && C==3) ||
		 ( R==4 && C==3)
		 )
		ans = "GABRIEL";
	} else if (X == 4) {
	    if ( ( R==4 && C==3) ||
		 ( R==4 && C==4)
		 )
		ans = "GABRIEL";
	}
	
	std::cout << "Case #" << icase << ": " << ans << '\n';
    }

}
