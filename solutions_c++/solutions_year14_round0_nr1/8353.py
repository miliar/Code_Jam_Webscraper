#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define Fit(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define inf 1000000005
#define all(a) (a).begin(), (a).end()
#define ms(a,x) memset(a, x, sizeof(a))
#define maxn (1 << 20) + 5
#define mod 1000000007

template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return s == 0 ? 0 : cntbit(s >> 1) + (s & 1);}

typedef unsigned long long ull;
typedef long long ll;

typedef long double ld;

int test;
int r, a[10][10];

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> test;
	for(int itest = 1; itest <= test; itest++){
		set<int> S, SS;
		cin >> r;
		for(int i = 1; i <= 4; i++) for(int j = 1; j <= 4; j++){
			cin >> a[i][j];
			if(i == r) S.insert(a[i][j]);
		}
		cin >> r;
		for(int i = 1; i <= 4; i++) for(int j = 1; j <= 4; j++){
			cin >> a[i][j];
			if(i == r && S.count(a[i][j])){
				SS.insert(a[i][j]);
			}
		}

		cout << "Case #" << itest << ": ";

		int size = (int)SS.size();
		if(size == 1){
			cout << *(SS.begin()) << endl;
		}
		else if(size == 0){
			cout << "Volunteer cheated!" << endl;
		}
		else cout << "Bad magician!" << endl;
	}
}
