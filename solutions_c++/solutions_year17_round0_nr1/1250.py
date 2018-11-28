#include <bits/stdc++.h>
using namespace std;

void write(int n, int ans){
   ofstream ofs;
   ofs.open ("out.txt", ios_base::app);
   // ofs << fixed << setprecision(6);
   if (ans == -1){
       ofs << "Case #" << n << ": " << "IMPOSSIBLE" << endl;
   }
   else{
       ofs << "Case #" << n << ": " << ans << endl;
   }
   ofs.close();
}

bool flip(int i, string &s, int K){
    if (i + K > s.size()) return false;
    for (int pos = i; pos < i+K; pos++){
        if (s[pos] == '-') s[pos] = '+';
        else s[pos] = '-';
    }
    return true;
}

int solve(){
    string s; int K;
    cin >> s >> K;
    int cnt = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[i] == '-'){
            if (!flip(i, s, K)) return -1;
            else cnt++;
        }
    }
    return cnt;
}

int main(void){
   remove("out.txt");
   int T;
   cin >> T;
   for (int i = 1; i <= T; i++){
       write(i, solve());
   }
   return 0;
}
