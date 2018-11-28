#include <bits/stdc++.h>
using namespace std;
int cnt[26];
int cntDig[10];
string nums[10] ={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
void getCnt(int num, char recCh){
    cntDig[num] = cnt[recCh - 'A'];
    int sz = nums[num].size();
    for(int i = 0;i < sz;++i){
        cnt[nums[num][i] - 'A'] -= cntDig[num];
    }
}
int main(){
    freopen("../A-large.in", "r", stdin);
    freopen("../outputA.txt", "w", stdout);
    int t;
    cin >> t;
    for(int tc = 1;tc <= t;++tc){
        string s;
        cin >> s;
        int N = s.size();
        for(int i = 0;i < 26;++i){
            cnt[i] = 0;
        }
        for(int i = 0;i < 10;++i){
            cntDig[i] = 0;
        }
        for(int i = 0;i < N;++i){
            ++cnt[s[i] - 'A'];
        }
        getCnt(2, 'W');
        getCnt(4, 'U');
        getCnt(6, 'X');
        getCnt(5, 'F');
        getCnt(7, 'V');
        getCnt(0, 'Z');
        getCnt(1, 'O');
        getCnt(3, 'R');
        getCnt(8, 'H');
        getCnt(9, 'E');
        string ans = "";
        for(int i = 0;i < 10;++i){
            while(cntDig[i]--){
                ans += i + '0';
            }
        }
        cout <<"Case #"<<tc<<": " << ans << endl;
    }
    return 0;
}
