#include <iostream>
#include <string>
#include <vector>
using namespace std;
int cas, T, N;
int arr[32];

int sol() {
  int maxx=0;
  for (int i=0; i<N; ++i)
    if (maxx<arr[i]) maxx=arr[i];
  if (maxx==0) return 0;

  vector<int> ids;
  for (int i=0; i<N; ++i)
    if (maxx==arr[i])
      ids.push_back(i);

  if (ids.size()%2==1) {
    cout<<' '<<(char)('A'+ids[0]);
    --arr[ids[0]];
  }
  else {
    cout<<' '<<(char)('A'+ids[0])<<(char)('A'+ids[1]);
    --arr[ids[0]];
    --arr[ids[1]];
  }
  return 1;
}

int main() {
  cin>>T;

  for (cas=1; cas<=T; ++cas) {
    cin>>N;
    for (int i=0; i<N; ++i) cin>>arr[i];
    cout<<"Case #"<<cas<<":";
    while (sol());
    cout<<endl;
  }

  return 0;
}
