#include <vector>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    string S;
    cin>>T;
    for(int ca=1;ca<=T;ca++) {
        cin>>S;
        int len = S.length();
        cout<<"Case #"<<ca<<": ";
        if(len==1)
        {
            cout<<S<<endl;
            continue;
        }
        string ans = "";
        if(S[0] > S[1]) {
            ans += S[0];
            ans += S[1];
        } else {
            ans += S[1];
            ans += S[0];
        }
        for(int i=2;i<len;i++) {
            int ll = ans.length();
            int j = 0;
            while(j < ll) {
                if(S[i] == ans[j]) {
                    j++;
                    continue;
                }
                if(S[i] > ans[j]) {
                    ans = (S.substr(i,1) + ans);
                    break;
                } else {
                    ans += S[i];
                    break;
                }
            }
            if(j == ll) ans += S[i];
        }
        cout<<ans<<endl;
    }

    return 0;
}
