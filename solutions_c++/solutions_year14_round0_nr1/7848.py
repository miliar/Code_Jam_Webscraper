// C++ libraries
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <typeinfo> // for badcast

// C libraries
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <assert.h>

using namespace std;

// TYPES
typedef long long int64;
typedef unsigned long long uint64;
typedef long double ld;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii; 

// CONSTANTS
const double PI=acos(-1.0);
const double EPS=1e-11;
#define INF 2000000000

#define FOR(k,a,b) for(decltype(a) k=(a); k < (b); k++)
#define REP(k,a) for(unsigned int k=0; k < (a); ++k)
#define all(c) (c).begin(), (c).end()  
#define pb push_back 
#define mp make_pair 
#define pbp(x, y) pb(mp(x,y))
#define sz(a) int((a).size()) 
#define tr(c,it) for(auto it = (c).begin(); it != (c).end(); ++it)  //iterate a container
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define pow2(X) (1<<(X))
#define pow2L(X) (((int64)(1))<<(X))

// for debug
#define WATCH(x) {cout<<__FILE__<<":"<<__LINE__<<":WATCHING:"<<#x<<": ";tr(x, it){cout<<*it<<", ";}cout<<endl;}
#define PEEK(x) {cout<<#x<<"="<<x;}

// Macros para leer cantidad de casos e imprimir resultados
#define READCases int cases, cs; cin >> cases; FOR(cs, 1, cases + 1)
#define PRINTSolution(res) cout << "Case #" << cs << ": " << (res) << endl;

// Maths
template<class T> inline T sqr(T x){return x*x;}//NOTES:sqr
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit
template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber
  {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}//NOTES:dist
double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}//NOTES:distR
  
//Translator
bool isUpperCase(char c){return c>='A' && c<='Z';}//NOTES:isUpperCase
bool isLowerCase(char c){return c>='a' && c<='z';}//NOTES:isLowerCase
bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}//NOTES:isLetter
bool isDigit(char c){return c>='0' && c<='9';}//NOTES:isDigit
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}//NOTES:toLowerCase
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}//NOTES:toUpperCase

// funcion para convertir de un tipo In a otro Out
template<typename Out, typename In> Out lexical_cast(In input) {
    stringstream ss; ss << input;
    Out r;
    if ((ss >> r).fail() || !(ss >> std::ws).eof()) throw std::bad_cast();
    return r;
}

int main()
{   
	int cards[2][4][4];
    int row[2];
	READCases {
		for (int k = 0 ; k < 2 ; ++k) {
			cin >> row[k];
			for (int i = 0; i < 4; ++i){
				for (int j = 0; j < 4; ++j) {
					cin >> cards[k][i][j];
				}
			}
		}
	
		int join[16] = {};
		int count = 0, val = 0;
		for (int k = 0 ; k < 2 ; ++k) {
			for (int j = 0; j < 4; ++j) {
				if (++join[ cards[k][row[k]-1][j] - 1 ] == 2){
					++count;
					val = cards[k][row[k]-1][j];
				}
			}
		}
		
		if (count == 0) {
			PRINTSolution("Volunteer cheated!");
		} else if (count == 1) {
			PRINTSolution(val);
		} else {
			PRINTSolution("Bad magician!");
		}
	}

    return 0;
}
