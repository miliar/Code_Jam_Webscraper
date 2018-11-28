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

int T,lef;
long long n;
bool is[12];

int main()
{
    freopen("in","r", stdin);
    freopen("out","w",stdout);

    cin >> T;
    for(int ii=1; ii<=T;++ii){
        cin >> n;
        memset(is,true,sizeof(is));
        lef=10;
        bool flg=false;
        for(int i=1; i<1e6+10; ++i){
            long long temp=n*i;
            while(temp>0){
                int tt=temp%10;
                temp/=10;
                if(is[tt]){
                    is[tt]=false;
                    lef--;
                }
                if(lef==0){
                    n=n*i;
                    flg=true;
                    i=1e6+11;
                    break;
                }
            }
        }
        cout << "Case #" << ii<<": ";
        if(flg)
            cout << n << endl;
        else cout << "INSOMNIA" <<endl;
    }

    return 0;
}
