#include<bits/stdc++.h>
#define ll long long
using namespace std;
int f(string x){
  for(int i = x.size()-1; i >= 0 ; --i){
    if(x[i]=='-')
    return i;
  }
  return -1;
}
int solve(string x){
   int val = f(x);
    if(val == -1)
    return 0;
    else {
      string y = x.substr(0,val+1);
      for(int i = 0 ; i < y.size() ; ++i ){
        if(y[i]=='-')
        y[i] = '+';
        else
        y[i] = '-';
      }
      y += x.substr(val+1);
    return 1 + solve(y);
    }
}
int main(){
       cin.sync_with_stdio(false);
    //   ifstream cin("a.txt");
   //    ofstream cout("b.txt");
       int T;
       cin >> T;
       for(int t = 1 ; t <= T ; ++t ){
        string x;
         cin >> x;
          cout << "Case #" << t <<": "<< solve(x) << endl;
       }
  return 0;
}
