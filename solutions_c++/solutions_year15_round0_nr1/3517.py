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
string s;
int a[10000];
int main()
{
	//freopen("oddoreven.in", "r", stdin);
	//freopen("oddoreven.out", "w", stdout);
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	ios::ios_base::sync_with_stdio(false);
	cin>>t;
	int c,x,ch;
	int n;
	forn(qq,t){
		cin>>n>>s;
		c = 0;
		ch = 0;
		forn(i,s.length()){
			x = s[i] - '0';
			if(x == 0) continue;
			if(c >= i)
				c += x;
			else{
				ch += i - c;
				c += x + i - c;
			}
		}
		//if(c < n) ch += n - c;
		cout<<"Case #"<<qq + 1<<": "<<ch<<endl;
	}
	return 0;
}