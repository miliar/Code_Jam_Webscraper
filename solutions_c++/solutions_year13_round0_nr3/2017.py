#include <functional>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <utility>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>
#include <cmath>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#define ll long long
#define MAX 10000000
using namespace std;
vector <ll> v;
bool pal(ll n){
	string s = "", t = "";
	while (n != 0){
		char c = ('0' + n % 10);
		s += c;
		t = c + t;
		n /= 10;
	}
	return t == s;
}
int main(){
	for (int i = 1;i <= MAX;++i)
		if (pal(i) && pal((ll)i * i)){
			v.push_back((ll)i * i);
		//	cout << (ll)i * i << endl;
		}
	//cout << v.size() << endl;
	
	int T;
	cin >> T;
	for (int i = 0;i < T;++i){
		ll a, b;
		cin >> a >> b;
		cout << "Case #" << i + 1 << ": " << upper_bound(v.begin(), v.end(), b) - lower_bound(v.begin(), v.end(), a) << endl;
	}
	return 0;
}