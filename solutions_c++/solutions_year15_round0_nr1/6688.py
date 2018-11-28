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
#define clr(a, v) memset( a , v , sizeof(a) )
#define pb push_back
#define mp make_pair
#define sz size()
#define FORN( i , s , n ) for( int i = (s) ; i < (n) ; i++ )
#define FOR( i , n ) FORN( i , 0 , n )
#define FORIT( i , x ) for( typeof x.begin() i = x.begin() ; i != x.end() ; i++ )
#define trace(x)    cerr << #x << ": " << x << endl;
#define trace2(x, y) cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define read ios::sync_with_stdio(false)

using namespace std;

typedef long long int64;
typedef vector <int> vi;
typedef pair <int,int> ii;
typedef vector <string> vs;
typedef vector <ii> vii;

int main(){
	int  numT,N;
	char S[10005];
	
	cin>>numT;
	
	FOR(caso,numT){
		cin>>N;
		scanf("%s",S);
			
		int stand=0;
		int cnt=0;		
		
		FOR(i,N+1){
			int act = S[i]-'0';
			if(stand>=i) stand += act;
			else{
				cnt+=  i-stand;
				stand = i+act;
			}
			
		}	
		
		printf("Case #%d: %d\n",caso+1,cnt);	
	}	
		
		
	return 0;
}












