#include <bits/stdc++.h>

#define verbose 0
#define inf 1e9;
using namespace std;

void write(int n, int ans){
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

void flip_substack(string &s, int c){
    string subs = s;
    subs.resize(c);
    reverse(subs.begin(), subs.end());
    for (int i = 0; i < c; i++){
        if (subs[i] == '+') subs[i] = '-';
        else subs[i] = '+';
        s[i] = subs[i];
    }
}


int solve(string s){
    int flip = 0;
    int l = s.size();
    while (l > 0){
        if (s[l-1] == '+'){
            s.resize(l-1);
            l--;
        }
        else{
            if (s[0] == '-'){
                flip_substack(s, l);
            }
            else{
                int c = 1;
                while (s[c] == '+'){
                    c++;
                }
                flip_substack(s,c);
            }

            flip++;
        }
    }
    return flip;
}

int main(void){
   remove("out.txt");
   int T;
   string s;
   cin >> T;
   for (int i = 0; i < T; i++){
       cin >> s;
       write(i+1, solve(s));
   }
   return 0;
}
