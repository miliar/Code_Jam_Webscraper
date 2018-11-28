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


string a;
int sum[200];

vector<char> v;
int f(){
	char prev = a[0];
	for (int i = 1; i < a.size(); i++){
		if (a[i] == prev) continue;
		else{
			v.push_back(prev);
		}
		prev = a[i];
	}
	v.push_back(prev);
	reverse(v.begin(), v.end());
}
int g(){
	int ans = 0;
	if (v.size() == 1){
		if (v.back() == '-') ans  = 1;
		v.pop_back();
	}
	else if (v.size() == 2){
		if (v.back() == '-') ans = 1;
		else ans = 2;
		v.clear();
	}
	else{
		v.pop_back();
		v.pop_back();
		ans = 2;
	}
	return ans;

}



int main(){
	ios::sync_with_stdio(0);
	
	int t, z = 1;
	cin >> t;
	while (t--){
		memset(sum, 0, sizeof(a));
		int ans = 0;
		
		cin >> a;
		f();
		while (!v.empty()) ans += g();
		

		cout << "Case #" << z++ << ": " << ans << endl;
	}

#undef cin
	int ____________;
	cin >> ____________;
	return 0;
}