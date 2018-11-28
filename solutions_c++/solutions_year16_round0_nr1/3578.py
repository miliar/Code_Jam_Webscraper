#include <vector>
#include <string>
#include <iostream>
using namespace std;

int doit(int n) {
  if(n==0) return -1;
  int arr[10];
  memset(arr,0,sizeof(arr));
  int have=0,cur=n;
  for(int i=0;i<100;i++) {
    int tmp=cur;
    while(tmp) {
      int digit=tmp%10;
      if(arr[digit]==0) arr[digit]=1,have++;
      tmp/=10;
    }
    if(have==10) return cur;
    cur=cur+n;
  }
  return -1;
}   

int main() {
  int tests;
  cin>>tests;
  for(int i=0;i<tests;i++) {
    int n;
    cin>>n;
    int ret=doit(n);
    if(ret>=0)
      cout<<"Case #"<<(i+1)<<": "<<ret<<endl;
    else
      cout<<"Case #"<<(i+1)<<": "<<"INSOMNIA"<<endl;
  }
  return 0;
}
