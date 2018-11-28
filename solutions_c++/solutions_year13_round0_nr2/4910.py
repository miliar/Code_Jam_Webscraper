#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

int main(void) {
     ifstream IN("B2.in");
     ofstream OUT("B2.out");
     
     int num_test;
     IN>>num_test;
     for (int test=1; test<=num_test; test++) {
          int N, M;
          IN>>N>>M;
          vector <vector <int> > A(N, vector<int> (M));
          for (int i=0; i<N; i++) for (int j=0; j<M; j++) IN>>A[i][j];
          
          vector <int> VERT(N, 0);
          vector <int> ORIZ(M, 0);
          
          for (int i=0; i<N; i++) for (int j=0; j<M; j++) {
               VERT[i]=max(VERT[i], A[i][j]);
               ORIZ[j]=max(ORIZ[j], A[i][j]);
               }
          
          bool doable=true;
          for (int i=0; i<N; i++) for (int j=0; j<M; j++) if (VERT[i]!=A[i][j] && ORIZ[j]!=A[i][j]) doable=false;
          
          string RES="NO";
          if (doable) RES="YES";
          OUT<<"Case #"<<test<<": "<<RES<<"\n";
          }
          
     system("pause");
     return 0;
     }
