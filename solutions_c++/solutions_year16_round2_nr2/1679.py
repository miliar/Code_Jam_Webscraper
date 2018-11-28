

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <bitset>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <ctime>
#include <cstring>
#include <list>
//#include <forward_list>
#include <iomanip>
#include <cassert>
#include <functional>	

const double EPS = 0.00000001;
const long long mod = 1000000000 + 7;
using namespace std;
#define ll long long
#define ull unsigned long long
#define mk make_pair

//----------------------------

#define cin fin

#define cout fout

//----------------------------


#ifdef cin
ifstream fin("in.in");
#endif
#ifdef cout
ofstream fout("out.out");
#endif




ll myPow(ll a, ll n){
	ll res = 1;
	while (n){
		if (n % 2) res *= a;
		n /= 2;
		a *= a;
	}
	return res;
}

int toInt(string & a){
	stringstream ss;
	ss << a;
	int ans;
	ss >> ans;
	return ans;
}

void hhh(string a, int i, vector<int> & u){
	if(i == a.size()) {
		u.push_back(toInt(a));
		return;
	}
	if(a[i] == '?'){
		for(int j = 0; j < 10; j++){
			a[i] = '0' + j;
			hhh(a, i + 1, u);
		}
	}
	else hhh(a, i + 1, u);
	
}
void ggg(string & a, string & b){
	vector<int> u, v;
	
	hhh(a, 0, u);
	hhh(b, 0, v);
	sort(u.begin(), u.end());
	sort(v.begin(), v.end());
	int x, y, ans = 1000000;
	for(int i = 0; i < u.size(); i++){
		for(int j = 0; j < v.size(); j++){
			if(abs(u[i] - v[j]) < ans){
				x = u[i], y = v[j];
			}
			ans = min(ans, abs(u[i]- v[j]));
		}
	}
	stringstream ss ;
	ss << x;
	string xx = ss.str();
	for(int i=  xx.size(); i < a.size(); i++) cout<<0;
	cout<<xx<<" " ;
	stringstream sss;
	sss << y;
	string yy = sss.str();
	for(int i = yy.size(); i < a.size(); i++) cout<<0;
	cout<<yy<<endl;
	
}


int n;

ll dp[20][4], dir[20][4], vis[20][4];

// dir = 

// k = 0 ==> a = b
// k = 1 ==> a < b
ll f(int i, int k, string & a, string & b){
	if(i == a.size()) return 0;
	if(vis[i][k]) return dp[i][k];


	ll ans = 0;
	int d = 0;
	if(k == 0){
		if(a[i] == '?' && b[i] == '?') {
			ll r1 = f(i + 1, k, a, b);
			ll r2 = f(i + 1, 1, a, b) + myPow(10, n - i);

			ans = min(r1, r2);
			if(r1 <= r2) d = 0;
			else d = 1;
		}
		else if(a[i] == '?'){
			ll r1 = f(i + 1, k, a, b);
			ll r2 = f(i + 1, 1, a, b) +  myPow(10, n - i);

			ans = min(r1, r2);

			if(r1 < r2) d = 0;
			else d = 1;
		}
		else if(b[i] == '?'){
			ll r1 = f(i + 1, k, a, b);
			ll r2 = 1000000000000000001LL;
			if(a[i] != '9') r2 = f(i + 1, 1, a, b) + myPow(10, n - i);

			ans = min(r1, r2);
			if(r1 <= r2) d = 0;
			else d = 1;
		}
		else if(a[i] > b[i]) ans = 1000000000000000001LL;
		else if(a[i] < b[i]){
			ans = f(i + 1, 1, a, b) + myPow(10, n - i) * (b[i] - a[i]);
		}
		else ans = f(i + 1, k, a, b);
	}
	else{ // a < b
		if(a[i] == '?' && b[i] == '?') {

			ll r2 = f(i + 1, 1, a, b) - 9 * myPow(10, n - i);

			ans = r2;
		}
		else if(a[i] == '?'){

			ll r2 = f(i + 1, k, a, b) - ('9' - b[i]) * myPow(10, n - i);

			ans = r2;
		}
		else if(b[i] == '?'){
			ll r1 = f(i + 1, k, a, b) - (a[i] - '0')  * myPow(10, n - i);
			ans = r1;
			d = 1;
		}
		else {
			ans = f(i + 1, k, a, b) + (b[i] - a[i]) * myPow(10, n - i);
		}
	}
	vis[i][k] = 1;
	dir[i][k] = d;
	return dp[i][k] = ans;
}

string a, b;


int main(){

	int t, z = 1;
	cin>>t;

	while(t--){
		cin>>a>>b;
		cout<<"Case #"<<z++<<": ";
		string aa = a, bb = b;
		//ggg(a, b);
		
		a = aa, b = bb;
		n = a.size() - 1;

		memset(vis, 0, sizeof(vis));
		ll r1 = f(0, 0, a, b);
		memset(vis, 0, sizeof(vis));
		ll r2 = f(0, 0, b, a);



		if(r1 == r2){
			memset(vis, 0, sizeof(vis));
			r1 = f(0, 0, a, b);

			int i = 0, k = 0;
			while(i < a.size()){
				if(k == 0){
					if(dir[i][k] == 0) {
						if(a[i] == '?' && b[i] == '?') a[i] = b[i] = '0';
						else if(b[i] == '?') b[i] = a[i];
						else if(a[i] == '?') a[i] = b[i];
						else if(a[i] < b[i]) k = 1;
					}
					else{
						if(a[i] == '?' && b[i] == '?') {
							a[i] = '0';
							b[i] = '1';
						}
						else if(a[i] == '?') a[i] = b[i] - 1;
						else if(b[i] = '?') b[i] = a[i] + 1;
					}
				}
				else{
					if(a[i] == '?' && b[i] == '?') {
						a[i] = '9';
						b[i] = '0';
					}
					else if(a[i] == '?') a[i] = '9';
					else if(b[i] == '?') b[i] = '0';
				}
				i++;
			}

			string a1 = a, b1 = b;
			a = aa, b = bb;

			memset(vis, 0, sizeof(vis));
			r2 = f(0, 0, bb, aa);

			i = 0, k = 0;
			while(i < a.size()){
				if(k == 0){
					if(dir[i][k] == 0) {
						if(a[i] == '?' && b[i] == '?') a[i] = b[i] = '0';
						else if(b[i] == '?') b[i] = a[i];
						else if(a[i] == '?') a[i] = b[i];
						else if(a[i] > b[i]) k = 1;
					}
					else{
						if(a[i] == '?' && b[i] == '?') {
							a[i] = '1';
							b[i] = '0';
						}
						else if(a[i] == '?') a[i] = b[i] + 1;
						else if(b[i] = '?') b[i] = a[i] - 1;
						k = 1;
					}
					
				}
				else{
					if(a[i] == '?' && b[i] == '?') {
						a[i] = '0';
						b[i] = '9';
					}
					else if(a[i] == '?') a[i] = '0';
					else if(b[i] == '?') b[i] = '9';
				}
				i++;
			}

			string a2 = a, b2 = b;

			if(a1 < a2) cout<<a1 <<" " <<b1<<endl;
			else if(a1 > a2) cout<<a2 << " " << b2<<endl;
			else if(a1 == a2){
				if(b1 < b2) cout << a1 <<" " << b1<<endl;
				else if(b1 > b2) cout<<a2 <<" " << b2<<endl;
				else cout<<a1 << " " <<b1<<endl;
			}

		}
		else if(r1 < r2){
			memset(vis, 0, sizeof(vis));
			r1 = f(0, 0, a, b);

			int i = 0, k = 0;
			while(i < a.size()){
				if(k == 0){
					if(dir[i][k] == 0) {
						if(a[i] == '?' && b[i] == '?') a[i] = b[i] = '0';
						else if(b[i] == '?') b[i] = a[i];
						else if(a[i] == '?') a[i] = b[i];
						else if(a[i] < b[i]) k = 1;
					}
					else{
						if(a[i] == '?' && b[i] == '?') {
							a[i] = '0';
							b[i] = '1';
						}
						else if(a[i] == '?') a[i] = b[i] - 1;
						else if(b[i] = '?') b[i] = a[i] + 1;
						k = 1;
					}
				}
				else{
					if(a[i] == '?' && b[i] == '?') {
						a[i] = '9';
						b[i] = '0';
					}
					else if(a[i] == '?') a[i] = '9';
					else if(b[i] == '?') b[i] = '0';
				}
				i++;
			}

			cout<<a << " " <<b<<endl;
		}
		else {
			
			memset(vis, 0, sizeof(vis));
			r2 = f(0, 0, b, a);

			int i = 0, k = 0;
			while(i < a.size()){
				if(k == 0){
					if(dir[i][k] == 0) {
						if(a[i] == '?' && b[i] == '?') a[i] = b[i] = '0';
						else if(b[i] == '?') b[i] = a[i];
						else if(a[i] == '?') a[i] = b[i];
						else if(a[i] > b[i]) k = 1;
					}
					else{
						if(a[i] == '?' && b[i] == '?') {
							a[i] = '1';
							b[i] = '0';
						}
						else if(a[i] == '?') a[i] = b[i] + 1;
						else if(b[i] = '?') b[i] = a[i] - 1;
						k = 1;
					}
				}
				else{
					if(a[i] == '?' && b[i] == '?') {
						a[i] = '0';
						b[i] = '9';
					}
					else if(a[i] == '?') a[i] = '0';
					else if(b[i] == '?') b[i] = '9';
				}
				i++;
			}
			cout<<a<<" " <<b<<endl;

		}
		
			
	}


#undef cin
	int ________________;
	cin >>________________;
	return 0;
}