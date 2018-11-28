#include <bits/stdc++.h>

using namespace std;
map <char, int> mp;

int main()
{
    int cases = 1, t;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        string s, ans;
        cin>>s;
        for(int i=0;i<s.size();i++)
            mp[s[i]]++;
        while(mp['Z']>0){
            mp['Z']--, mp['E']--, mp['R']--, mp['O']--;
            ans+='0';
        }
        while(mp['X']>0){
            mp['S']--, mp['I']--, mp['X']--;
            ans+='6';
        }
        while(mp['W']>0){
            mp['T']--, mp['W']--, mp['O']--;
            ans+='2';
        }
        while(mp['G']>0){
            mp['E']--, mp['I']--, mp['G']--, mp['H']--, mp['T']--;
            ans+='8';
        }
        while(mp['U']>0){
            mp['F']--, mp['O']--, mp['R']--, mp['U']--;
            ans+='4';
        }
        while(mp['F']>0){
            mp['F']--, mp['I']--, mp['V']--, mp['E']--;
            ans+='5';
        }
        while(mp['V']>0){
            mp['S']--, mp['E']-=2, mp['V']--, mp['N']--;
            ans+='7';
        }
        while(mp['T']>0){
            mp['T']--, mp['H']--, mp['R']--, mp['E']-=2;
            ans+='3';
        }
        while(mp['I']>0){
            mp['N']-=2, mp['I']--, mp['E']--;
            ans+='9';
        }

        while(mp['O']>0&&mp['N']>0&&mp['E']>0){
            mp['O']--, mp['N']--, mp['E']--;
            ans+='1';
        }

        sort(ans.begin(), ans.end());
        printf("Case #%d: ", cases++);
        cout<<ans<<"\n";
        ans.clear();
        mp.clear();
    }
    return 0;
}
