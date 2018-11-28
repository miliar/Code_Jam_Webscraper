#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main () {  
    freopen("A-large.in", "r", stdin); 
    freopen("A-large.out", "w", stdout);
  
    int _T, check, Smax, pemalu, stand, _friend=0, _friendInv=0;
    string Audience;
    
    scanf("%d", &_T);
    for(int _t = 1; _t <= _T; ++_t) {	
	scanf("%d", &Smax);
	cin >> Audience;		
	
	stand=0;
	_friend=0;
	_friendInv=0;
	for(check=0; check <= Smax; check++) {
	    pemalu = Audience[check] - '0'; 
	    if(stand >= Smax) break;
	    else if(stand >= check) stand += pemalu; 
	    else if(stand < check && pemalu != 0){
		_friend = (check-stand);
		_friendInv += _friend;
		stand += pemalu + _friend; 
	    }
	}
	 
	printf("Case #%d: %d\n", _t, _friendInv);
    }
  return 0;
}

