#include <iostream>
#include <map>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;

typedef long long Long;
typedef long double Double;
namespace Helper
{
    template<typename T> inline string inttos(T x){ostringstream q;q << x;return q.str();}
    inline int stoint( string str){istringstream in(str);int res;in >> res;return res;}
    inline Long stolong(string str){istringstream in(str);Long res;in >> res;return res;}
    template<typename T> inline T pow(T x, T n, T MOD){T res = 1;while (n>0) {if (n & 1) {res = 1ll*res * x % MOD;}x = 1ll*x * x % MOD;n/=2;}return res;}
    template<typename T> inline T gcd(T a, T b){a=abs(a);b=abs(b);while ((a>0) && (b>0)) {if (a>b)a%=b;else b%=a;}return a+b;}
    inline int rand() { long long q = 1ll*rand()*RAND_MAX+rand(); return q % INT_MAX; }
    inline int abs(int x) { if (x<0) return -x;else return x; }
    const int MAXINT = 0x7FFFFFFF;
}

#ifdef h0me
#define FILES freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILES
#endif

vector<string> readWords(string & s, int q = 100)
{
	vector<string> v;
	istringstream in(s);
	string str;
	while (in >> str) {
		v.push_back(str);
	}
	return v;
}

vector<string> A[111];
vector<int> a[111];
int fra[1111],eng[1111];

int used[11111];
//map<string,int> mp;
int main() {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		cout << "Case #"<<test<<": ";
	//	mp.clear();
		
		int n;
		cin >> n;
		cin.ignore(256,'\n');
		string str;
		getline(cin, str);
		vector<string> Eng = readWords(str);
		getline(cin, str);
		vector<string> Fra = readWords(str);
		
		n -= 2;
		/*
		for (map<string, int>::iterator it = mp.begin(); it != mp.end(); ++it) {
			cout << it->first << " " << it->second << endl;
		}*/

		int engs = Eng.size();
		int fras = Fra.size();
		
		for (int i = 0; i < n; ++i) {
			getline(cin, str);
			A[i] = readWords(str);
			a[i].clear();
		}

		vector<string> allStrings;
		for (int i = 0; i < engs; ++i) {
			allStrings.push_back(Eng[i]);
		}
		for (int i = 0; i < fras; ++i) {
			allStrings.push_back(Fra[i]);
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < A[i].size(); ++j) {
				allStrings.push_back(A[i][j]);
			}
		}
		sort(allStrings.begin(), allStrings.end());
		map<string, int> mp2;
		mp2[allStrings[0]] = 1;
		int t = 1;
		for (int i = 1; i < allStrings.size(); ++i) {
			if (allStrings[i] != allStrings[i-1]) {
				t++;
				mp2[allStrings[i]]=t;
			}
		}
		int allstrs = t;
		for (int i = 0; i < Eng.size(); ++i) {
			eng[i] = mp2[Eng[i]];
//			cout << eng[i] << " ";
		}
//		cout << endl;
		for (int i = 0; i < Fra.size(); ++i) {
			fra[i] = mp2[Fra[i]];
			//cout << fra[i] << " ";
		}
		//cout << endl;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < A[i].size(); ++j) {
				a[i].push_back(mp2[A[i][j]]);
//				cout << a[i].back() << " ";
			}
			//cout << endl;
		}
		
		


		
		int mmask = 1<<n;
		int res = 1000000000;
		for (int mask = 0; mask < mmask; ++mask) {
			memset(used,0,sizeof(used));
			for (int i = 0; i < Eng.size(); ++i) {
				used[eng[i]] |= 1;
			}
			for (int i = 0; i < Fra.size(); ++i) {
				used[fra[i]] |= 2;
			}
		
			for (int i = 0; i < n; ++i) {
				int q = 2;
				if ((mask & (1<<i))>0) {
					q = 1;
				}

				for (int j = 0; j < a[i].size(); ++j) {
					used[a[i][j]] |= q;
				}
			}
			int ress=0;
			for (int i = 0; i <= allstrs+10; ++i) {
				if (used[i]==3) 
					ress++;
			}
			if (ress<res)
				res = ress;

			
		}
		cout << res << endl;
	}

    return 0;
}