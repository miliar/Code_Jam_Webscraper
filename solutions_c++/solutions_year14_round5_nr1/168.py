#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

long long best_value(vector <long long> S) {
     long long R=0;
     for (int i=0; i<S.size(); i++) R=max(R, S[i]);
     return R;
     }

int main(void) {
     ifstream IN("A-large.in");
     ofstream OUT("A-large.out");
     int num_test;
     IN>>num_test;
          
     for (int test=1; test<=num_test; test++) {
          long long N, p, q, r, c;
          IN>>N>>p>>q>>r>>c;
          
          vector <long long> A(N);
          for (long long i=0; i<N; i++) A[i]=(i*p+q)%r+c;
          
          A.push_back(0);
          
          long long SUM=0;
          for (int i=0; i<N; i++) SUM+=A[i];

          int s=0, e=0;
          vector <long long> S(3, 0);
          S[0]=0;
          S[1]=0;
          S[2]=SUM;
          
          long long BEST=0;
          
          while (e<N) {
               BEST=max(BEST, SUM-best_value(S));
               
               S[1]+=A[e];
               S[2]-=A[e];
               e++;
               
               while (s<e && max(S[0]+A[s],S[1]-A[s])<=max(S[0], S[1])) {
                    S[0]+=A[s];
                    S[1]-=A[s];
                    s++;
                    }
               }

          BEST=max(BEST, SUM-best_value(S));


          OUT.precision(12);
          OUT<<"Case #"<<test<<": "<<(double)BEST/(double)SUM<<"\n";
          }
     return 0;
     }
