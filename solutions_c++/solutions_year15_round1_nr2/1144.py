#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <fstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>	
#include <ctime>
#include <cstring>


using namespace std;
#define ll long long
#define EPS 0.00000001


ll a[200000];
ll b;
ll f(ll n){
	if (n == 0) return b;
	ll ans = 0;
	for (int i = 1; i <= b; i++)
		ans += n / a[i];
	return ans + b;
}
ll bs(ll n, ll x){
	if (f(0) >= x) return 0;
	ll low = 0, high = n;
	while (high - low > 1){
		ll mid = (high + low) / 2;
		if (f(mid) >= x) high = mid;
		else low = mid;
	}
	return high;
}


int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int t, z = 1;
	fin >> t;
	ll n;
	while (t--){
		fin >> b >> n;
		for (int i = 1; i <= b; i++) fin >> a[i];
		ll m = 100000000000000000, ans = 1;
		ll x = bs(m, n);
		if (x == 0) ans = n;
		else{
			n -= f(x - 1);
			for (int i = 1; i <= b; i++){
				if (x % a[i] == 0) n--;
				if (n == 0){
					ans = i; 
					break;
				}
			}
		}
		fout << "Case #" << z << ": ";
		fout << ans << endl;
		z++;
	}





	fin.close();
	fout.close();
	return 0;
}