/*
 * a1.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: hassan
 */

#include <bits/stdc++.h>

using namespace std;

typedef long long                       ll;
typedef unsigned long long              ull;
typedef pair<int,int>                   ii;
typedef vector<int>                     vi;
typedef vector<vector<int> >            vvi;
typedef vector<pair<int,int> >          vii;
typedef vector<vector<pair<int,int> > > vvii;
typedef complex<double>                 point;

#define PI                 (acos(-1.0))
#define EPS                (1e-12)
#define MOD                ((int)(1e9)+7)
#define Inff               ((int)(1e8))
#define pb                 push_back
#define mp                 make_pair
#define X                  real()
#define Y                  imag()
#define polar(r,t)         ((r)*exp(point(0,(t))))
#define length(a)          hypot((a).X,(a).Y)
#define angle(a)           atan2((a).Y,(a).X)
#define vec(a,b)           ((b)-(a))
#define dot(a,b)           ((conj(a)*(b)).real())
#define cross(a,b)         ((conj(a)*(b)).imag())
#define length_sqr(a)      dot(a,a)
#define rotate(v,t)        ((v)*exp(point(0,t)))
#define rotateabout(v,t,a) (rotate(vec(a,v),t)+(a))
#define reflect(v,m)       (conj((v)/(m))*(m))
#define endl               "\n"

int cases;

string t;

int n;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> cases;
    for(int CASE = 1 ; CASE <= cases ; ++CASE) {
    	cin >> n >> t;
    	int ppl = t[0] - '0';
    	int ans = 0;
    	for(int i = 1 ; i < t.size() ; ++i) {
    		if(ppl < i)
    			ans += i-ppl, ppl += i-ppl;
    		ppl += t[i] - '0';
    	}
    	cout << "Case #" << CASE << ": " << ans << endl;
    }
    return 0;
}
