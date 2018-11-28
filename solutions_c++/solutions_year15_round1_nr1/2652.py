#include<iostream>
#include <string>
#include<climits>
using namespace std;

int main(){
  
  int T;
  cin >> T;
  
  for(int q=1;q<=T;q++){
    
    int N;
    cin >> N;
    
    int m[N] ;
    
    int ans1=0,ans2=0;
    int eaten=0,mineaten=INT_MAX;
    int b=0;
    for(int j=0;j <N; j++){
      cin>> m[j];
    }
    
    for(int j=1;j <N; j++){
      if(m[j]<m[j-1]){ans1+=(m[j-1]-m[j]);}
    }
    
    for(int k1=0;k1<=10000;k1++){
      double k=((double)k1/10);
      eaten=0;
      for(int j=0;j<N-1;j++){
	if(k*10<=m[j]){
	  eaten+=(k*10);
	  int temp=m[j]-(k*10);
	  //if(j==N-1){
	  //  if(temp>m[j+1]){eaten=INT_MAX;break;}
	  //}
	  if(temp>m[j+1]){eaten=INT_MAX;break;}
	}
	else{
	  int temp=m[j]-(k*10);
	  eaten+=m[j];
	  //if(m[j]%k!=0){eaten=INT_MAX;break;}
	}
      }
      if(eaten<mineaten){
	mineaten=eaten;
	b=k;
      }
    }
    //cout<<b<<endl;
    cout << "Case #" << q << ": "<<ans1<<" "<<mineaten<<endl;
  }
  
  return 0;
}