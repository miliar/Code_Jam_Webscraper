#include <bits/stdc++.h>

using namespace std;

int i,j,k,l,m,n,t, p, r, s;
string ans1, ans2, ans3;

string solve(char start, int level){
    int i;
    string answer = "";
    answer += start;
    string tmp1, tmp2;
    if (level == 0) return answer;
            if (start == 'S'){
                tmp2 = solve('P', level - 1);
                tmp1 = solve('S', level - 1);
                if (tmp1 < tmp2){
                    answer = tmp1 + tmp2;
                } else
                    answer = tmp2 + tmp1;
            } else
            if (start == 'R'){
                tmp2 = solve('R', level - 1);
                tmp1 = solve('S', level - 1);
                if (tmp1 < tmp2){
                    answer = tmp1 + tmp2;
                } else
                    answer = tmp2 + tmp1;
            } else
            if (start == 'P'){
                tmp1 = solve('R', level - 1);            
                tmp2 = solve('P', level - 1);
                if (tmp1 < tmp2){
                    answer = tmp1 + tmp2;
                } else
                    answer = tmp2 + tmp1;
            }


    return answer;
}

bool good(string check){
    int i, pp = 0, rr = 0, ss = 0;
    for (i = 0; i < check.length(); i++){
        if (check[i] == 'P') pp++; else
        if (check[i] == 'R') rr++; else
        ss++;
    }
    if (s == ss && p == pp && r == rr) return 1; else
    return 0;
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int test = 0; test < t; test++){
        cout << "Case #"<< test+1 << ": ";
        cin >> n;
        cin >> r >> p >> s;
        ans1 = solve('R', n);
        ans2 = solve('S', n);
        ans3 = solve('P', n);
        string answer = "";
        //cout << ans1 <<"\n"<< ans2 <<"\n"<< ans3 << "\n";
        if (good(ans1)){
            answer = ans1;
        }        
        if (good(ans2)){
            if (answer.size() == 0 || answer > ans2){
                answer = ans2;            
            }
        }
        if (good(ans3)){
            if (answer.size() == 0 || answer > ans3){
                answer = ans3;            
            }
        }
        if (answer.length() == 0) cout << "IMPOSSIBLE\n"; else        
        cout << answer << "\n";
    }
    return 0;
}
