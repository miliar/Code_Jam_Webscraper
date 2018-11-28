#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("inA.txt", "r", stdin);
    freopen("outA.txt", "w", stdout);
    int T;cin >> T;
    for(int cas=1;cas<=T;++cas){
        cout << "Case #" << cas << ": ";
        string s;
        int K, out=0;
        cin >> s >> K;
        for(int i=0;i<=int(s.size())-K;++i){
            if(s[i]=='-'){
                ++out;
                for(int j=i;j<i+K;++j){
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                }
            }
            cerr << s << "\n";
        }
        if(any_of(s.begin(), s.end(), [](char const&a){return a=='-';})) cout << "IMPOSSIBLE";
        else cout << out;

        cout << "\n";
    }

    return 0;
}
