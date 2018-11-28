#include<iostream>
using namespace std;

int ispalindrome(long long x);
int main(){

  int t,n,i,cnt = 0;
  long long st,end;
  cin>>t;
  n = t;
  while(t--){
  
    cin>>st;
    cin>>end;
    for(i=1;i*i<=end;i++){
    
      if(ispalindrome(i) && i*i>=st){
      
        if(ispalindrome(i*i))
          cnt++;
      }
    }
   cout<<"Case #"<<n-t<<": "<<cnt<<endl;
   cnt = 0;
  }
}
int ispalindrome(long long x){

  long long tmp = 0,r = 0,i=0,sum=0;

  tmp = x;
  while(x!=0){
  
    r = x%10;
    sum = sum*10+r;
    x = x/10;

  }
  if(tmp == sum)
    return 1;
  else
    return 0;
}
