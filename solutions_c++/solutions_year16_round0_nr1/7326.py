#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <string>
#include <functional>
#define x first
#define y second
#define pb push_back
#define forn(i,n) for(int i=0;i<n;i++)
#define mst(a,i) memset(a,i,sizeof(a))
#define mp(x,y) make_pair(x,y)
typedef long long ll;
typedef long double ld;
typedef std::pair<int,int> pii;
const double pi=acos(-1.0);
const ll MAXN = 550;
using namespace std;

set<int> num;
int t,cnt=1,x,ans[2222];

void go(int i){
    while(i>0){
        num.insert(i%10);
        i/=10;
    }
}
int slove(int n){
    num.clear();
    for(int i=1;i<=20000;i++){
        go(i*n);
        if(num.size()==10)
            return i*n;
    }
    return -1;
}
int main(){
    
    freopen("/Users/gexin/Desktop/A-small-attempt6.in.txt","r",stdin);
    freopen("/Users/gexin/Desktop/out.txt","w",stdout);
    cin>>t;
    for(int n=0;n<=2200;n++)
        ans[n]=slove(n);
    
    while(cnt<=t){
        cin>>x;
        if(ans[x]!=-1)
            // cout<<"Case #"<<cnt<<": "<<ans[x]<<endl;
            printf("Case #%d: %d\n",cnt,ans[x]);
        else
            // cout<<"Case #"<<cnt<<": INSOMNIA"<<endl;
            printf("Case #%d: INSOMNIA\n",cnt);
        cnt++;
    }
    return 0;
}