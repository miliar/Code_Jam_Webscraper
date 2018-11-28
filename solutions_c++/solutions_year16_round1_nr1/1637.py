#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>

using namespace std;

#define gettime printf("\nTime : %0.3lf\n",clock()*1.0/CLOCKS_PER_SEC);
#define PB push_back
#define MP make_pair
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define repp(i,a,b) for(int i=a;i>=b;i--)
#define Set(data,value) memset(data,value,sizeof(data));

#define vs vector<string>
#define vi vector<int>
#define ll long long
#define ff first
#define ss second

struct comp {
       bool operator() (int a,int b) {
            return a>b;
       }
};

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    std::ios::sync_with_stdio(false);
    int T, len;
    string data, ans;
    cin>>T;
    rep (t,1,T) {
        cin>>data;
        cout<<"Case #"<<t<<": ";
        len=data.size()-1;
        ans = data[0];
        rep (i,1,len) {
            if (ans[0]<=data[i]) {
                ans = data[i]+ans;
            }
            else ans = ans+data[i];
        }
        cout<<ans<<endl;
    }
    return 0;
}
