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


string num[]={"ZERO","SIX","TWO", "FOUR", "EIGHT", "FIVE", "SEVEN","NINE", "ONE" , "THREE"};
map<char,int> usos;
int main() {
	int T;cin>>T;
	FOR(i,T){
		string resp="";
		usos.clear();
		string cad;
		cin >> cad;
		FOR(k,cad.size()){
			usos[cad[k]]++;
		}
		FOR(j,10){
			int letras=999999;
			FOR(k,num[j].size()){
				if((j==6 || j==9 ) && num[j][k]=='E') {
					letras=min(usos[num[j][k]]/2,letras);	
				}
				else
					letras=min(usos[num[j][k]],letras);	
			}
			FOR(k,num[j].size()){
				usos[num[j][k]]-=letras;	
			}
			FOR(k,letras)
				 if(j==0)resp+=('0');
			else if(j==1)resp+=('6');
			else if(j==2)resp+=('2');
			else if(j==3)resp+=('4');
			else if(j==4)resp+=('8');
			else if(j==5)resp+=('5');
			else if(j==6)resp+=('7');
			else if(j==7)resp+=('9');
			else if(j==8)resp+=('1');
			else if(j==9)resp+=('3');			
		}
		sort(all(resp));
		cout<<"Case #"<<i+1<<": "<<resp<<endl;
	}
	return 0;
}