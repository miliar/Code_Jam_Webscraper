#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <stdlib.h>
#include <ctime>
#include <queue>
#include <set>
#include <iostream>
#include <stack>
#include <list>
#include <bitset> 
//#include <WinDef.h> 
//#include <iterator> map<string,int>::iterator i;
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<ll> vc;
#define mp make_pair
#define forn(i,n)	for(ll i = 0; i < n; i++)
#define forn2(i,n)	for(ll i = 1; i <= n; i++)
#define forn3(i,n,s) for(ll i = s; i <= n; i++)
#define forn4(i,n)	for(ll i = n; i >= 0; i--)
#define bad {cout<<"1 1";return 0;}
//#define push(x,g) {cin>>x;g.push_back(x);}
int F(const void* l,const void* r){
    return (*(int*)l - *(int*)r);//A(n,m) * B(m,k) = C(n,k);
} 
//const ll inf = 1000000000000000003;
const ll inf = 1000000007; 
ll n,t;
ll c;
ll bw (ll a, ll n) {
	ll res = 1;
	while (n) {
		if (n & 1)
			res *= a;
		a *= a;
		n >>= 1;
	}
	return res;
}
ll rev(ll x){
	ll x2 = x;
	ll l = 0;
	while(x2){
		l++;
		x2 /= 10;
	}
	x2 = x;
	ll t = 0;
	forn(i,l)
		t += bw(10,l-i-1) * (x2 % 10),x2 /= 10;
	return t;
}
ll prov(ll x){
	vc a;
	vc b;
	ll x2 = x,n2 = n;
	//if(n >= x && n - x <= 2) return n - x;
	while(x2){
		b.push_back(x2 % 10);
		x2 /= 10;
	}
	while(n2){
		a.push_back(n2 % 10);
		n2 /= 10;
	}
	reverse(a.begin(),a.end());
	reverse(b.begin(),b.end());
	if(a.size() > b.size()){
		if(b[0] == 9){
			ll t = bw(10,b.size()) + 2;
			if(t >= n) return -1;
			else{
				c += t - x - 1;
				return t - x;
			}
		}
		else{
			c++;
			return 2;
		}
	}
	else{
		int j = 0,h = b.size() / 2;
		//while(j < h){	
			for(int i = j; i < b.size(); i++)
				if(a[i] != b[i]) {
					j = i;
					break;
				}
				if(j >= h) return -1;
				else{
					if(b.size() % 2 == 0){
						/*ll q1 = 0,q2 = 0;
						for(int i = b.size() - j - 1; i < b.size(); i++)
							q1 += bw(10,b.size() - j - i) * b[i];
						forn(i,j+1) q2 += bw(10,j) * a[j-i];
						if(q2 - q1 <= bw(10,j)){

						}
						else
							return q2 - q1;*/
						return bw(10,b.size() - j - 1) * (a[j] - b[b.size() - j - 1]);
					}
					else{
						return bw(10,b.size() - j - 1) * (a[j] - b[b.size() - j - 1]);
					}
				}
		//}
	}
}
ll d[1010010];
int main()
{
	//freopen("oddoreven.in", "r", stdin);
	//freopen("oddoreven.out", "w", stdout);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	ios::ios_base::sync_with_stdio(false);
	cin>>t;
	ll k;
	ll z;
	/*forn(vv,t){
		cin>>n;
		if(n <= 20) c = n;
		else{
			ll pr = n;
			ll n2 = 12;
			c = 12;
			k = rev(n);
			if(k < n && n % 10 != 0) c++,n = k;
			while(n2 != n){
				k = rev(n2);
				if(k <= n && k > n2) n2 = k,c++;
				else{
					z = prov(n2);
					if(z == -1){
						c += n - n2;
						break;
					}
					else{
						c++;
						n2 += z;
					}
				}
			}
		}
		cout<<"Case #"<<vv+1<<": "<<c<<endl;
	}*/
	forn2(i,20) d[i] = i;
	for(int i = 21; i <= 1000001;i++){
				k = rev(i);
				d[i] = d[i-1] + 1;
			  if(i > k && i % 10 != 0)  d[i] = min(d[i],d[k] + 1);
	}
	forn(vv,t){
		cin>>n;
		cout<<"Case #"<<vv+1<<": "<<d[n] + c<<endl;
	}
	return 0;
}