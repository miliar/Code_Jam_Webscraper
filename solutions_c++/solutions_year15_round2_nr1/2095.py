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
typedef vector <int64> vi;
typedef pair <int,int> ii;
typedef vector <string> vs;
typedef vector <ii> vii;

int64 MCD (int64 x,int64 y){
        return (y==0 ? x:MCD(y,x%y));
}
 
int64 MCM(int64 x ,int64 y){
        return (x*y/MCD(x,y));
}

int64 voltear(int64 x){
	if(x%10==0) return x;
	string aux=to_string(x);
	reverse(all(aux));
	int64 j=stol(aux);
	return j;
}

int64 llegar[]={0,1,11,30,139,338,1437,3436,14435,34434,144433,344432,1444431,3444430};
//int64 llegar[]={0,0,11,29,137,335,1433,3431,14429,34427,144425,344423,1444421,3444419};
int64 pot[]=   {0,0,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000
				,100000000000,1000000000000};
int main() {
    int T;cin>>T;
    FOR(i,T){
        int64 ans=0 ,N; 
        cin>>N;
        if(N%10==0)	{ans+=9; N-=9;}
        int64 aux=1;
        string cad=to_string(N);
       	aux=aux*pot[cad.size()]+1;
       	//cout<<aux<<endl;
       	ans+=llegar[cad.size()];
       	//cout<<aux<<endl;
       	//cout<<cad<<endl;
       	string cad1=cad.substr(0,ceil(cad.size()/2.0));
       	//string cad2=cad.substr(ceil(cad.size()/2.0));
       	reverse(all(cad1));
       	int dif1=stol(cad1)+pot[cad.size()];
       	//cout<<dif1<<endl;
       	ans+=(dif1-aux); 
       	//cout<<aux<<" "<<ans<<endl;
       	if(dif1!=voltear(dif1)) {ans++;dif1=voltear(dif1);}
       	ans+=(N-dif1);
        cout<<"Case #"<<i+1<<": "<<ans <<endl;
    }
    
    return 0;
}