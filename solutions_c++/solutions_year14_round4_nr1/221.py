#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

const int MAX_N = 10030;
typedef pair<int,int> pii;

/*
  int do_case(){
  int n,X,A[MAX_N];
  cin >> n >> X;
  multiset<pii> S;
  for(int i=0;i<n;i++) cin >> A[i];
  sort(A,A+n);
  for(int i=0;i<n;i++) S.insert(A[i]);

  bool used[MAX_N] = {0};
  
  for(int i=0;i<n;i++){
    if(used[i]) continue;
    
  }
  }*/

int do_case(){
  int n,X,A[MAX_N];
  cin >> n >> X;
  
  for(int i=0;i<n;i++) cin >> A[i];
  sort(A,A+n);

  bool used[MAX_N] = {0};

  int ctr = n;
  for(int i=0;i<n;i++){
    if(used[i]) continue;
    for(int j=n-1;j>i;j--)
      if(!used[j] && A[i]+A[j] <= X){
	ctr--;
	used[j] = true;
	break;
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
