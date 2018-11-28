#include<bits/stdc++.h>
using namespace std;


int solve(string &s){
    int sol = 0;
    int idx = s.size() - 1;
    while(idx >= 0){
        if(s[idx] == '+'){
            idx--;
        }else{
            if(s[0] == '+'){
                int i = 0;
                while(i < idx && s[i] == '+'){                    
                    s[i] = '-';
                    i++;
                }
                sol++;
            }else{
                reverse(s.begin(), s.begin() + idx + 1);
                for(int i = 0; i <= idx; i++){
                    if(s[i] == '+') s[i] = '-';
                    else            s[i] = '+';
                }
                sol++;

            }
        }
    }
    return sol; 
}

int main(){
    string s;
    int tc = 0, t; cin >> t;
    while(t--){
        cin >> s;
        cout << "Case #" << ++tc << ": " << solve(s) << endl;
    }
}


