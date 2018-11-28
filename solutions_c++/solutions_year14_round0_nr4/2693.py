#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <stack>
#include <cstring>
#include <cctype>
#include <cstring>
#include <cstdlib>
#include <iomanip>


using namespace std;

#define INFY 1000000000


int main() {
    freopen("/Users/arunamahesh/D-large.in","r",stdin);
    freopen("/Users/arunamahesh/GCJ_output.txt","w",stdout);
    int T; cin>>T;
    for(int t = 1;t <= T;t++) {
        int n; cin>>n;
        vector<double> a(n),b(n),ac(n),bc(n);
        for(int i = 0;i < n;i++) cin>>a[i];
        for(int i = 0;i < n;i++) cin>>b[i];
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        int cnt1 = 0,cnt2 = 0;
        ac = a;
        bc = b;
        for(int i = 0;i < n;i++) {
            if(ac[i] > bc[bc.size() - 1]) break;
            bc.erase(upper_bound(bc.begin(), bc.end(),ac[i]));
            cnt2++;
        }
        cnt2 = n - cnt2;
        while(!a.empty() && (a[0] < b[0])) {
            a.erase(a.begin());
            b.erase(b.begin()+b.size()- 1);
        }
        for(int i = 0;i < b.size();i++) {
            if(b[i] > a[a.size() - 1]) break;
            a.erase(upper_bound(a.begin(), a.end(),b[i]));
            cnt1++;
        }
        cout<<"Case #"<<t<<": "<<cnt1<<' '<<cnt2<<endl;
    }
    
    
    
    
        
}