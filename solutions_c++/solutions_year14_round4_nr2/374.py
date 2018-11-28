#include <iostream>
#include <algorithm>

using namespace std;

long long A[1000];

int main () {
  int T,N;
  
  cin >> T;
  for (int t=1; t<=T; t++) {
    cin >> N;
    for (int i=0; i<N; i++)
      cin >> A[i]; 
    int low=0, high=N-1,swaps=0;
    while (low<high) {
      int i=low;
      for (int j=low+1; j<=high; j++)
	if (A[j]<A[i]) i=j;
      long long x=A[i];
      if (i-low < high-i) { // move to low
	for (int j=i-1; j>=low; j--) A[j+1]=A[j];
	A[low]=x;
	swaps += i-low;
	low ++;
      } else { // move to high
	for (int j=i+1; j<=high; j++) A[j-1]=A[j];
	A[high]=x;
	swaps += high-i;
	high --;
      }
    };
    cout << "Case #" << t << ": " << swaps << endl;
    

    /*
    for (int i=0; i<N; i++)
      cout << A[i] << " "; 
    cout << endl;
    */
    /*
    for (int i=0; i<N; i++)
      cout << A[i] << " "; 
    cout << endl;
    */
  };
};
