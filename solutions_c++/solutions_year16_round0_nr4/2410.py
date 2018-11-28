#include <bits/stdc++.h>

#define verbose 0
#define inf 1e9;
using namespace std;

void write(int n, vector<int> ans){
   ofstream ofs;
   ofs.open ("out.txt", ios_base::app);
   // ofs << fixed << setprecision(6);
   ofs << "Case #" << n << ":";
   for (int i: ans){
       ofs << " " << i;
   }
   ofs << endl;
   ofs.close();
}
vector<int> solve(int K, int C, int S){
    vector<int> ret(S);
    for (int i = 1; i <= S; i++){
        ret[i-1] = i;
    }
    return ret;
}

int main(void){
   remove("out.txt");
   int T; cin >> T;
   for (int i = 0; i < T; i++){
       int K, C, S;
       cin >> K >> C >> S;
       write(i+1, solve(K, C, S));
   }
   return 0;
}
