#include <iostream>
using namespace std;

int main() {
  int cas, T, N, num, n;
  int arr[3000];

  cin>>T;
  for (cas=1; cas<=T; ++cas) {
    cin>>N; num=(2*N-1)*N;
    for (int i=0; i<3000; ++i) arr[i]=0;
    for (int i=0; i<num; ++i) {
      cin>>n; arr[n]+=1;
    }
    cout<<"Case #"<<cas<<":";
    for (int i=0; i<3000; ++i)
      if (arr[i]%2)
        cout<<" "<<i;
    cout<<endl;
  }
  return 0;
}
