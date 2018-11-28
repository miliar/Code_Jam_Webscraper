#include<iostream>

#include<string>
#include<algorithm>
#include<vector>

using namespace std;
int Dy[2][1000000010];
//     123456789

int main(){
   int n;
   int i;
   cin >> n;
   for(i=0;i<=1000000000;i++) Dy[0][i] = Dy[1][i] = 0;
   for(int t=1;t<=n;t++){
      vector<int> coins;
      int C, D, V;
      cin >> C >> D >> V;
      for(i=1;i<=D;i++){
         int tmp;
         cin >> tmp;
         coins.push_back(tmp);
      }
      coins.push_back(0x7fffffff); // dummy for boundary.
      std::sort(coins.begin()+1, coins.begin()+1+D);
      // cout << "sort done.\n";
      // for(i=0;i<coins.size();i++){
      //    cout << coins[i] << " ";
      // }
      // cout << "\n";
      int j, k;
      int done_v = 0;
      int cur=1, prev=0;
      int result = 0;
      Dy[cur][0] = Dy[prev][0] = t;
      if(coins[0] != 1){
         // cout << "we need coin val 1\n";
         result ++;
         coins.insert(coins.begin(), 1);
      }
      int loop_done = 0;
      for(k=0;k<=D;k++){
         // cout << "do with coin: " << coins[k] << '\n';
         for(i=0;i<=V;i++){
            for(j=1;j<=C;j++){
               if( i - coins[k] * j < 0 )
                  continue;
               if(Dy[prev][i - coins[k] * j] == t){
                  Dy[cur][i] = t;
               }
            }
            if(Dy[prev][i] == t)
               Dy[cur][i] = t;
         }
         // for(i=1;i<=V;i++){
         //    if(Dy[cur][i] == t){
         //       cout << "1 ";
         //    }
         //    else
         //       cout << "0 ";
         // }
         // cout << '\n';
         while(done_v < coins[k+1] && done_v <= V){
            if(Dy[cur][done_v] == t){
               done_v += 1;
               if(done_v > V){
                  loop_done = 1;
                  break;
               }
               continue;
            }
            else{
               // cout << "let's make new coin!! val: " << done_v << "\n";
               result ++;
               coins.insert(coins.begin()+k+1, done_v);
               D += 1;
               break;
            }
         }
         if(loop_done)
            break;
         int tmp;
         tmp = cur;
         cur = prev;
         prev = tmp;
      }
      // cout << "done_v: " << done_v << "\n";
      cout << "Case #" << t << ": ";
      cout << result;
      cout << "\n";
   }

   return 0;
}
