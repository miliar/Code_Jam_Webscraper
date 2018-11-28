#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>


using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int t;
    string pat;
    int kase = 1;
    cin>>t;
    while (t--) {
        cin>>pat;
        vector<char> shrinkChar;
        int i,len;
        len = pat.size();
        char lastChar = 'c';
        for (i=0; i< len;i++)
            if ( pat[i] != lastChar) {
                lastChar = pat[i];
                shrinkChar.pb(lastChar);
            }
        int ans;
        if ( shrinkChar.back() == '+')
            ans = shrinkChar.size() - 1;
        else
            ans = shrinkChar.size();
        pf("Case #%d: %d\n",kase++, ans);
    }
    return 0;
}
