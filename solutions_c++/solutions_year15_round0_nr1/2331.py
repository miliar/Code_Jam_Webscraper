#include <bits/stdc++.h>
using namespace std;

#define DB(v) cerr << #v << ' ' << v << endl
#define where(v) cerr << #v << ": " << v << ' '
#define F first
#define S second
#define pb push_back
#define forup(i,a,b) for(int i = a;i <= (int)b;++i)

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tests; cin >> tests;
    forup(test,1,tests){
        string s;
        int max_level;
        cin >> max_level >> s;
        int ans = 0,cur = (s[0] - '0');
        forup(i,1,(int)s.length() - 1){
            if(s[i] == '0'){continue;}
            ans += max(0,i - cur);
            cur = max(i,cur);
            cur += (s[i] - '0');
        }
        cout << "Case #" << test << ": " << ans << '\n';
    }
    return 0;
}
