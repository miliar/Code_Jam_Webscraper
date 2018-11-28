#include <bits/stdc++.h>
#define _USE_MATH_DEFINES
#define pb push_back
#define mp make_pair
#define ll long long
#define vi vector <int>
#define ii pair <int, int>
#define vii vector < ii >
#define vll vector <ll>
#define hash1 10000000000000061ll
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define na(x) ((x)<P?(x):(x)-P)
#define X first
#define Y second
using namespace std;
//__________________________

int n, t, p, ans;
string s;
//_________________________________________
int main(){

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>t;
	for(int t1 = 1; t1 <= t; ++t1){
		cin>>n>>s;

		p = s[0] - '0';
		for(int i = 1; i <= n; i++){
			if(i > p){
				ans += i - p;
				p += i - p;
			}
			p += s[i] -'0';
		}
		cout<<"Case #"<<t1<<": "<<ans<<endl;
		ans = 0;
	}

    return 0;
}
