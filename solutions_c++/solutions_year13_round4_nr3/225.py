#include<iostream>
#include<algorithm>

using namespace std;

int N;
int A[2000];
int B[2000];
int a[2000];
int dp[22];

bool f(int x,int u){
  if(x!=N){
    for(int i=0;i<N;i++){
      if(!(u>>i&1)){
	dp[x]=1;
	for(int k=0;k<x;k++){
	  if(a[k]<i&&dp[k]+1>dp[x]){
	    dp[x]=dp[k]+1;
	  }
	}
	if(dp[x]==A[x]){
	  a[x]=i;
	  if(f(x+1,u|1<<i))return true;
	}
      }
    }
    return false;
  }else{
    int dc[22];
    for(int i=N-1;i>=0;i--){
      dc[i]=1;
      for(int j=i+1;j<N;j++){
	if(a[i]>a[j]&&dc[i]<dc[j]+1){
	  dc[i]=dc[j]+1;
	}
      }
    }
    return equal(dc,dc+N,B);
  }
}
    
int main(){
  int T;
  cin>>T;
  for(int i=1;i<=T;i++){
    cin>>N;
    for(int j=0;j<N;j++){
      cin>>A[j];
    }
    for(int j=0;j<N;j++){
      cin>>B[j];
    }
    f(0,0);
    cout<<"Case #"<<i<<":";
    for(int j=0;j<N;j++){
      cout<<' '<<a[j]+1;
    }
    cout<<endl;
  }
  return 0;
}
