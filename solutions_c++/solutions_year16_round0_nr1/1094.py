#include <iostream>
using namespace std;

int main() {
  int cas, T, N, res;
  int arr[10], tmp, i;

  cin>>T;
  for (cas=1; cas<=T; ++cas) {
    cin>>N;
    cout<<"Case #"<<cas<<": ";
    if (N==0) {
      cout<<"INSOMNIA\n";
    }
    else {
      for (i=0; i<10; ++i) arr[i]=0;
      res = N;
      while (1) {
        tmp = res;
        while (tmp) {arr[tmp%10]=1; tmp/=10;}
        for (i=0; i<10; ++i) if (arr[i]==0) break;
        if (i==10) break;
        res+=N;
      }
      cout<<res<<endl;
    }
  }

  return 0;
}
