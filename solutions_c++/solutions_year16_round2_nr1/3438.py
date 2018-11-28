#include <bits/stdc++.h>

using namespace std;

string digit[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
map<char, int> mp;
int test;

bool check(string s, int cnt){
    bool ok = true;
    int i;
    for (i = 0; i < s.length(); ++i){
        if (mp[s[i]] - cnt < 0){ok = false; break;}
        mp[s[i]] -= cnt;
    }
    for (int j = 0; j < i; ++j)
        mp[s[j]] += cnt;
    return ok;
}

void del(string s, int cnt){
    for (int i = 0; i < s.length(); ++i){
        mp[s[i]] -= cnt;
    }
}

void add(string s, int cnt){
    for (int i = 0; i < s.length(); ++i){
        mp[s[i]] += cnt;
    }
}

bool is_empt(){
    map<char, int>::iterator it;
    for (it = mp.begin(); it != mp.end(); ++it)
        if (it->second != 0) return false;
    return true;
}

int cnt[10];

bool slv(int num){
    if (is_empt()) return true;
    if (num >= 10) return false;
    for (int i = 0; i < 100; ++i){
        if (!check(digit[num], i)) return false;
        del(digit[num], i);
        bool p = slv(num + 1);
        add(digit[num], i);
        if (p){
            cnt[num] = i;
            return true;
        }
    }
}
string solve(string s){
    mp.clear();
    for (int i = 0; i < s.length(); ++i) mp[s[i]]++;
    slv(0);
    string ans;
    for (int i = 0; i < 10; ++i){
        while (cnt[i]) {
            ans += char('0' + i);
            cnt[i]--;
        }
    }
    return ans;
}
int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> test;
    for (int t = 1; t <= test; ++t){
        string s; cin >> s;
        cout << "Case #" << t << ": " << solve(s) << endl;
    }
    return 0;
}
