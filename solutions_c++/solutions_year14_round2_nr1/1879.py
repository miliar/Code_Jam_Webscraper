#define _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <unordered_set>
#include <unordered_map>
#include <numeric>
#include <tuple>
#include <cassert>
#include <cstring>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
#define rp(i,s,n) for((i)=(s);(i)<(n);(i)++)	
#define fore(x,Z) for(__typeof((Z).begin()) x=(Z).begin();x!=(Z).end();++x)
#define repe(it,a) for(auto (it) = (a).begin();(it)!=(a).end();++(it))

#define ll long long
#define MP make_pair 
#define MT make_tuple
#define PB push_back
#define X first
#define Y second
#define ALL(a) (a).begin(),(a).end()
#define SZ(a) (a).size()
#define LEN(s) (s).length() 
#define uset unordered_set
#define umap unordered_map
#define IT iterator

#pragma comment(linker,"/STACK:100000000")

using namespace std;			

#define NUMBERS(a,b) { int _i_; vector<int> _A_(((b))-(a)); rep(_i_,_A_.size()) _A_[_i_] =_i_+(a); out(_A_);}

template <class T> void out(map<char,T> & a,string s="(%3c ->%3d)"){repe(it,a) printf(s.c_str(),it->X,it->Y);printf("\n");}

template <class T>void out(vector<T> & a,string s="%3d "){int i,n=a.size();rep(i,n) printf(s.c_str(),a[i]);printf("\n");}

template <class T>void out(T * a,int n,string s="%3d "){int i;rep(i,n) printf(s.c_str(),a[i]);printf("\n");} 


ll i,j,N,M,n,m,k,p;


int GoogleSolve(){
	int _T,_t;
	cin>>_t;
	_T = _t;
	while(_t--){
		
		cin>>n;
		int const N = 105;
		vector<pair<char,int> > a[N];
		ll  k =0;
		int ok = 1;
		string s;
		rep(i,n) {
			cin>>s;
			char last = '#';
			for(auto el : s){
				if (el != last) {
					a[i].PB(MP(el,1));
					last = el;
				}
				else a[i][a[i].size()-1].Y++;
			}
			
			if (i) {
				if(a[i-1].size() != a[i].size()) ok =0;
				if (ok) rep(j,a[i].size()) if (a[i][j].X != a[i-1][j].X) {ok=0;break;}
			}
			if (!ok) break;
		}
		
		
		if (ok)
		rep(j,a[0].size()){
			vector<int> cur(n);
			rep(i,n) cur[i] = a[i][j].Y;
			sort(ALL(cur));
			size_t pos = (cur.size()-1)>>1;
			ll sm = 0;
			rep(i,n) sm += abs(cur[i]-cur[pos]);
			k += sm;
		}
		
		
		
		printf("Case #%d: ",_T-_t);
		cerr<<"Log: Test number "<<_T-_t<<endl;
		//answer here
		if (!ok) printf("Fegla Won\n");
		else{
			cout<<k<<endl;
		}
		
	}
	return 0;
}


int main() {

	//freopen("C:\\Olimp2014\\JAM1B_A\\input.txt","r",stdin);
	//freopen("C:\\Olimp2014\\JAM1_14_B\\input.txt","r",stdin);
	 freopen("A-small-attempt0.in","r",stdin);freopen("output-small-attempt.txt","w",stdout);//FILE * f, *g; f = fopen ("input.txt","r");//g = fopen ("output.txt","w");
	// freopen("B-large.in","r",stdin);freopen("output-large.txt","w",stdout);
	//freopen("B-small-practice.in","r",stdin);freopen("output-small-practice.txt","w",stdout);//FILE * f, *g; f = fopen ("input.txt","r");//g = fopen ("output.txt","w");
	//freopen("B-large-practice.in","r",stdin);freopen("output-large-practice.txt","w",stdout);//FILE * f, *g; f = fopen ("input.txt","r");//g = fopen ("output.txt","w");
	GoogleSolve();
return 0;
}