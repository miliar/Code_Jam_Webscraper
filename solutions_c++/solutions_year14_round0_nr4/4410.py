#include<cstdio>
#include<iostream>
#include<iomanip>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<map>
#include<set>
#include<bitset>
#include<algorithm>
#include<cassert>
#include<ctime>
#include<queue>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)n; i++)
#define FOR(i,n,m) for(int i = (int)n; i <= (int)m; i++)
#define FOD(i,n,m) for(int i = (int)n; i >= (int)m; i--)
#define EACH(i,v) for(__typeof((v).begin()) i = (v).begin(); i != (v).end(); i++)

typedef long long i64;
typedef pair<int, int> PI;
typedef pair<double, char> PDC;

#define sz(v) ((i64)(v).size())
#define all(v) (v).begin(),(v).end()
#define bit(n) (1LL<<(i64)(n))

#define PB push_back
#define MP make_pair
#define X first
#define Y second
template<class T> void fmax(T &a, const T &b) { if (a < b) a = b; }
template<class T> void fmin(T &a, const T &b) { if (a > b) a = b; }
template<class T> T sqr(const T &a) { return a * a; }

bool myfunction (PDC a, PDC b) { return (a.X>b.X); }

void doit() {
     int N;
     double peso;
     vector< PDC > V;
     cin >> N;

     int pontosWN = 0;
     int pontosWK = 0;
     int pontosDWN = 0;
     int pontosDWK = 0;
     
     FOR(i,0,N-1) {
                  cin >> peso;
                  V.PB(MP(peso,'N'));
     }
     FOR(i,0,N-1) {
                  cin >> peso;
                  V.PB(MP(peso,'K'));
     }
     sort (V.begin(), V.end(), myfunction);
     
     for(std::vector<int>::size_type i = 0; i != V.size(); i++) {                 
         if (V[i].Y=='N') {
              pontosDWN++;
              if(pontosWK ==0) pontosWN++;
              else pontosWK--;
         }
         
         if (V[i].Y=='K') {
              if(pontosDWN==0) pontosDWK++;
              else pontosDWN--;
              pontosWK++;
         }
     }
     
     cout << N-pontosDWK << " " << pontosWN;
}

int main() {
    freopen("D-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	int Te;
	scanf("%d", &Te);
	for (int Ti = 1; Ti <= Te; Ti++) {        		
		printf("Case #%d: ", Ti);
		doit();
		printf("\n", Ti);
	}
}
