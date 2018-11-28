#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_N = 1000;
int A[MAX_N];

int do_case(){
  int n;
  cin >> n;
  for(int i=0;i<n;i++)
    cin >> A[i];

  int ctr = 0;
  int mini = 0,maxi = n;
  while(mini < maxi){
    int m = min_element(A+mini,A+maxi) - A;
    // Left? Right?
    int l = m-mini, r = maxi-1-m;
    if(l < r){
      ctr += l;
      for(int i=m;i>mini;i--) A[i] = A[i-1];
      mini++;
    } else {
      ctr += r;
      for(int i=m;i<maxi-1;i++) A[i] = A[i+1];
      maxi--;
    }
  }
    

  return ctr;
}

int main(){
  int T,C=1;
  cin >> T;
  while(T--)
    cout << "Case #" << C++ << ": " << do_case() << endl;
  return 0;
}
