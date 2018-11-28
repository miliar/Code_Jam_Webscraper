#include <bits/stdc++.h>

#define verbose 0
#define inf 1e9;
using namespace std;

int globalindex = 0;
void write(int n, long long ans){
   ofstream ofs;
   ofs.open ("out.txt", ios_base::app);
   // ofs << fixed << setprecision(6);
   if (ans == -1){
       ofs << "Case #" << n << ": " << "INSOMNIA" << endl;
   }
   else{
       ofs << "Case #" << n << ": " << ans << endl;
   }
   ofs.close();
}
void get_digits(set<int> &digits, long long n){
    while (n > 0){
        digits.insert(n%10);
        n /= 10;
    }
}

long long solve(int N){
    if (N == 0) return -1;
    set<int> digits;
    int i = 1;
    while (digits.size() < 10){
        get_digits(digits, (long long) N*i);
        i += 1;
    }
    i--;
    return i*N;
}

int main(void){
   remove("out.txt");
   int T, N;
   cin >> T;
   for (int i = 0; i < T; i++){
       cin >> N;
       write(i+1, solve(N));
   }
   return 0;
}
