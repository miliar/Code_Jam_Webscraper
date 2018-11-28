// By Anudeep :)
//Includes
#include <vector> 
#include <queue>
#include <map> 
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <sstream> // istringstream>> ostring stream<<
#include <iostream> 
#include <iomanip> 
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

//M lazy ;)
typedef long long ll;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <string> vs;
typedef pair< int ,int > pii;
typedef vector <ll> vll;
typedef istringstream iss;
typedef ostringstream oss;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz size()
#define ln length()
#define rep(i,n) for(int i=0;i<n;i++)
#define all(a)  a.begin(),a.end() 
#define ESP (1e-9)

//String Utilities 
bool isl(char c) { return (c>='a' && c<='z'); }
bool isu(char c) { return (c>='A' && c<='Z'); }
bool isa(char c) { return (isl(c) || isu(c)); }
bool isn(char c) { return (c>='0' && c<='9'); }
bool isan(char c) { return (isa(c) || isn(c)); }
bool isv(char c) { return (c=='a' || c=='e' || c=='i' || c=='o' || c=='u'); }
string tolow(string s) { rep(i,s.ln) if(isu(s[i])) s[i]=s[i]-'A'+'a'; return s; }
string toup(string s) { rep(i,s.ln) if(isl(s[i])) s[i]=s[i]-'a'+'A'; return s; }

//It all starts here ;)

//End Template
string itos(ll n) {
	string s = "";
	while(n) {
		s = char(n%10+'0')+s;
		n/=10;
	}
	return s;
}

int stoi(string s) {
	int ans = 0;
	for(int i=0; i<s.ln; i++) ans = (ans*10)+s[i]-'0';
	return ans;
}

ll palins[12*1000];
int ptr;
void prep() {
	//generate palindromes till 10^7, ie length max 8
	string s1,s2,s3;
	ptr=0;
	rep(i,10) if(i) palins[ptr++] = i;
	rep(i,1000) if(i) {
		s1 = s2 = itos(i);
		//reverse it
		reverse(all(s2));
		palins[ptr++] = stoi(s1+s2);
		//reverse wid mid num
		rep(i,10) palins[ptr++] = stoi( s1 + char('0'+i) + s2 );
	}
	int cc = ptr; ptr = 0;
	rep(i,cc) {
		long long cur = palins[i];
		cur *= cur;
		s1 = itos(cur);
		s2 = s1.substr(0,s1.ln/2);
		s1 = s1.substr(s1.ln/2);
		if(s1.ln > s2.ln) s1=s1.substr(1);
		reverse(all(s2));
		if(s1==s2) {
			// printf("%lld %lld\n",palins[i],cur);
			palins[ptr++] = cur;
		}
	}
	sort(palins,palins+ptr);
}

int testno=0;
void test() {
	printf("Case #%d: ",++testno);
	ll A,B;
	scanf("%lld%lld",&A,&B);
	//search for a
	int a,b;
	a=0;
	while(a<ptr && palins[a] < A ) a++;
	b=0;
	while(b<ptr && palins[b] <= B) b++;
	printf("%d\n",b-a);
}

int main() {
	prep();
	int t;
	scanf("%d",&t);
	while(t--) test();
	return 0;
}