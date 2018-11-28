#include<iostream>
#include<algorithm>
#include<limits.h>
using namespace std;

int _minm;

void solve(int a[],int x,int ans)
{
  if(ans+x<_minm) _minm = ans+x;
  
  if(x<=0) return ;
  
  int b[20],i,j;
  for(i=1;i<=x/2;i++) {
    for(j=1;j<x;j++) b[j] = a[j];
    b[i] += a[x];
    b[x-i] += a[x];
    solve(b,x-1,ans+a[x]);
  }
}

int main()
{
  freopen("jamQbque.txt","r",stdin);
  freopen("jamQbnew.txt","w",stdout);
  int t,count;
  cin>>t;
  for(count=1;count<=t;count++) {
    int i,j,n,m,ans=0,maxm=0,temp,a[15];
    _minm = INT_MAX;
    cin>>n;
    for(i=0;i<=10;i++) a[i]=0;
    for(i=1;i<=n;i++) {
      cin>>temp;
      a[temp]++;
    }
    for(i=9;i>=1;i--) {
      if(a[i]>0) {
        solve(a,i,0);
        break;
      }
    }
    cout<<"Case #"<<count<<": ";
    cout<<_minm<<"\n";
  }
//  system("pause");
  return 0;
}
