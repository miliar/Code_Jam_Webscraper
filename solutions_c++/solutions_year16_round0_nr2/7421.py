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
const ll MAXN = 1000001;
using namespace std;

string s;
int n,cnt=0;
bool ok(string s){
    for(auto x:s)
        if(x=='-')
            return false;
    return true;
}
void slove(string s){
    int ans=0;
    while(!ok(s)){
        int start=0;
        char flag=s[0];
        while(s[start]==flag) start++;
        for(int i=0;i<start;i++){
            s[i]=='-'? s[i]='+':s[i]='-';
        }
        ans++;
    }
    printf("Case #%d: %d\n",++cnt,ans);
}
int main(){
    freopen("/Users/gexin/Downloads/B-small-attempt0.in.txt","r",stdin);
    freopen("/Users/gexin/Desktop/out.txt","w",stdout);
    cin>>n;
    while(n--){
        cin>>s;
        slove(s);
    }
    return 0;
}