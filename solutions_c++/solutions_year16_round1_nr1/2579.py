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
const long long MOD = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------
//
#define cin fin
////
#define cout fout

//----------------------------
#ifdef cin	
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif



string a;

int main(){
	
	int t, z = 1;
	cin >> t;
	while (t--){
		cin >> a;
		string ans;
		ans.push_back(a[0]);
		for (int i = 1; i < a.size(); i++){
			if (a[i] >= ans[0]) ans = a[i] + ans;
			else ans.push_back(a[i]);
		}

		cout << "Case #" << z++ << ": " << ans << endl;

	}


#undef cin
	int ____________;
	cin >> ____________;
	return 0;
}

