#include <iostream>
#include <sstream>
#include <cstdio>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define FOR(i,n) for(int i = 0 ; i<n ;i++)
#define f(i,x,y) for (int i = x; i < y; i++)
#define all(v) v.begin(),v.end()
#define pb push_back
#define sz(v) ((int)v.size())
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
#define oo 2000000000

typedef long long ll  ;
typedef vector<int> vi ;
typedef pair<ll,ll> ill;
typedef pair<int,int> ii ;
typedef pair<ii, int> tri;

int num[100002];

int reverse(int i){
	for(int j=0;j<=i;j++){
		num[j]=abs(num[j]-1);
	}
}

int main(){
	string s;
	int t;
	cin>>t;
	int m=t;
	while(m--){
		cin>>s;
		vi plus, minus,v;
		int n=(int)s.size();
		for(int i=0;i<n;i++){
			plus.pb(1);
			minus.pb(0);
			if(s[i]=='+'){
				num[i]=1;
			}
			else{
				num[i]=0;
			}
		}
		int cont=0;
		for(int i=0;i<n;i++){
			v.clear();
			if(i!=n-1 and num[i]!=num[i+1]){
				reverse(i);
				cont++;
			}
			for(int j=0;j<n;j++){
				//cout<<num[j];
				v.pb(num[j]);
			}
			if(v==plus){
				break;
			}
			else if(v==minus){
				cont++;
				break;
			}
		}
		cout<<"Case #"<<abs(m-t)<<": ";
		cout<<cont;
		if(m) cout<<endl;
	}
	return 0;
}