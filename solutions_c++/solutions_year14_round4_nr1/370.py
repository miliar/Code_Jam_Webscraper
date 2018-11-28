#include <iostream>
#include <algorithm>

using namespace std;

long long S[10000];

int main () {
  int T,N,X;
  
  cin >> T;
  for (int t=1; t<=T; t++) {
    cin >> N >> X;
    for (int i=0; i<N; i++)
      cin >> S[i]; 
    
    sort(S,S+N);

    int disks=0;
    int low=0, high=N-1;
    while (low<=high) {
      if (low<high && S[low]+S[high]<=X) low++;
      high--, disks++;
    };

    cout << "Case #" << t << ": " << disks << endl;
  };
};
