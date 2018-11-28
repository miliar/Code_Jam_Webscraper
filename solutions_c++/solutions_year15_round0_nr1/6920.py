#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int T;
int Smax;
int S[1001];

int main () {
  cin >> T;
  for(int t=1;t<=T;t++) {
    cin >> Smax;
    for (int i=0;i<=Smax;i++){
      scanf("%1d",&S[i]);
    }

    int count=S[0];
    int need=0;
    for(int i=1;i<=Smax;i++){
      if (count < i) {
        need=need+(i-count);
        count=count+(i-count);
      }
      count=count+S[i];
    }
    cout << "Case #" << t << ": " << need << endl;
  }
}

