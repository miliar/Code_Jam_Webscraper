#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h> 
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

set<int> se;
void add(long long x) {
    do {
        se.insert(x%10);
        x/=10LL;
    }while (x);
}
int main () {
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;
    cin>>T;
    while (T--) {
        int n;
        cin>>n;
        long long ret=-1;
        se.clear();
        for (int i=1;i<=100000;i++) {
            long long now=1LL*i*n;
            add(now);
            if (se.size()==10) {
                ret=now;
                break;
            }
        }
        static int cas=1;
        if (ret!=-1)
            cout<<"Case #"<<cas++<<": "<<ret<<endl;
        else 
            cout<<"Case #"<<cas++<<": "<<"INSOMNIA"<<endl;
    }
    return 0;
}

