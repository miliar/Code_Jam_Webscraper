#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define MOD 1000000007
#define MAXN 100001

#define PRIME 1000008259

using namespace std;

int main(){
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
	
    int tc;
	cin >> tc;
	
    for (int tc_i = 0; tc_i < tc; tc_i++) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << (tc_i + 1) << ": ";
		
		for (int i = 0; i < k; i++) {
			cout << (i + 1) << " ";
		}
		
		cout << endl;
    }

    return 0;
}