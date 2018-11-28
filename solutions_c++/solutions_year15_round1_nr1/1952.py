#include<iostream>
using namespace std;
int main(void){
  int T;
  cin>>T;
  for( int testcase = 1; testcase <= T; testcase++){
    int pcs[2000];
    int n;
    cin>>n;
    int sum = 0;
    int big = 0;
    int sum2 = 0;
    cin>>pcs[0];
    for( int i = 1; i< n; i++){
      cin>>pcs[i];
      int tmp = pcs[i-1] - pcs[i];
      if( tmp > 0 ){
        sum += pcs[i-1]-pcs[i];
        big = max( big , pcs[i-1]-pcs[i] );
      }
    }
    sum2 = big* (n-1);
    for( int i = 0; i< n-1; i++){
      if(pcs[i] < big) sum2 -= (big-pcs[i]) ;
    }
      
    cout<< "Case #" << testcase << ": " << sum <<" "<<sum2<<endl;
  }
  return 0;
}

      

      
    
