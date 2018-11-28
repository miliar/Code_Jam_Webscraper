#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

int main(void) {
     ifstream IN("A-large.in");
     ofstream OUT("A-large.out");
     int num_test;
     IN>>num_test;
          
     for (int test=1; test<=num_test; test++) {
          int N, X;
          IN>>N>>X;
          
          vector <int> A(N);
          for (int i=0; i<N; i++) IN>>A[i];
          
          sort(A.begin(), A.end());
          
          int s=0;
          int e=N-1;
          int used=0;
          
          while (e>=s) {
               if (A[e]+A[s]<=X) {
                    used++;
                    e--;
                    s++;
                    }
               else {
                    used++;
                    e--;
                    }
               }
          
          
          
          OUT<<"Case #"<<test<<": "<<used<<"\n";
          }
     return 0;
     }
