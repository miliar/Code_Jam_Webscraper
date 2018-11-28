#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

pair <double, double> temperature(vector <pair<double, double> > & A, int s, int e) {
     double V=0.0;
     double total_T=0.0;
     for (int i=s; i<=e; i++) {
          V += A[i].second;
          total_T += A[i].second * A[i].first;
     }
     return make_pair(total_T/V, V);
}

pair <double, double> sum_temp(pair<double, double> A, pair<double, double> B, double X) {
     A.first *= A.second;
     A.first += B.first*B.second*X;
     A.second += B.second*X;
     A.first /= A.second;
     return A;
}

double abs(double X) {
     return max(X, -X);
}

int main(void) {
     int num_test;
     cin>>num_test;
     
     cout.precision(9);
     
     for (int test=1; test<=num_test; test++) {
          int N;
          double V, T;
          cin >> N >> V >> T;
          
          vector <pair<double, double> > A(N);
          for (int i=0; i<N; i++) cin >> A[i].second >> A[i].first;
          
          sort(A.begin(), A.end());
          int s=0, e=N-1;
          
          bool DOABLE = (A[s].first <= T) && (A[e].first >= T);
          
          pair<double,double> CURR = temperature(A, s, e);
          
          bool F=true;
          while (DOABLE && F && e>s) {
               F=false;
               
               if (temperature(A, s, e).first > T && temperature(A, s, e-1).first > T) {
                    F=true;
                    e--;
               }
               else if (temperature(A, s, e).first < T && temperature(A, s+1, e).first < T) {
                    F=true;
                    s++;
               }
          }
          
          int m=s;
          double Q=0.0;
          if (!DOABLE || (s==e)) {
               if (s==e) {
                    if (abs(A[s].first-T)>1e-7) DOABLE=false;
               }
          }
          else if ( abs(temperature(A, s, e).first-T) < 1e-12) {
               cerr<<"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n";
          }
          else {
               bool LOW=true;
               if (temperature(A, s, e).first > T) {
                    LOW=false;
                    m=e;
                    e--;
               }
               else {
                    m=s;
                    s++;
               }
               
               pair <double, double> S = temperature(A, s, e);
               double min=0.0, max=1.0;
               while (min+1e-12 < max) {
                    Q = (min + max)/2.0;
                    pair <double, double> K = sum_temp(S, A[m], Q);
                    
                    if ((K.first > T) ^ LOW) max=Q;
                    else min=Q;
               }
          }
          
          if (DOABLE) {
               pair <double, double> W = sum_temp(temperature(A, s, e), A[m], Q);
               cerr<<s<<"\t"<<e<<"\t"<<W.first<<"\t"<<W.second<<"\t"<<T<<"\n";
               assert (W.second > 1e-12);
               cout<<"Case #"<<test<<": "<< V/W.second <<"\n";
          }
          else cout<<"Case #"<<test<<": "<< "IMPOSSIBLE" <<"\n";
          }
     return 0;
     }
