#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define Foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define rof(i,a,b) for(int (i)=(a);(i) > (b); --(i))
#define rep(i, c) for(auto &(i) : (c))
#define x first
#define y second
#define pb push_back
#define PB pop_back()
#define iOS ios_base::sync_with_stdio(false)
#define sqr(a) (((a) * (a)))
#define all(a) a.begin() , a.end()
#define error(x) cerr << #x << " = " << (x) <<endl
#define Error(a,b) cerr<<"( "<<#a<<" , "<<#b<<" ) = ( "<<(a)<<" , "<<(b)<<" )\n";
#define errop(a) cerr<<#a<<" = ( "<<((a).x)<<" , "<<((a).y)<<" )\n";
#define coud(a,b) cout<<fixed << setprecision((b)) << (a)
#define L(x) ((x)<<1)
#define R(x) (((x)<<1)+1)
#define umap unordered_map
#define double long double
typedef long long ll;
#define int ll
typedef pair<ll, ll>pii;
typedef vector<int> vi;
typedef complex<ll> point;
template <class T>  inline void smax(T &x,T y){ x = max((x), (y));}
template <class T>  inline void smin(T &x,T y){ x = min((x), (y));}
template <typename T> using os =  tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
inline int isprime(int n){
	if(n < 2)	return -1;
	if(n == 2)	return -1;
	int x = 3;
	while(x * x <= n){
		if(n % x == 0)	return x;
		x += 2;
	}
	return -1;
}
int n = 16, k = 50;
string s[] = {"1101111001101011", "1101111001101001", "1101111001101111", "1101111001100101", "1101111001110001", "1101111001111011", "1101111001010111", "1101111001010011", "1101111001000111", "1101111001000101", "1101111001001011", "1101111000000011", "1101111000000111", "1101111000001101", "1101111000001111", "1101111000001001", "1101111000011011", "1101111000011111", "1101111000010111", "1101111000100001", "1101111000100101", "1101111000100111", "1101111000101101", "1101111000101011", "1101111000111001", "1101111000111111", "1101111000110011", "1101111000110101", "1101111010101111", "1101111010101011", "1101111010101001", "1101111010100101", "1101111010100011", "1101111010110111", "1101111010111101", "1101111010011001", "1101111010010011", "1101111010010001", "1101111010000001", "1101111010000101", "1101111010000111", "1101111010001001", "1101111010001101", "1101111011101101", "1101111011101001", "1101111011100001", "1101111011100111", "1101111011100101", "1101111011111111", "1101111011110011" };
inline bool check(string a){
	cout << a << ' ';
	vi v = {2, 3, 4, 5, 6, 7, 8, 9, 10};
	//random_shuffle(all(v));
	rep(b, v){
		int x = 0;
		rep(i, a)
			x = b * x + i - '0';
		cout << isprime(x) << (b == 10? '\n': ' ');
	}
	return true;
}
main(){
	iOS;
	int T;
	cin >> T;
	For(test, 1, T + 1){
		cout << "Case #" << test << ":\n";
		For(i,0,k)
			check(s[i]);
	}
	return 0;
}
