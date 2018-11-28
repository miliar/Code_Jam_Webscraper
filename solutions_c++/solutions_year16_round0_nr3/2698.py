// Brute force.
// try all at most length 16 binary strings. 
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cassert>
using namespace std;

bool prime(long long z, long long &factor) {
  long long x=2;
  while (x*x <=z) {
    if ((z%x) == 0) {
      factor =x;
      return false;
    }
    x++;
  }
  factor=-1;
  return true;
}

long long base_k(vector<int> &bits, int base) {
  
  long long sum=0;
  for (int i=0;i<bits.size();i++) {
    sum=(sum*base) + bits[i];
  }
  return sum;
}
  

void gen_J_cases(int N, int J) {
  vector<int> bits;
  bits.resize(N);
  bits[0]=1;
  bits[N-1]=1;
  int C=0;
  int max_d = 1<<(N-2);
  for (int i=0;i<max_d;i++) {
    for (int j=0;j<N-2;j++) {
      if ((i&(1<<j))>0) {
	bits[j+1]=1;
      } else {
	bits[j+1]=0;
      }
    }
    //for (int i=0;i<bits.size();i++) {
    //  cout << bits[i];
    //}
    //cout << endl;

    long long t;
    bool found = true;
    vector<long long> factors;
    factors.resize(11);
    for (int k=2;k<=10;k++) {
      long long t;
      t = base_k(bits,k);
      //cout << t << " " << k << endl;

      long long l=0;
      if (prime(t,l)) {
	found=false;
	//break;
      } else {
	assert((t%l)==0);
	factors[k] = l;
      }
    }
    if (found) {
      //for (int k=2;k<=10;k++) {
      //t = base_k(bits,k);
      //cout << t << " " << k << endl;
      //assert((t%factors[k])==0);
      //}
 
  
      for (int z=0;z<bits.size();z++) {
	cout << bits[z];
      }
      for (int k=2;k<=10;k++) {
	cout << " " << factors[k];
      }
      cout << endl;
      C++;
      if (C==J) return;
    }
  }

}


int main() {

  int I;
  cin >> I;
  for (int i=1;i<=I;i++) {
    int N;
    int J;
    cin >> N;
    cin >> J;
    cout << "Case #"<<i<<":"<<endl;
    gen_J_cases(N,J);
  }
}
