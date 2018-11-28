#include <bits/extc++.h>
#include <iostream>

using namespace std;

//#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif
#define WRITE(x) DEBUG { cout << (x) << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << (x) << endl; }
//#define ALL(x) (x).begin(), (x).end()
//#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); ++i)
//#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

#define MAXN 1014

int as[MAXN];
int bs[MAXN];
int tmp[MAXN];
int n;

int invcnt(int b, int e){
	if(b >= e) return 0;
	int m = (b + e) / 2;
	int total = 0;
	total += invcnt(b, m);
	total += invcnt(m + 1, e);
	int pb = b;
	int pe = m + 1;
	for(int i = b; i <= e; i++){
		if(pe > e or (pb <= m and bs[pb] < bs[pe])){
			tmp[i] = bs[pb++];
		}else{
			total += m - pb + 1;
			tmp[i] = bs[pe++];
		}
	}
	for(int i = b; i <= e; i++) bs[i] = tmp[i];
	return total;
}

int solve(){
	int sol = n * n;
	sort(as, as + n);
	for(int m = 0; m < n; m++){
		
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int ntc;
	cin >> ntc;
	for(int tc = 0; tc < ntc; tc++){

	}
}
