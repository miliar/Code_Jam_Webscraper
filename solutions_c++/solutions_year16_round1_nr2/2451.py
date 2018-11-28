#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int main()
{
int a[100],b[2501],n,t,i,j,k,num,vis;
cin>>t;
for(i=0;i<t;i++)
{   vis=0;
    memset(b,0,sizeof(b));
    cin>>n;
  for(j=0;j<2*n-1;j++){
    for(k=0;k<n;k++){
        cin>>num;
        if(b[num]==0){a[vis]=num; vis++;}
        ++b[num];
        }
  }
  sort(a,a+vis);
  cout<<"Case #"<<i+1<<": ";
  for(j=0;j<vis;j++){
    if(b[a[j]]%2!=0)cout<<a[j]<<" ";
  }
  if(i!=t-1)cout<<endl;
}

return 0;
}
