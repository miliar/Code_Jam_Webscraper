#include<iostream>
#include<algorithm>
using namespace std;

int main(){
  int t=0,T;
  cin>>T;
  while(t<T){
    int n,j;
    cin>>n;
    float p1[n],p2[n];
    for(int i=0;i<n;i++)cin>>p1[i];
    for(int i=0;i<n;i++)cin>>p2[i];
    sort(p1,p1+n); sort(p2,p2+n);
    //Deceitful
    int sum=0;j=n-1;
    for(int i=n-1;i>=0;i--){
      while(j>=0 && p1[i]<p2[j])j--;
      if(j>=0){
        sum++;
        j--;
      }
      else break;
    }    
    cout<<"Case #"<<t+1<<": "<<sum<<" ";
    //War
    sum=0;j=n-1;
    for(int i=n-1;i>=0;i--){
      while(j>=0 && p2[i]<p1[j])j--;
      if(j>=0){
        sum++;
        j--;
      }
      else break;
    }
    cout<<n-sum<<endl;
    t++;
  }
  return 0;
}
