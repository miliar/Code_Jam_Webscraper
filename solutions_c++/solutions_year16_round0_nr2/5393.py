#include<bits/stdc++.h>
 
using namespace std;

int main(){
    int t;
    cin >> t;

    int m=1;

    while(t--){
      string s;
      cin >> s;
      cout << "Case #" << m << ": ";
      int n = s.size();

      int segment=0,i=0;
      bool check=true;
      while(i<n){
        if(s[i]=='-'){
          if(check)
            segment++;
          check = false;
        }else{
          check = true;
        }
        i++;
      }

      if(s[0]=='+')
        cout << 2*segment << "\n";
      else
        cout << 2*segment-1 << "\n";
      
      m++;
    }

    return 0;
}
