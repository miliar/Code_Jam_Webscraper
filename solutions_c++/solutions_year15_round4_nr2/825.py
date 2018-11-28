#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i, k, n) for (int i = (int)(k); i < (int)(n); i++)
#define forba(i, n, k) for (int i = (int)(n) - 1; i >= (int)(k); i--)

#define vi vector<int>
#define pii pair<int, int>
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define X first
#define Y second                    
#define pb push_back
#define mp make_pair

using namespace std;

typedef long long ll;
typedef double ld; 

const ld pi = acos(-1.0);
const ld eps = 1e-9;
const int INF = 1E9;        
const int MAXN = 111;
                                                                             
int t, n;
ld V, C, x[MAXN], v[MAXN], w[MAXN], ans, minV, mid;
ld l, r, maxR;                           

bool check(ld T) {
	forn(i, n)
		if (!(0 <= w[i] && w[i] <= v[i] * T))
			return 0;
	ld c = 0;
	forn(i, n)
		c += w[i] * x[i];
	c /= V;
	return (abs(c - C) < eps);
}

bool good(ld T) {
	bool f = 0;
	if (n == 1) {
		w[0] = V;
		f |= check(T);		
	} else {
		if (abs(x[0] - x[1]) < eps) {
			if (abs(C - x[0]) > eps)
				return 0;
			f |= ((v[0] + v[1]) * T) >= V;
		} else {
			w[0] = V * (C - x[1]) / (x[0] - x[1]);
			w[1] = V - w[0];
			assert(abs(w[0] + w[1] - V) < eps);
			f |= check(T);
			if (f) {
				ld c = 0;
				forn(i, n)
					c += w[i] * x[i];
				c /= V;
				assert(abs(c - C) < eps);
			}	
		}	
	}
	    	
	return f;
}

int main() {

	cout.precision(30);

  	scanf("%d\n", &t);
  	
  	forn(tt, t) {
  		printf("Case #%d: ", tt + 1);
  		cin >> n >> V >> C;

  		forn(i, n)
  			cin >> v[i] >> x[i];
  		/*
  		if (n == 1) {
  			cerr << n << ' ' << V << ' ' << C << '\n';
  			forn(i, n)
  				cerr << v[i] << ' ' << x[i] << '\n';	
  		}
  		*/
  		minV = v[0];
  		forn(i, n)
  			minV = min(minV, v[i]);
  		l = 0;
  		r = maxR = 1E18;//V / minV * 10.0;
  		forn(j, 100000) {
  			mid = (l + r) / 2;
  			if (good(mid))
  				r = mid;
  			else
  				l = mid;
  		}
  		
  		assert((r - l) <= 1);
  		if (!good(r))
  			cout << "IMPOSSIBLE\n";
  		else {
  			cout << r << '\n';
  			assert(good(r));
  		    /*
  			if (r < 0.0001) {
  			cout << n << ' ' << V << ' ' << C << '\n';
  			forn(i, n)
  				cout << v[i] << ' ' << x[i] << '\n';	
  			}
  			*/
  		}      
  		
  	}  	
  	  		    
	return 0;
}