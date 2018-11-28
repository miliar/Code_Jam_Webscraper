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


void doit() {
     int row=1;
     int num[16];
     int v;
     int resp=0;
     cin >> row;
     FOR(i, 1, 16) {
            cin >> v;
            num[v]= (i>(row*4-4) && i<=(row*4)) ? 1 : 0;
            }
     cin >> row;            
     FOR(i, 1, 16) {
            cin >> v;
            num[v]+= (i>(row*4-4) && i<=(row*4)) ? 1 : 0;
            if (num[v] == 2) {
                if (resp>0) resp=100;
                else resp = v;
                }
            }
     if (resp==0) {
	 cout << "Volunteer cheated!";                  }
     else if (resp==100) {                      
     cout << "Bad magician!";            
          }
     else {
	 cout << resp;
                  }
}

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	int Te;
	scanf("%d", &Te);
	for (int Ti = 1; Ti <= Te; Ti++) {        		
		printf("Case #%d: ", Ti);
		doit();
		printf("\n", Ti);
	}
}
