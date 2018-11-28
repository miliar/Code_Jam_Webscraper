#include<bits/stdc++.h>
 
using namespace std;

int main(){
    int t;
    cin >> t;

    int m=1;

    while(t--){
      cout << "Case #" << m << ": ";
      long long int k,c,s;
      cin >> k >> c >> s;

      if(s>=k-1){
        if(k==1){
          cout << 1 << "\n";
        }else if(c==1){
          if(s==k){
            for(int i=1;i<=k;i++)
              cout << i << " ";
            cout << "\n";
          }else{
            cout << "IMPOSSIBLE\n";    
          }
        }else{
          for(int i=2;i<=k;i++)
            cout << i << " ";
          cout << "\n";
        }
      }else{
        cout << "IMPOSSIBLE\n";
      }
      m++;
    }

    return 0;
}
