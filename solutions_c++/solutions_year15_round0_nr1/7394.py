#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <time.h>
#include <cassert>
#include <bitset>
using namespace std;

int main () {
    freopen("in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    for (int cas=1;cas<=T;cas++) {
        int n;
        cin>>n;
        string s;
        cin>>s;
        //cout<<n<<" "<<s<<endl;
        int need=0;
        int cnt=s[0]-'0';
        for (int i=1;i<=n;i++) {
            int u=s[i]-'0';
            if (u==0) continue;
            if (cnt<i) {
                need+=i-cnt;
                cnt+=u+i-cnt;
            }
            else cnt+=u;
        }
        cout<<"Case #"<<cas<<": "<<need<<endl;
    }
    return 0;
}
