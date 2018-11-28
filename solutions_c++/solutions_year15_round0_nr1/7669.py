#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <new>
#include <string>
#include <sstream>
#include <numeric>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <climits>

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;

#define N 100005
#define MOD 1000000007

int main() {
    //ios_base::sync_with_stdio(false);
    //freopen("input","r",stdin);
    //freopen("output","w",stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++) {
        int sm;
        cin>>sm;
        string a;
        cin>>a;
        int *s;
        s=new int[sm+1];
        for(int i=0;i<=sm;i++) {
            s[i]=a[i]-'0';
        }
        LL ans=0;LL csc=0;
        for(int i=0;i<=sm;i++) {
            if(s[i]==0)
                continue;
            if(csc>=i) {
                csc+=s[i];
            }
            else {
                ans+=(i-csc);
                csc=i+s[i];
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
