#include <bits/stdc++.h>
using namespace std;

int main(){
    std::ios::sync_with_stdio(false);
    freopen("problema1.in","r",stdin);
    freopen("lolzano.out","w",stdout);
    int n; cin >> n;
    for( int caso = 1 ; caso <= n ; ++caso ){
        string s; cin >> s;
        map<char,int>mp;
        for( int i = 0 ; i < (int)s.size() ; ++i ){
            ++mp[s[i]];
        }
        string ans = "";
        while( mp['Z'] ){
            ans += '0';
            mp['Z']--, mp['E']--, mp['R']--, mp['O']--;
        }
        while( mp['X'] ){
            ans += '6';
            mp['S']--, mp['I']--, mp['X']--;
        }
        while( mp['U'] ){
            ans += '4';
            mp['F']--, mp['U']--, mp['R']--, mp['O']--;
        }
        while( mp['F'] ){
            ans += '5';
            mp['F']--, mp['E']--, mp['I']--, mp['V']--;
        }
        while( mp['W'] ){
            ans += '2';
            mp['W']--, mp['T']--, mp['O']--;
        }
        while( mp['S'] ){
            ans += '7';
            mp['S']--, mp['E']--, mp['V']--, mp['E']--, mp['N']--;
        }
        while( mp['R'] ){
            ans += '3';
            mp['T']--, mp['E']--, mp['R']--, mp['H']--, mp['E']--;
        }
        while( mp['H'] ){
            ans += '8';
            mp['I']--, mp['E']--, mp['G']--, mp['H']--, mp['T']--;
        }
        while( mp['I'] ){
            ans += '9';
            mp['N']--, mp['E']--, mp['I']--, mp['N']--;
        }
        while( mp['N'] ){
            ans += '1';
            mp['N']--, mp['E']--, mp['O']--;
        }
        sort(ans.begin(), ans.end());
        cout << "Case #" << caso << ": " << ans << '\n';
    }
}
