#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <stack>
#include <algorithm>
#include <cctype>
#include <vector>
#include <queue>
#include <tr1/unordered_map>
#include <cmath>
#include <map>
#include <bitset>
#include <set>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector< ii > vii;
///////////////////////////////UTIL/////////////////////////////////
#define ALL(x) (x).begin(),x.end()
#define CLEAR0(v) memset(v, 0, sizeof(v))
#define CLEAR(v, x) memset(v, x, sizeof(v))
#define IN0(x, n) ((x) > -1 && (x) < n)
#define IN(x, a, b) ((x) >= a && (x) <= b)
#define COPY(a, b) memcpy(a, b, sizeof(a))
#define CMP(a, b) memcmp(a, b, sizeof(a))
#define REP(i,n) for(int i = 0; i<n; i++)
#define REPP(i,a,n) for(int i = a; i<n; i++)
#define REPD(i,n) for(int i = n-1; i>-1; i--)
#define REPDP(i,a,n) for(int i = n-1; i>=a; i--)
#define pb push_back
#define pf push_front
#define sz size()
#define mp make_pair
/////////////////////////////NUMERICAL//////////////////////////////
#define INCMOD(a,b,c) (((a)+b)%c)
#define DECMOD(a,b,c) (((a)+c-b)%c)
#define ROUNDINT(a) (int)((double)(a) + 0.5)
#define INF 0x3f3f3f3f
#define EPS 1e-9
/////////////////////////////BITWISE////////////////////////////////
#define CHECK(S, j) (S & (1 << j))
#define CHECKFIRST(S) (S & (-S))  //PRECISA DE UMA TABELA PARA TRANSFORMAR EM INDICE
#define SET(S, j) S |= (1 << j)
#define SETALL(S, j) S = (1 << j)-1  //J PRIMEIROS
#define UNSET(S, j) S &= ~(1 << j)
#define TOOGLE(S, j) S ^= (1 << j)
///////////////////////////////64 BITS//////////////////////////////
#define LCHECK(S, j) (S & (1ULL << j))
#define LSET(S, j) S |= (1ULL << j)
#define LSETALL(S, j) S = (1ULL << j)-1ULL  //J PRIMEIROS
#define LUNSET(S, j) S &= ~(1ULL << j)
#define LTOOGLE(S, j) S ^= (1ULL << j)
//__builtin_popcount(m)
//scanf(" %d ", &t);

int t;
int n;

int main(){
	cin >> t;
	REP(ca, t){
		cin >> n;
		vector< double > na(n);
		vector< double > ke(n), KE;
		REP(i, n) cin >> na[i];
		REP(i, n) cin >> ke[i];
		sort(na.begin(), na.end());
		sort(ke.begin(), ke.end());
		
		int war = 0, dwar = 0;
		
		//REP(i, n) cout << na[i] << " ";
		//cout << endl;
		//REP(i, n) cout << ke[i] << " ";
		//cout << endl;
		
		
		KE = ke;
		int l = 0, r = n-1;
		double x;
		REPD(i, n){
			x = na[i];
			
			vector<double>::iterator it;
			it = lower_bound(KE.begin(), KE.end(), x);
			if(it == KE.end()){
				KE.erase(KE.begin());
				war++;
			}
			else{
				KE.erase(it);
			}
		}
		
		REP(i, n){
			x = ke[i];
			vector<double>::iterator it;
			it = lower_bound(na.begin(), na.end(), x);
			if(it == na.end()){
				na.erase(na.begin());
			}
			else{
				dwar++;
				na.erase(it);
			}
		}
		
		printf("Case #%d: %d %d\n", ca+1, dwar, war);
	
	}
}
