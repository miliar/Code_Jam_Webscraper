#include <bits/stdc++.h>

using namespace std;

typedef __int128 ll;

ostream& operator << (ostream& cout, __int128 x) {
	string s;
	do {
		s += x % 10 + '0';
		x /= 10;
	} while (x);
	reverse (s.begin (), s.end ());
	cout << s;
	return cout;
}

mt19937 rnd;

int T;   
int N, J;
string s;
int n;

ll mul (ll a, ll b, ll m) {
    if (b == 1)
        return a;
    if (b % 2 == 0) {
        ll t = mul (a, b / 2, m);
        return (2 * t) % m;
    }
    return (mul (a, b - 1, m) + a) % m;
}

ll pows (ll a, ll b, ll m) {
    if (b == 0)
        return 1;
    if (b % 2 == 0) {
        ll t = pows (a, b / 2, m);
        return mul (t, t, m) % m;
    }
    return (mul (pows (a, b - 1, m) , a, m)) % m;
}

ll gcd (ll a, ll b) {
    if (b == 0)
        return a;
    return gcd (b, a % b);
}

bool isp (ll x){
    if (x == 2)
        return true;
    
    for (int i = 0; i < 100; i++) {
        ll a = (rnd () % (x - 2)) + 2;
        if (gcd (a, x) != 1)
            return false;           
        if (pows(a, x - 1, x) != 1)       
            return false;           
    }
    return true;
}           

void load () {
	cin >> N >> J;
	n = N;
}           
              
ll create (ll pos) {
	ll t = 1;
	ll val = 0;
	auto tmp = s;
	//reverse (tmp.begin (), tmp.end ());
	for (int i = 0; i < n; i++) {
		ll y = s[i] - '0';
		val += y * t;
		t *= pos;
	}
	return val;
}


void gen (int pos) {
	if (pos == n - 1) {
		bool good = true;
		/*for (int i = 2; i <= 10 && good; i++) {
			ll v = create (i);
			if (!isp (v))
				good = false;
		}    */
		if (good) {
			vector<ll> ans;
			for (int i = 2; i <= 10; i++) {
				ll v = create (i);
				
				for (ll p = 2; p * p <= v; p++) {
					if (v % p == 0) {
						ans.push_back (p);
						break;
					}
				}
			}
			if (ans.size () == 9) {
				J--;
				string tmp = s;
				reverse (tmp.begin (), tmp.end ());
				cout << tmp;
				for (auto it : ans) cout << ' ' << it;
				cout << endl;
			}
		}
		//clog << s << ' ' << J << endl;
		return;
	}

	s[pos] = '0';
	gen (pos + 1);
	if (!J)
		return;
	s[pos] = '1';
	gen (pos + 1);
}

void solve () {
	s = string (n, '0');
	s[0] = s.back () = '1';
	gen (1);			
}

int main () {                         
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);

	rnd = mt19937 (6434536);
	
	cin >> T;

	for (int tc = 1; tc <= T; tc++) {
		load ();
		cout << "Case #" << tc << ":\n";
		solve ();
	}

	return 0;
}