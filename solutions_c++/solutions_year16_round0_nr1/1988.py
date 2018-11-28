#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
//#include <forward_list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin
//
#define cout fout

//----------------------------
#ifdef cin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif

int a[10];

void g(ll x){
	while (x){
		a[x % 10] = 1;
		x /= 10;
	}
}
ll f(ll x){
	memset(a, 0, sizeof(a));
	for (ll y = 1; y < 100; y++){
		int fnd = true;
		g(y * x);
		for (int i = 0; i < 10; i++)
			if (!a[i]) fnd = false;
		if(fnd) return y * x;
	}
}
int main(){
	ios::sync_with_stdio(0);
	
	int t, z = 1;
	cin >> t;
	while (t--){
		int n;
		cin >> n;
		ll ans = 0;
		if (n != 0) ans = f(n);
		cout << "Case #" << z << ": ";
		if (ans) cout << ans << endl;
		else cout << "INSOMNIA" << endl;
		z++;
	}

#undef cin
	int ____________;
	cin >> ____________;
	return 0;
}