#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
  int zz,zzz;
  cin>>zzz;
  for(zz=1;zz<=zzz;zz++) {
    int n;
    int a[2000];
    cin>>n;
    for(int i=0;i<n;i++)
      cin>>a[i];
    printf("Case #%d: ",zz);
    int c=0;
    int b=0;
    for(int i=0;i<n-1;i++) {
      if(a[i+1]<a[i])
        c+=a[i]-a[i+1];
      b=max(b,a[i]-a[i+1]);
    }
    printf("%d ",c);
    c=0;
    for(int i=0;i<n-1;i++) {
      if(a[i]-b<0)
        c+=a[i];
      else
        c+=b;
    }
    cout<<c;
    cout<<"\n";
  }
  return 0;
}
