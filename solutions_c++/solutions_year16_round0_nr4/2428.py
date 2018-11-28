#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<bitset>
#include<sstream>
#include<queue>
#include<algorithm>
#include<string>
#include<cmath>
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

ll T,k,c,s;


int main()
{
    freopen("in","r", stdin);
    freopen("out","w",stdout);

    cin >> T;
    for(int ii=1; ii<=T; ++ii){
        cin >> k >> c >> s;
        ll step = pow(k,c-1);
        ll maxn = step*k;
//        cout << step<<endl;
        vector<ll> ans;
        ll t=1;
        while(t<=maxn){
            ans.push_back(t);
            t+=step;
        }
        printf("Case #%d:", ii);
        if(s==k){
            for(int i=0; i<ans.size(); ++i)
                cout << " " << ans[i];
            cout << endl;
        }
        else{
            cout << " IMPOSSIBLE" << endl;
        }


    }


    return 0;
}
