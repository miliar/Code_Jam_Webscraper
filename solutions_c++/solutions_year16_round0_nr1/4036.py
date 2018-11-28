#include<bits/stdc++.h>
#define ll long long
using namespace std;
int solve( int N ){
  int it = 1 , ct = 0;
  int h[10] = {0};
  while( it <= 1000 ){
      int val = N * it;
      while(val){
        if(!h[ val % 10 ]) ct++ , h[val % 10] = 1;
        val /= 10;
      }
       if(ct == 10)
       return (it * N);
       ++it;
  }
  return 0;
}
int main(){
       cin.sync_with_stdio(false);
      // ifstream cin("a.txt");
    //   ofstream cout("b.txt");
       int T;
       cin >> T;
       for(int t = 1 ; t <= T ; ++t ){
            int N;
            cin >> N;
            cout << "Case #"<<t<<": ";
            int Ans = solve(N);
             if(!Ans)
             cout << "INSOMNIA" << endl;
             else
             cout << Ans << endl;
       }
  return 0;
}
