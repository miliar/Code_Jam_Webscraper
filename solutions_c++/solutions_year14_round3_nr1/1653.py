#include <vector>
#include <iostream>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int main(int argc, char* argv[]) {
    int T;
    cin>>T;
    for (int t=1;t<=T;++t) {
        cout<<"Case #"<<t<<": ";
        long long p,q;
        char div;
        cin>>p;
        cin>>div;
        cin>>q;
        bool possible=false;
        long long x=q;
        while (x%2==0) {
            x/=2;
            if (x==p) {
                possible =true;
                break;
            }
        }
        if (x==1) {
            possible=true;
        }

        if (!possible) {
            cout<<"impossible"<<endl;   
        } else {
            int ans=1;
            p<<=1;
            while (p < q) {
                p<<=1;
                ans++;
            }
            cout<<ans<<endl;
        }
    }
    return 0;
}
