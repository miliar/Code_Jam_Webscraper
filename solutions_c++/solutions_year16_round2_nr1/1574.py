#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <vector>
using namespace std;
int d[256], ans[1000];
int main(){
    int T;
    cin >> T;
    string s;
    for(int t = 1; t <= T; t++){
        cin >> s;
        memset(d, 0, sizeof(d) );
        int cnt = 0;
        for(int i = 0; i < s.size(); i++){
            d[ s[i] ]++;
            cnt++;
        }

        int len = 0;
        while( cnt > 0 ){/*
            puts("-------------");
                for(int i = 'A'; i <= 'Z'; i++){
            if(d[i] != 0)
                cout << (char)i << " " << d[i] << endl;
        }*/
            if(d[ 'Z' ]){
                cnt -= 4;
                ans[len++] = 0;
                d['Z']--, d['E']--, d['R']--, d['O']--;
            }
            else if(d['X']){
                cnt -= 3;
                ans[len++] = 6;
                d['S']--, d['I']--, d['X']--;
            }
            else if(d['W']){
                cnt -= 3;
                ans[len++] = 2;
                d['T']--, d['W']--, d['O']--;
            }
            else if(d['U']){
                cnt -= 4;
                ans[len++] = 4;
                d['F']--, d['O']--, d['U']--, d['R']--;
            }
            else if(d['G']){
                cnt -= 5;
                ans[len++] = 8;
                d['E']--, d['I']--, d['G']--, d['H']--, d['T']--;
            }
            //-----------
            else if(d['O']){
                cnt -= 3;
                ans[len++] = 1;
                d['O']--, d['N']--, d['E']--;
            }

            else if(d['F']){
                cnt -= 4;
                ans[len++] = 5;
                d['F']--, d['I']--, d['V']--, d['E']--;
            }
            else if(d['T']){
                cnt -= 5;
                ans[len++] = 3;
                d['T']--, d['H']--, d['R']--, d['E']-= 2;
            }
            else if(d['S']){
                cnt -= 5;
                ans[len++] = 7;
                d['S']--, d['E']-= 2, d['V']--, d['N']--;
            }
            else{
                cnt -= 4;
                ans[len++] = 9;
                d['N']-=2, d['I']--, d['E']--;
            }
        }

        for(int i = 'A'; i <= 'Z'; i++){
            if(d[i] != 0)
                cout << (char)i << " " << d[i] << endl;
                }
        sort(ans, ans + len);
        cout << "Case #" << t << ": ";
        for(int i = 0; i < len; i++)
            cout << ans[i];
        puts("");
    }
    return 0;
}
