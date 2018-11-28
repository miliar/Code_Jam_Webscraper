#include <iostream>
#include <map>
#include <cstring>
#include <cstdio>

using namespace std;

int main()
{
    freopen("a.txt", "r", stdin);
    freopen("b.txt", "w", stdout);
    map<char, bool> m;
    m['+'] = true;
    m['-'] = false;
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        char s[110];
        cin >> s;
        int l = strlen(s);
        int j=0;
        bool state = m[s[j++]];
        int ans = 0;
        while(j < l){
            while(j < l && state == m[s[j]])j++;

            if(j < l){ans++;state = !state;}
        }
        if(!state)ans++;
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
