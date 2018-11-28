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
#define bad {cout<<"-1"<<endl;return 0;}
//#define push(x,g) {cin>>x;g.push_back(x);}
int F(const void* l,const void* r){
    return (*(int*)l - *(int*)r);//A(n,m) * B(m,k) = C(n,k);
} 
//const ll inf = 1000000000000000003;
const ll inf = 10000000007;
int t;
ll a[10000];

int main()
{
	//freopen("oddoreven.in", "r", stdin);
	//freopen("oddoreven.out", "w", stdout);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	/*string c[1000];
	forn(i,100) getline(cin,c[i]);
	string s;
	forn(i,100) {getline(cin,s);if(c[i] != s) cout<<"FFF"<<i;}*/
	ios::ios_base::sync_with_stdio(false);
	cin>>t;
	ll c,x,ch = 0,d,v,q;
	int n;
	forn(qq,t){
		cin>>n;
		c = 0;
		ch = 0;
		forn(i,n){
			cin>>a[i]; 
			ch = max(a[i],ch);
		}
		d = ch;
		for(ll i = ch; i >= 1;i--){
			v = 0;
			c = 0;
			d = 0;
			forn(j,n){
				if(a[j] < i) continue;
				if(a[j] % i != 0) v += a[j] / i ;
				else v += a[j] / i - 1;
			}
			ch = min(ch,i + v);
		}
		cout<<"Case #"<<qq + 1<<": "<<ch<<endl;
	}
	return 0;
}