#include <algorithm>
#include <bitset>
#include <deque>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define fst first
#define snd second
#define all(x) (x).begin(), (x).end()
#define clr( a , v ) memset( a , v , sizeof(a) )
#define pb push_back
#define mp make_pair
#define sz size()
#define FORN( i , s , n ) for( int i = s ; i < (int)(n) ; i++ )
#define FOR( i , n ) FORN( i , 0 , n )
#define FORIT(i,x) for( typeof x.begin() i = x.begin() ; i != x.end() ; i++ )
#define trace(x)    cerr << #x << ": " << x << endl;
#define trace2(x, y) cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define read ios::sync_with_stdio(false)
#define unos(x) __builtin_popcount (x)
#define TAM 1000005

using namespace std;

typedef long long int64;
typedef vector <int> vi;
typedef pair <int,int> ii;
typedef vector <string> vs;
typedef vector <ii> vii;



int main() {
	int T; cin>>T;
	FOR(i,T){
		int X,R,C;
		cin>>X>>R>>C;
		cout<<"Case #"<<i+1<<": ";
			 if(X==1) cout<<"GABRIEL";
		else if(X==2 && (((R*C))%2==0)) cout<<"GABRIEL";
		else if(X==3 && (((R*C))%3==0) && (R*C)>3) cout<<"GABRIEL";
		else if(X==4 && ((R*C)==12 || (R*C)==16) ) cout<<"GABRIEL";
		else cout<<"RICHARD";
		cout<<endl;
	}
	return 0;
}