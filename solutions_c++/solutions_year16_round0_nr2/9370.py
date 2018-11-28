/*
	program: 
	author : rhnvrm
*/

//!! TODO Debug ON/OFF | VLL

#include <bits/stdc++.h>

using namespace std;
#define mp             make_pair
#define pb             push_back
#define fi             first
#define se             second
#define sz(x)          (int)((x).size())
#define fill(x, y)     memset(x, y, sizeof(y))
#define all(x)         (x).begin(), (x).end()
#define TC(x)          cin >> (x); while(x --)
#define debug(x)       { cout << #x << " = " << (x) << '\n'; }
#define rep(i, x, y)   for (int i = x; i < y; i ++)
#define repi(i, x, y)  for (__typeof(x) i = x; i > y; i --)
#define fore(itr, x)   for (__typeof(x.begin()) itr = x.begin(); itr != x.end(); itr ++)
#define forei(itr, x)  for (__typeof(x.end()) itr = x.end() - 1; itr != x.begin() - 1; itr --)
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
typedef long long      ll;
typedef pair<int, int> ii;
typedef pair<ii, int>  iii;
typedef vector<int>    vi;
typedef vector<ii>     vii;
typedef vector<iii>    viii;
const   int            inf = 0;
const   double         eps = 0;
const   int            ms  = 0;
const   int            md  = 0;
const   double         pi  = 2*acos(0);

template<class T> T power(T N,T P){ return (P==0)?  1: N*power(N,P-1); }


int main() {

	fast;

	long long int t,i,j,l,c=0;
	char s[1000001];
	cin>>t;
	for(j=1;j<=t;j++){
		c=0;
		cin>>s;
		l = strlen(s);
		while(1){
			i=0;
			if(s[i]=='+'){
				while(s[i]=='+' && i<l){
					i++;
				}
				if(i==l){
					break;
				}
				else{
					memset(s,'-',sizeof(char)*(i+1));
					c+=1;
				}
			}
			else if(s[i]=='-'){
				while(s[i]=='-' && i<l){
					i++;
				}
				if(i==l){
					c+=1;
					break;
				}
				else{
					memset(s,'+',sizeof(char)*(i+1));
					c+=1;
				}
 
			}
		}
		cout<<"case #"<<j<<": "<<c<<"\n";
	}
 
	return 0;
}
