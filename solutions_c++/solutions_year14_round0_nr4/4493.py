#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
using namespace std;

const int N=1111;
double len1[N],len2[N];
int getP1(int n){
    int l2l=1,l2r=n;
    int ans=0;
    for (int l1=1;l1<=n;l1++){
        if (len1[l1]>len2[l2l]){
            l2l++;
            ans++;
        }
        else {
            l2r--;
        }
    }
    return ans;
}
int getP2(int n){
    int l1=1,l2=1;
    int ans=n;
    for (;l1<=n;l1++){
        bool found=false;
        for (;l2<=n&&!found;l2++){
            if (len2[l2]>len1[l1]){
                found=true;
            }
        }
        if (found)
            ans--;
        else break;
    }
    return ans;
}
int main() {

    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=1;
    cin>>T;
    while (T--){
        int n;
        cin>>n;
        for (int i=1;i<=n;i++)
            cin>>len1[i];
        for (int i=1;i<=n;i++)
            cin>>len2[i];
        sort(len1+1,len1+1+n);
        sort(len2+1,len2+1+n);
        printf("Case #%d: %d %d\n",cas++,getP1(n),getP2(n));
    }
    return 0;
}
