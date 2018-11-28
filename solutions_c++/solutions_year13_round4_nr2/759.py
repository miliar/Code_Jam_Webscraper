#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

long long last_possible(long long exp2N, long long P) {
     if (P==0) return -1;
     long long last=exp2N;
     long long pp=1;
     while (P<last) {
          pp*=2;
          last/=2;
          }
     return exp2N-pp;
     }

long long first_guaranteed(long long exp2N, long long P) {
     if (P==exp2N) return P-1;
     vector <long long> A(1, 0);
     long long B=exp2N;
     while (B>1) {
          B/=2;
          A.push_back(B);
          }
     for (int i=1; i<A.size(); i++) A[i]+=A[i-1];
     
     vector <long long> C=A;
     long long ppp=1;
     for (int i=0; i<A.size(); i++) {
          C[i]=ppp-1;
          ppp*=2;
          }
     for (int i=0; i+1<A.size(); i++) C[i]=C[i+1]-1;
     
     int counter=1;
     long long pp=0;
     ppp=1;
     for (int i=0; i<A.size(); i++) {
          if (A[i]+1<=P) pp=C[i];
//          cout<<A[i]+1<<"\t"<<P<<"\t"<<C[i]<<"\n";
          ppp*=2;
          }
/*     while (P>A[counter]) {
          cout<<A[counter]<<"\t"<<P<<"\n";
          counter++;
          pp++;
          }
*/     return ppp;
     }
/*
long long first_guaranteed(long long exp2N, long long P) {
     P=exp2N-P;
     
     
     
     
     
     if (P==exp2N) return P-1;

     long long last=exp2N;
     long long pp=2;
     vector <long long> A;
     while (last>1) {
          last/=2;
          A.push_back(last);
          }

     for (int i=1; i<A.size(); i++) A[i]+=A[i-1];
     
     while (
     
     long long position=
     
     
     
     while (P>last/2) {
          P-=last/2;
          pp*=2;
          last/=2;
          }
     return exp2N-pp;
     }
*/
int main(void) {
     ifstream IN("B2.in");
     ofstream OUT("B2.out");
     
     int num_test;
     IN>>num_test;

     for (int test=1; test<=num_test; test++) {
          int N;
          long long P;
          IN>>N>>P;

          long long exp2N=1;
          for (int i=0; i<N; i++) exp2N*=2;
          
//          OUT<<"Case #"<<test<<": "<<first_guaranteed(exp2N, P)<<" "<<last_possible(exp2N, P)<<"\n";
          OUT<<"Case #"<<test<<": "<<exp2N-2-last_possible(exp2N, exp2N-P)<<" "<<last_possible(exp2N, P)<<"\n";
 //         cout<<N<<"\t"<<P<<"\t"<<first_guaranteed(exp2N, P)<<"\n";
 //    system("pause");
          }
          
     system("pause");
     return 0;
     }
