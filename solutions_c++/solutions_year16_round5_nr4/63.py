#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
#include <complex>

using namespace std;
typedef long long ll;
typedef double ld;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

string g[1<<7];
string bad;

char a[1<<8];
char b[1<<8];

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		int n; cin >> n;
		int ll; cin >> ll;
		for (int i = 0; i < n; i++)
			cin >> g[i];
		cin >> bad;
		
		bool okay = true;
		for (int i = 0; i < n; i++){
			if (bad == g[i]){
				okay = false;
				break;
			}
		}
		if (!okay){
			cout << "Case #" << zz << ": IMPOSSIBLE" << endl;
			continue;
		}
		
		for (int i = 0; i < ll; i++){
			if (bad[i] == '0'){
				a[2*i] = '1';
				b[i] = '0';
			}
			else{
				a[2*i] = '0';
				b[i] = '1';
			}
			a[2*i+1] = '?';
		}
		a[2*ll] = 0;
		if (ll == 1){
			b[0] = a[0];
			b[1] = 0;
		}
		else b[ll-1] = 0;
		
		string sa(a);
		string sb(b);
		cout << "Case #" << zz << ": " << sa << " " << sb << endl;
	}
	
	return 0;
}
