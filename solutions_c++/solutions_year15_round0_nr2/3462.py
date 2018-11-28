#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <cassert>
#include <cstdio>
#include <set>
using namespace std;

struct ptr_compare
{
    bool operator()(int a, int b) const
    {
        return a > b;
    }
};
int can(vector<int> &a,int x){

    int sul = 0;

    int z = 0;

    for(auto elem : a)
        while(elem > x){
            elem -= x;
            z++;
        }


    return z + x;
}

int solve(){
    int n;cin>>n;
    vector<int> in(n);
    for(auto &a : in) cin>>a;
    sort(in.rbegin(),in.rend());

    int mx = *max_element(in.begin(),in.end());
    int ans = 10000000;

    for(int i = 1; i <= mx; i++){
        ans = min(ans,can(in,i));
    }

    return ans;
}


int main() {
    freopen("C:\\a.txt","r",stdin);
    freopen("C:\\w.txt","w",stdout);

    int n;cin>>n;
    for(int i = 1; i <= n;i++){
        printf("Case #%d: %d\n",i,solve());

    }
    return 0;
}
