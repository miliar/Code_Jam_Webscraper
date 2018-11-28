// Bismillahirrahmanirrahim
// AgriCoder IPB
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <sstream>
#include <clocale>
#include <ctime>
//#include <unordered_map>
using namespace std;

#define FOR(i, agri, coder) for (int i = (int)agri; i <= (int)coder; i++)
#define REP(agri,coder) for (int agri = 0; agri < (int)coder; agri++)
#define FOREACH(i,agricoder) for (typeof((agricoder).end()) i = (agricoder).begin(); i != (agricoder).end(); ++i)
//for (auto& it: agricoder)
#define RESET(agri,coder) memset(agri, coder, sizeof(agri))
#define pb push_back
#define mp make_pair
#define NL printf("==========================\n")
//#define getchar_unlocked getchar // for codeforces


int arahbar[8] = {0,1,0,-1,1,1,-1,-1};
int arahkol[8] = {1,0,-1,0,1,-1,-1,1};
int kudabar[8] = {-2,-1,1,2, 2,1 , -1 ,-2};
int kudakol[8] = {1 ,2 ,2,1,-1,-2 , -2,-1};

typedef long long ll;
typedef unsigned long long ULL;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef pair<ll,ll> PLL;

//template<typename T>
//T getNum() {
   //T res=0;
   //char c;
   //while(1)
   //{
      //c=getchar_unlocked();
      //if(c==' ' || c=='\n') continue;
      //else break;
   //}
   //bool negatif;
   //if (c=='-') {
       //negatif = true;
       //res = 0;
   //}
   //else {
       //res=c-'0';
       //negatif = false;
   //}
   //while(1)
   //{
      //c=getchar_unlocked();
      //if('0'<=c && c<='9') res=10*res + c-'0';
      //else break;
   //}
   //if (negatif) res*=-1;
   //return res;
//}

inline int mutlak(int x) {
	if (x>0) return x; return -x;
}

inline ll mutlak(ll x) {
    if (x>0) return x; return -x;
}

inline int kuadrat(int x) {
    return x*x;
}
inline ll kuadrat (ll x) {
    return x*x;
}

inline void boost() {
	//dont use with cstdio, dont use in interactives
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
}
//freopen("badmilk.in", "r", stdin);
//freopen("badmilk.out", "w", stdout);
//fclose(stdin);
//fclose(stdout);

#define INF 1000000000
#define EPS 1e-7
#define MAX_N 100005

// ================================  TEMPLATE ENDS HERE ================================================== //

bitset<10> sudah;
int jum;

void cek(ll x) {
	while (x) {
		ll wew = x%10;
		if (!sudah[(int)wew]) {
			sudah[wew] = 1;
			jum--;
		}
		x/=10;
	} 
}
int main() {
	int n;
	ll x;
	scanf("%d",&n);
	
	FOR(zz,1,n) {
		cin >> x;
		
		printf("Case #%d: ",zz);
		if (x==0) printf("INSOMNIA\n");
		else {
			int ans = 1;
			sudah.reset();
			jum = 10;
			
			cek(x);
			while (jum) {
				ans++;
				cek((ll)ans*x);
			}
			
			cout << (ll)ans*x << endl;
		}
		
	}
	
	return 0;
}

// Alhamdulillahirabbilalamin

