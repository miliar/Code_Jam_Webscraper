
//
// Created by 鲁蕴铖 on 16/5/8.
//



#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <thread>
#include <random>
#include <iomanip>
#include <queue>
#include <set>
#include <map>
using namespace std;

int n, p[300];

void solve(){
    while(1) {
        int sum = 0;
        for(int i = 0; i < n; i++) {
            sum += p[i];
        }
        if(sum >= 1 && sum <= 2) {
            cout<<" ";
            for(int i = 0; i < n; i++) {
                if(p[i] > 0) {
                    p[i]--;
                    char c = 'A' + i;
                    cout<<c;
                }
                if(p[i] > 0) {
                    p[i]--;
                    char c =  'A' + i;
                    cout<<c;
                }
            }
            break;
        }

        int pos = -1, maxv = 0;
        for(int i = 0; i < n; i++) {
            if(p[i] > maxv) {
                maxv = p[i];
                pos = i;
            }
        }
        if(pos >= 0) {
            char c = 'A' + pos;
            cout<<" "<< c;
            p[pos]--;
        }

        pos = -1, maxv = 0;
        for(int i = 0; i < n; i++) {
            if(p[i] > maxv) {
                maxv = p[i];
                pos = i;
            }
        }
        if(sum >= 4 && pos >= 0)
        {
            char c= 'A' + pos;
            cout<<c;
            p[pos]--;
        }
    }
    cout<<endl;
}
int main()
{

    //#ifndef ONLINE_JUDGE
    freopen("/Users/luyuncheng/Downloads/A-large.in", "r", stdin);
    freopen("/Users/luyuncheng/Downloads/A-large.out", "w", stdout);
//#endif
    int T;
    while(cin>>T) {
        int cas = 1;

        while(T--) {
            cin>>n;
            for(int i = 0; i < n; i++) {
                cin>>p[i];
            }
            cout << "Case #" << cas++ <<":";
            solve();
        }
    }
}


