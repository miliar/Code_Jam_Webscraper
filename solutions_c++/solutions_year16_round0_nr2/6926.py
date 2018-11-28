/* do something */

#include <bits/stdc++.h>
#define ll long long
#define over999 1234567890
#define fi first
#define se second
#define mp make_pair
#define pb push_back

using namespace std;

string s;
int ans,t;

int main(){
    cin >> t;
    for(int lap=1;lap<=t;lap++)
    {
        ans=0;
        cin >> s;
        cout << "Case #" << lap << ": ";
        if(s[0]=='-')ans++;
        for(int i=1;i<s.length();i++)
            if(s[i]=='-' && s[i-1]=='+')ans+=2;
        cout << ans << endl;
    }
    return 0;
}