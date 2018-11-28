#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<list>

using namespace std;

int main(){
  freopen("in","r",stdin);
  freopen("out","w",stdout);
  int T;
  cin>>T;

  for(int t=1; t<=T; t++){
    printf("Case #%d: ",t);
    int smax;
    cin>>smax;
    int ar[smax+1];
    
    string input;
    cin>>input;
    
    int result = 0;
    int person = 0;
    int k = 0;
    
    for(int i=0; i <= smax; i++){
      int ip = input[i] - 48;
      ar[i] = ip;
    }
    if(ar[0]==0){
      result++;
      person++;
      ar[0] = 1;
    }else{
      result += ar[0];  
    }
cerr<<"Case #"<<t<<": "<<endl;
    for(int shy = 1; shy <= smax; shy++){
      cerr<<"Iteration "<<shy<<" res = "<<result<<endl;
      if((shy > result) && (ar[shy] != 0)){
        //find least shy
        cerr<<"Finding Least"<<endl;
        int least = shy;
        
        for(int j = shy; j >= 0; j--){
          if(ar[j] == 0){
            if(j < least) least = j;
          }
        }
        cerr<<"least = "<<least<<endl;
        int diff = shy - result;
        cerr<<"diff = "<<result<<endl;
        ar[least] = diff;
        cerr<<"ar[least] = "<<ar[least]<<endl;
        result += diff;
        person += diff;
        cerr<<"new res = "<<result<<endl;
        result += ar[shy];
      }else{
        result += ar[shy];
        cerr<<"Else part res = "<<result<<endl;
      }
    }
    cout<<person<<endl;
  }

return 0;
}
