#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<sstream>
#include<queue>
#include<algorithm>
#include<string>
#include<cmath>
#include<bits/stdc++.h>
using namespace std;

int T;
string s;

int main()
{
    freopen("in","r", stdin);
    freopen("out","w",stdout);

    cin >> T;
    for(int ii=1; ii<=T;++ii){
        cin >> s;
        int len=s.size();
        int ans=0;
        if(s[len-1]=='-')
            ans++;
        for(int i=len-2; i>=0; i--){
            if(s[i]!=s[i+1])
                ans++;
        }
        cout << "Case #" << ii<<": " << ans <<endl;
    }

    return 0;
}
