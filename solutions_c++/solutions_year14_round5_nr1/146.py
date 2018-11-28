#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<iomanip>
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define pb push_back
#define mini(a,b) a=min(a,(b))
#define maxi(a,b) a=max(a,(b))
#define RE(i,n) for(int i=0,_n=(n);i<_n;++i)
#define RI(i,n) for(int i=1,_n=(n);i<=_n;++i)
#define pii pair<int,int>
#define mp make_pair
#define st first
#define nd second
const int nax = 1e6+5;
ll inf = 1e9 + 5;

ll t[nax], s[nax];
ll razem;
int n;

/*bool check(ll x) {
	s[n] = inf;
	if(*upper_bound(s, s + (n + 1), x) == s[0]) {
		// dsafasdf
	}
	ll a = *(upper_bound(s, s + (n + 1), x) - 1);
	ll b = *lower_bound(s, s + (n + 1), razem - x);
	return a <= x && b - a <= x && razem - b <= x;
}*/

void Test()
{
	int n;
	ll p, q, r, pyk;
	cin >> n >> p >> q >> r >> pyk;
	RE(i, n) t[i] = (  ((ll) i)   * p + q) % r + pyk;
	s[0] = t[0];
	RI(i, n - 1) s[i] = s[i - 1] + t[i];
	razem = s[n - 1];

	int low = 0, high = n - 1;
	ll raz, dwa;
	raz = dwa = 0;
	ll res = inf;

	if(n == 1 || razem == 0LL) {
		cout << "0\n";
		return;
	}
	/*
	else if(n == 2) {
		ll suma = t[0] + t[1];
		ll jeden = min(t[0], t[1]);
		ld wynik = jeden;
		wynik /= (ld) suma;
		cout << setprecision(15) << wynik << "\n";
		return;
	}*/

	while (low <= high) {
		if(raz + t[low] < dwa + t[high]) {
			raz += t[low];
			low++;
		}
		else {
			dwa += t[high];
			high--;
		}
		mini(res, max(raz, max(dwa, razem - raz - dwa)));
	}

	res = razem - res;
	ld wynik = res;
	wynik /= (ld) razem;

	cout << setprecision(15) << wynik << "\n";

	/*ll low = 0, high = razem;
	while(low < high) {
		ll med = (low + high) / 2LL;
	}*/
}

int main() {
	inf *= inf;
	ios_base :: sync_with_stdio(0);
	int z;
	cin >> z;
	RI(i, z) {
		cout << "Case #" << i << ": ";
		Test();
	}
	return 0;
}