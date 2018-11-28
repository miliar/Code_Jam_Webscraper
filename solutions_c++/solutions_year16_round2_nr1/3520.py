#include <bits/stdc++.h>
using namespace std;

int T;

string fin;
void rec(int *c, string ans, int charleft){
    if (charleft == 0){
        fin = ans;
        return;
    }
    for(int i = 0; i<=9; i++){
            if (i == 0){
                if (c['Z'] > 0 && c['E'] > 0 && c['R'] > 0 && c['O'] > 0){
                    ans += '0';
                    c['Z']--;
                    c['E']--;
                    c['R']--;
                    c['O']--;
                    rec(c, ans, charleft - 4);
                    ans = ans.substr(0, ans.length()-1);
                    c['Z']++;
                    c['E']++;
                    c['R']++;
                    c['O']++;
                }
            }
            else if (i == 1){
                if (c['O'] > 0 && c['E'] > 0 && c['N'] > 0){
                    ans += '1';
                    c['O']--;
                    c['N']--;
                    c['E']--;
                    rec(c, ans, charleft - 3);
                    c['O']++;
                    c['N']++;
                    c['E']++;
                    ans = ans.substr(0, ans.length()-1);
                }
            }
             else if (i == 2){
                if (c['T'] > 0 && c['W'] > 0 && c['O'] > 0){
                    ans += '2';
                    c['T']--;
                    c['W']--;
                    c['O']--;
                    rec(c, ans, charleft - 3);
                    c['T']++;
                    c['W']++;
                    c['O']++;
                    ans = ans.substr(0, ans.length()-1);
                }

            }
             else if (i == 3){
                if (c['T'] > 0 && c['H'] > 0 && c['R'] > 0 && c['E'] > 1){
                    ans += '3';
                    c['T']--;
                    c['H']--;
                    c['R']--;
                    c['E']-=2;
                    rec(c, ans, charleft - 5);
                    c['T']++;
                    c['H']++;
                    c['R']++;
                    c['E']+=2;
                    ans = ans.substr(0, ans.length()-1);
                }
            }
             else if (i == 4){
                if (c['F'] > 0 && c['O'] > 0 && c['R'] > 0 && c['U'] > 0){
                    ans += '4';
                    c['F']--;
                    c['O']--;
                    c['U']--;
                    c['R']--;
                    rec(c, ans, charleft - 4);
                    c['F']++;
                    c['O']++;
                    c['U']++;
                    c['R']++;
                    ans = ans.substr(0, ans.length()-1);
                }
            }
             else if (i == 5){
                if (c['F'] > 0 && c['I'] > 0 && c['V'] > 0 && c['E'] > 0){
                    ans += '5';
                    c['F']--;
                    c['I']--;
                    c['V']--;
                    c['E']--;
                    rec(c, ans, charleft - 4);
                    c['F']++;
                    c['I']++;
                    c['V']++;
                    c['E']++;
                    ans = ans.substr(0, ans.length()-1);
                }
            }
             else if (i == 6){
                if (c['S'] > 0 && c['I'] > 0 && c['X'] > 0){
                    ans += '6';
                    c['S']--;
                    c['I']--;
                    c['X']--;
                    rec(c, ans, charleft - 3);
                    c['S']++;
                    c['I']++;
                    c['X']++;
                    ans = ans.substr(0, ans.length()-1);
                }
            }
             else if (i == 7){
                if (c['S'] > 0 && c['E'] > 1 && c['V'] > 0 && c['N'] > 0){
                    ans += '7';
                    c['S']--;
                    c['E']-=2;
                    c['V']--;
                    c['N']--;
                    rec(c, ans, charleft - 5);
                    c['S']++;
                    c['E']+=2;
                    c['V']++;
                    c['N']++;
                    ans = ans.substr(0, ans.length()-1);
                }
            }
             else if (i == 8){
                if (c['E'] > 0 && c['I'] > 0 && c['G'] > 0 && c['H'] > 0 && c['T'] > 0){
                    ans += '8';
                    c['E']--;
                    c['I']--;
                    c['G']--;
                    c['H']--;
                    c['T']--;
                    rec(c, ans, charleft - 5);
                    c['E']++;
                    c['I']++;
                    c['G']++;
                    c['H']++;
                    c['T']++;
                    ans = ans.substr(0, ans.length()-1);
                }
            }
             else if (i == 9){
                if (c['N'] > 1 && c['I'] > 0 && c['E'] > 0){
                    ans += '9';
                    c['N']-=2;
                    c['I']--;
                    c['E']--;
                    rec(c, ans, charleft - 4);
                    c['N']+=2;
                    c['I']++;
                    c['E']++;
                    ans = ans.substr(0, ans.length()-1);
                }
            }

        }
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas<=T; cas++){
        printf("Case #%d: ", cas);
        string s;
        int c[1000] = {0};

        cin >> s;
        for (int i = 0; i<s.length(); i++){
            c[s[i]]++;
        }
        rec(c, "", s.length());
        for (std::string::reverse_iterator rit=fin.rbegin(); rit!=fin.rend(); ++rit)
            std::cout << *rit;
            cout << endl;


    }


}
