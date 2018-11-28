#include <bits/stdc++.h>
using namespace std;

int calc(string a, string b){
  a += "#";
  b += "#";
  int A[101], B[101];
  for(int i = 0 ; i < 101 ; i++) A[i] = B[i] = 0;
  
  int cnt1 = 0, cnt2 = 0;
  for(int i = 0 ; i < (int)a.size() ; i++){
    if(a[i] != a[i+1]){
      A[cnt1++] = cnt2;
      cnt2 = 0;
    }
    else cnt2++;
  }
  
  cnt1 = 0, cnt2 = 0;
  for(int i = 0 ; i < (int)b.size() ; i++){
    if(b[i] != b[i+1]){
      B[cnt1++] = cnt2;
      cnt2 = 0;
    }
    else cnt2++;
  }
  
  int ret = 0;
  for(int i = 0 ; i < 101 ; i++){
    ret += abs(A[i] - B[i]);
  }
  return ret;
}

int main(){
  int T;
  cin >> T;
  for(int tc = 1 ; tc <= T ; tc++){
    cout << "Case #" << tc << ": ";
    
    int N;
    cin >> N;
    
    string a, b;
    cin >> a >> b;
    string A = a, B = b;
    
    A.erase(unique(A.begin(), A.end()), A.end());    
    B.erase(unique(B.begin(), B.end()), B.end());    
    
    if(A != B){
      cout << "Fegla Won" << endl;
      continue;
    }
    
    cout << calc(a, b) << endl;
    
    
    
  }
  return 0;
}
