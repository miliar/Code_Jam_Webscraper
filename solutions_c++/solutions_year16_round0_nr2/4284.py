#include <bits/stdc++.h>
using namespace std;
const int N = 1e7 + 5;
void flip(string & st , int s , int e){
    for(int i = s; i <= e; ++i){
        if(st[i] == '-') st[i] = '+';
        else st[i] = '-';
    }
}
int main(){
    int t;
    string s;
   // freopen("Ginp.txt" , "r" , stdin);
   // freopen("Goup.txt" , "w" , stdout);
    cin >> t;
    int tt = t;
    while(t--){
        cin >> s;
        int cnt = 0;
        for(int i = s.size() - 1; i >= 0; --i){
            if(s[i] == '+') continue;
            flip(s , 0 , i);
            ++cnt;
        }
        cout << "Case #" << tt - t << ": " << cnt << endl;
    }
    return 0;
}
