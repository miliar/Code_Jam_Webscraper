#include<iostream>
#include<algorithm>

using namespace std;

double a[1100],b[1100];

int main(){
  int j1,j2,pos,a1,b1,ans1,ans2,i,n,t,ct=1;
  cin>>t;
  while(t--){
    cin>>n;
    for(i=0;i<n;i++){
      cin>>a[i];
    }
    sort(a,a+n);
    for(i=0;i<n;i++){
      cin>>b[i];
    }
    sort(b,b+n);
    ans1 = 0; ans2 = 0;
    j1 = n-1; j2 = 0;
    for(i=n-1;i>=0;i--){
      if(a[i] > b[j1]){
	j2++; ans2++;
      }
      else{
	j1--;
      }
    }
    pos = lower_bound(a,a+n,b[0]) - a;
    j1 = n-1; j2 = pos;
    for(i=0;i<n && (j1 >= j2);i++){
      if(a[j2] > b[i]){
	ans1++; j2++;
      }
      else{
	j2++; i--;
      }
    }
    cout<<"Case #"<<ct<<": "<<ans1<<" "<<ans2<<endl;
    ct++;
  }
  return 0;
}