#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const double eps = 1e-8;
const int dx[] = { 1, 0, -1, 0, -1, -1, 1, 1 };
const int dy[] = { 0, 1, 0, -1, -1, 1, -1, 1 };
const int OO = INT_MAX;

#define SZ(x)          (int)x.size()
#define ALL(x)         (x).begin(),(x).end()
#define ALLR(x)        (x).rbegin(),(x).rend()
#define rep(i,st,en)    for(int i=st ; i< en; i++)
#define repR(i,st,en)   for(int i=st;i>=en ; i--)
#define fill(v, d)       memset(v, d, sizeof(v))
/**************************************************************/
ll isprimeDash(ll num){

	for(ll i = 2; i*i < num; i+=2){
		if(num % i == 0){
			return i;
		}
	}
	for(ll i = 3; i*i < num; i+=2){
		if(num % i == 0){
			return i;
		}
	}
	return 0;
}

vector<string>all;
int n, j ;
void generateAll(string s){
	if(SZ(s) == n-1){
		s += '1';
		all.push_back(s);
		return;
	}
	generateAll(s+'0');
	generateAll(s+'1');
}

ll conv(string s, int base){
	reverse(ALL(s));
	ll res = 0;
	ll p = 1;
	rep(i, 0, SZ(s)){
		res += (s[i]== '0'?0:p);
		p *= base;
	}
	return res;
}


int main() {

	freopen("C-small-attempt0.in" , "r",stdin);
	freopen("C-small-attempt0.out", "w", stdout);

	int T;
	cin >> T;
	rep(t, 1, T+1){
		cin >> n >> j;
		generateAll("1");
		vector< pair<string, vector<ll> > >jamcoins;
		int cnt = 0;
		while(SZ(jamcoins) < j && SZ(all) > cnt){
			vector<ll>divs;
			rep(base, 2, 11){
				ll num = conv(all[cnt], base);
				ll pp = isprimeDash(num);
				if(pp == 0){
					break;
				}
				divs.push_back(pp);
			}
			if(SZ(divs) == 9){
				jamcoins.push_back({all[cnt], divs});
			}
			cnt++;
		}
		printf("Case #%d:\n", t);
		rep(i, 0, j){
			cout << jamcoins[i].first;
			rep(x, 0, 9){
				cout << ' ' << jamcoins[i].second[x];
			}
			cout << '\n';
		}
	}

	return 0;
}
