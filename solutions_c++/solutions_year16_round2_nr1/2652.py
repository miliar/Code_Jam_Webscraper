
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <ctime>
#include <iostream>

#include <set>
#include <map>
#include <list>
#include <deque> /* have op [] */
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

#define READ(f)  freopen(f, "r", stdin )
#define WRITE(f) freopen(f, "w", stdout)

#define D1(a)     cout << "[ " << #a << " : " << a << " ]" << endl ;  
#define D2(a,b)   cout << "[ " << #a << " : " << a << " , " << #b << " : " << b << " ]" << endl  
#define D3(a,b,c) cout << "[ " << #a << " : " << a << " , " << #b << " : " << b << " , " << #c << " : " << c << " ]" << endl  

#define FOR(i,a,b) for(int i(a);i<=b;++i)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i(a);i>=b;--i)

#define ALL(c)    (c).begin(), (c).end()
#define SORT(c)   sort(ALL(c))
#define ZERO(x)   memset(x,0,sizeof x);
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())

#define MAX_I  2147483647
#define MAX_LL 9223372036854775807LL

#define MAXPQ(T) priority_queue<T>
#define MINPQ(T) priority_queue<T,vector<T>,greater<T> >

template< typename T > bool inside(T a, T b, T c) { return ( a<=b and b<=c ) ; }

int dx[]={ 0, 1, 0,-1, 1, 1,-1,-1 };
int dy[]={ 1, 0,-1, 0,-1, 1, 1,-1 };
//[this,=,&,(&x,&y)](int a , int b )-> int { return } lamda

using namespace std;

typedef long long llint;
typedef pair<int ,int > PII ;
typedef pair<llint ,llint > PLL ;
typedef pair<int ,PII > PIPII ;

const int inf = -1u/2 ; // 1023456789 
const int MOD = 1 ;
const int N   = 0 ;

string a[11] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE" } ; 
int ord[11] = {6,8,0,3,2,4,5,7,1,9};

void solve(){
	static int ii = 1 ;
	int arr[2000] ; 
	char in[2004] ; 
	scanf(" %s",in);
	ZERO(arr);
	for(int i=0;i<strlen(in);i++) arr[in[i]]++ ; 
	string ans = "" ; 
	REP(i,10){
		while( true ){
			bool cc = true ; 
			for(int j=0;j<a[ord[i]].length();j++){
				if( arr[a[ord[i]][j]] == 0 ){cc = false ; break; }
			}
			if( cc == false ) break ; 
			else {
				for(int j=0;j<a[ord[i]].length();j++)
					arr[a[ord[i]][j]]-- ; 
				ans += '0'+ord[i] ; 
			}
		}
	}	
	sort(ALL(ans));
	cout << "Case #"<<ii<<": "<<ans << endl;
	ii++; 

}

int main(int argc, char const *argv[]){
	READ("/Users/JET/Desktop/A-large.in.txt");
	WRITE("/Users/JET/Desktop/A-large.out.txt");
	int t ; scanf("%d",&t);
	while(t--)solve();

	return 0 ;

}
