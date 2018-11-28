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
          int N;
          IN>>N;
          
          vector <int> A(N);
          for (int i=0; i<N; i++) {
               IN>>A[i];
               }
          
     int RES=0;
     
     vector <pair<int,int> > B(N);
     for (int i=0; i<N; i++) B[i]=make_pair(A[i], i);
     sort(B.begin(), B.end());
     
     int remains=N;
     
     for (int i=0; i<N; i++) {
          RES+=min(B[i].second, (remains-1-B[i].second));
          for (int j=0; j<N; j++) if (B[j].second>B[i].second) B[j].second--;
          remains--;
          }
          
          
          OUT<<"Case #"<<test<<": "<<RES<<"\n";
          }
     return 0;
     }
