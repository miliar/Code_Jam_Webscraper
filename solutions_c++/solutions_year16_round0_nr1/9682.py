// #define _CRT_SECURE_NO_WARNINGS
// #define _USE_MATH_DEFINES
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <functional>
#include <locale>
#include <cctype>
#include <sstream>
#include <iomanip>	// 10桁出力 cout << setprecision(10) << double;
#include <queue>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef map<int, int> MAPII;
typedef multimap<int, char, greater<int> > MuMAPIC;
typedef vector<pair<int, int> > VPII;
typedef multimap<int, string, greater<int> > MuMIS;
typedef pair<int, int> P;
typedef pair<int, pair<P, P> > PP;

#define MP make_pair
#define FAST_IO  cin.tie(0); ios::sync_with_stdio(false);
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
//for gcc (未test)
// #define FOREACH_IT(it,c) for(typeof(c)::iterator it=(c).begin(); it!=(c).end(); ++it)
//for Visual Studio
#define foreach_it(type,it,c) for(type::iterator it=c.begin(),c_end=c.end();it!=c_end;++it)
// for Debug.
#define DUMP_VVI(b) FOR(i,0,b.size()){FOR(j,0,b[i].size())printf("%d ",b[i][j]);puts("");}
#define D_OUT(str,value) if(dbgF){cout<<str<<" : "<<value<<endl;}
// 入力をpush_back(d)やarray[d]に使う時に1行で書ける
// int INPUT_INT() {int d;cin>>d;return d;}
template<class T>T IN() { T d; cin >> d; return d; }
// 最大公約数（Greatest Common Divisor）
LL gcd(LL a, LL b) { return (b > 0) ? gcd(b, a%b) : a; }
// 最小公倍数（Least Common Multiple）
LL lcm(LL a, LL b) { return a / gcd(a, b) * b; }
// Y年はうるう年か否か
bool uruu(LL Y) { return (((Y % 4 == 0 && Y % 100 != 0) || Y % 400 == 0) ? true : false); }

// vector注意
// vec[i][j]の形に入力を入れるとき、vecは初期化してある必要がある.

// ------------------- include, typedef, define END. -------------------

int main() {
	FAST_IO;
	// for D_OUT(str, value)  ... cout<< str <<" : "<< value <<endl;
	bool dbgF = true;

	//コードはここから書く.

	int T;
	LL N;

	cin >> T;
	FOR(i, 0, T) {
		cin >> N;
		bool ans[10];
		FOR(i, 0, 10) {
			ans[i] = false;
		}
		bool finFlg;
		FOR(j, 1, 100) {
			int temp = N*j;
			//cout << "formae" << endl;

			while (to_string(temp).length() > 1) {
				//cout << "now temp = " << temp << endl;
				int nowDigit = temp % 10;
				//cout << "nowDi = " << nowDigit << endl;
				temp /= 10;
				ans[nowDigit] = true;
			}
			ans[temp] = true;

			
			// finish check
			finFlg = true;
			FOR(a, 0, 10) {
				//cout << "ans[" << a << "] = " << ans[a] << endl;
				if (ans[a] == false) {
					finFlg = false;
				}
			}
			if (finFlg) {
				cout << "Case #" << i+1 << ": " << N*j << endl;
				break;
			}
		}
		if(finFlg==false)
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
	}


	return 0;
}