#include <cstring>
#include <string>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <iostream>
using namespace std;

int n;
double a[1111],b[1111];
int ai,aj,bi,bj;

int get1(){
    ai=bi=0;aj=bj=n-1;
    int ans=0;
    while(bi<=bj){
        if(b[bi]>a[ai]){
            ai++;bi++;
        }
        else bi++,ans++;
    }
    return ans;
}

int get2(){
    ai=bi=0;aj=bj=n-1;
    int ans=0;
    while(bi<=bj){
        if(b[bi]>a[ai]){
            ai++;bj--;
        }
        else {
            ans++;ai++;bi++;
        }
    }
    return ans;
}

int main(){
    //freopen("D-small-attempt0.in","r",stdin);
    //freopen("as.out","w",stdout);
    int t;cin>>t;
    for(int i=1;i<=t;i++){
        cin>>n;
        for(int i=0;i<n;i++)cin>>a[i];
        for(int i=0;i<n;i++)cin>>b[i];
        sort(a,a+n);sort(b,b+n);
        printf("Case #%d: %d %d\n",i,get2(),get1());
    }
    //fclose(stdin);
    //fclose(stdout);
}
