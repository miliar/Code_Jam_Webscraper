#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

int main(void) {
     ifstream IN("B-large.in");
     ofstream OUT("B-large.out");
     int num_test;
     IN>>num_test;

     for (int test=1; test<=num_test; test++) {
          int P,Q,N;
          IN>>P>>Q>>N;
          
          vector <int> G(N), H(N);
          for (int i=0; i<N; i++) IN>>H[i]>>G[i];
          
          vector <int> pre(201, 100000);
          for (int i=0; i<201; i++) {
               pre[i]=min(pre[i], (i+P-1)/P);
               for (int j=0; j<=i; j+=P) {
                    if ((i-j)%(P+Q)>Q || (i-j)%(P+Q)==0) pre[i]=min(pre[i], j/P);
                    }
               }

          vector <int> vantage(201, -1);
          for (int i=0; i<201; i++) {
               for (int j=0; j<i; j+=Q) {
                    if ((i-j)%(P+Q)>Q || (i-j)%(P+Q)==0) vantage[i]=max(vantage[i], j/Q);
                    }
               }
          
          vector <vector <int> > DP(N+2, vector <int> (1001, 0) );
          
          for (int j=N-1; j>=0; j--) for (int v=0; v<=1000; v++) {
               DP[j][v]=max(DP[j][v], DP[j+1][min(1000, v+(H[j]+Q-1)/Q)]);
               if (vantage[H[j]]>=0) DP[j][v]=max(DP[j][v], G[j]+DP[j+1][min(1000, v+vantage[H[j]])]);
               if (pre[H[j]]<=v) DP[j][v]=max(DP[j][v], G[j]+DP[j+1][v-pre[H[j]]]);
               }
          
          OUT<<"Case #"<<test<<": "<<DP[0][1]<<"\n";
          }
     return 0;
     }
