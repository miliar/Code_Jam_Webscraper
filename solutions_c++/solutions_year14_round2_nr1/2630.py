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
     int N;
     bool perdeu=false;
     cin >> N;
     string bla;
     string ref="";
     int M[N][100];
     int soma[100];
     memset (M, 0, sizeof(M[0][0])*100*N);
     memset (soma, 0, sizeof(soma[0])*100);
     FOR (i, 0, N-1)
     {
         cin >> bla;
         if(perdeu) continue;
         int k=0;
         FOR(j, 0, bla.length()-1){
                if(j>0 && bla[j]!=bla[j-1]) k++;
                M[i][k]++;
                soma[k]++;
                if(i==0 && M[i][k]==1) {
                         ref += bla[j];
                         }
                else {
                    if(ref.length()<=k || ref[k]!=bla[j]){
                                       perdeu=true;  
                                         }    
                              
                              }
                }
         //out<<ref<<endl;
         //cout<<bla<<endl;
         }    
          int moves=0; 
         if (!perdeu) {     
              
              FOR (j, 0, ref.length()-1){
                  int media = (int) (((1.0*soma[j])/(1.0*N))+0.5);
                  //cout<<media<<" ";
              FOR (i, 0, N-1) {
                  if(M[i][j]==0) perdeu=true;
                  if(M[i][j]>media)
                  moves+=M[i][j]-media;
                  else
                  moves+=media-M[i][j];
                  
                  //cout<<M[i][j]<<" "<<moves<<" ";
              }
              //cout<<endl;
              }
              } 
              if(perdeu) cout<<"Fegla Won"; 
              else              cout<<moves;
              
              
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
