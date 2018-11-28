#include<iostream>
#include<algorithm>

using namespace std;

int main() {
  int t; cin >> t;
  for (int i=0; i<t;i++) {
    int ans1=0, ans2=0;
    int rate=0;
    int n; cin >> n;
    int *arr = new int[n];
    for (int j=0; j<n; j++) {
      cin >> arr[j];
    }
    for (int b=1; b<n; b++) {
      if (arr[b-1]-arr[b] > rate) {
	rate = arr[b-1] - arr[b];
      }
    }
    for (int b=0; b<n-1; b++) {
      ans2 += min(rate,arr[b]);
    }
    for (int a=1; a<n; a++) {
      if (arr[a] < arr[a-1])
	ans1 += (arr[a-1]-arr[a]);
    }

    cout << "Case #" << i+1 << ": " << ans1 << " " << ans2 << endl;
    delete [] arr;
  }
  
  return 0;
}
