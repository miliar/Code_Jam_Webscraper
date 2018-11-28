#include <bits/stdc++.h>

using namespace std;

typedef long long int li;

map <pair <char, char>, pair<char, li> > mp;

void pre()
{
    li i;
    mp[make_pair('a', 'i')] = make_pair('i', 0);
    mp[make_pair('a', 'j')] = make_pair('j', 0);
    mp[make_pair('a', 'k')] = make_pair('k', 0);
    mp[make_pair('i', 'a')] = make_pair('i', 0);
    mp[make_pair('j', 'a')] = make_pair('j', 0);
    mp[make_pair('k', 'a')] = make_pair('k', 0);

    mp[make_pair('a','a')] = make_pair('a', 0);
    mp[make_pair('i','i')] = make_pair('a', 1);
    mp[make_pair('j','j')] = make_pair('a', 1);
    mp[make_pair('k','k')] = make_pair('a', 1);

    mp[make_pair('i','j')] = make_pair('k', 0);
    mp[make_pair('i','k')] = make_pair('j', 1);
    mp[make_pair('j','i')] = make_pair('k', 1);
    mp[make_pair('j','k')] = make_pair('i', 0);
    mp[make_pair('k','i')] = make_pair('j', 0);
    mp[make_pair('k','j')] = make_pair('i', 1);

}

int main() {

    li t, l, x, i, cnt = 0;
    pre();
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    while(t--){
        li f = -1;
        li sign = 0;
        cin >> l >> x;
        string s = "", temp;
        cin >> temp;
        while(x--){
            s += temp;
        }

        char ch = 'a';

        for(i = 0;i < s.size(); ++i){
            sign += mp[make_pair(ch, s[i])].second;
            ch = mp[make_pair(ch, s[i])].first;
            sign %= 2;
            if(ch == 'i' && sign == 0) break;

        }
        if(i == s.size()){
            printf("Case #%lld: NO\n", ++cnt);
            continue;
        }
        ch = 'a';
        for(i = i + 1;i < s.size(); ++i){
            sign += mp[make_pair(ch, s[i])].second;
            ch = mp[make_pair(ch, s[i])].first;
            sign %= 2;
            if(ch == 'j' && sign == 0) break;
        }
        if(i == s.size()){
            printf("Case #%lld: NO\n", ++cnt);
            continue;
        }
        ch = 'a';
        for(i = i + 1;i < s.size(); ++i){
            sign += mp[make_pair(ch, s[i])].second;
            ch = mp[make_pair(ch, s[i])].first;
            sign %= 2;
            if(ch == 'k' && sign == 0){
                f = i;
            }
        }
        if(f == s.size() - 1){
            printf("Case #%lld: YES\n", ++cnt);
            continue;
        }
        else{
            printf("Case #%lld: NO\n", ++cnt);
        }
    }
}
