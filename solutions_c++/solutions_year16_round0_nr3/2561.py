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

const int MaxLen=18;
typedef long long ll;

int T;
ll n,j, maxn;
vector< vector<int> > ans;

bool isprimes(ll a, ll &div){
    if(a<2) return false;
    if(a==2) return true;

    for(ll i=3; i*i<=a; i+=2)
        if(a%i==0){
            div=i;
            return false;
        }
    return true;
}

bool checks(ll k){
    ll temp=k;
    ll powsans[13];
    ll pows[13];
    memset(powsans,0,sizeof(powsans));
    memset(pows,0,sizeof(pows));
    for(int i=2; i<=10; ++i)
        pows[i]=1;
    while(k>0){
        if(k&1){
            for(int i=2; i<=10; ++i)
                powsans[i]+=pows[i];
        }

        k>>=1;
        for(int i=2; i<=10; ++i)
            pows[i]=pows[i]*i;
    }
    vector<int> temps;
    temps.push_back(temp);
    for(int i=2; i<=10; ++i){
//        cout << powsans[i] << " ";
        ll div;
        if(isprimes(powsans[i], div))
            return false;
        temps.push_back(div);
    }
    ans.push_back(temps);
    return true;
}

int main()
{
    freopen("in","r", stdin);
    freopen("out","w",stdout);

    cin >> T;
    for(int ii=1; ii<=T;++ii){
        cin >> n >> j;
        maxn = (1L<<n);

        for(ll i=(1L<<(n-1))+1; i<maxn; i=i+2){
            bool flg = checks(i);
  //          cout << ans.size() << endl;
            if(ans.size()==j){
                break;
            }
        }

        cout << "Case #"<<ii<<":"<<endl;
        for(int i=0; i<ans.size(); ++i){
            bitset<16> bits(ans[i][0]);
            cout << bits ;
            for(int j=1; j<ans[i].size(); ++j)
                cout << " " << ans[i][j];
            cout << endl;
        }


        //cout << "Case #" << ii<<": " << ans <<endl;
    }

    return 0;
}
