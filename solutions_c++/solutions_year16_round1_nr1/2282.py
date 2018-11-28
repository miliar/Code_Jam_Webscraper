#pragma comment(linker, "/STACK:102400000,102400000")
#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>
#include <map>
#include <string.h>
#include <assert.h>
#include <set>
#include <cmath>
using namespace std;
#define vi vector<int>
#define pii pair<int,int>
#define pb push_back
#define mp make_pair
#define all(x) x.begin(),x.end()
#define SZ(x) (int)(x.size())
#define rep(i,a,b) for(int i=a;i<b;i++)
#define per(i,a,b) for(int i=b-1;i>=a;i--)
#define inf 1000000007
#define mod 1000000007
#define x first
#define y second
#define pi acos(-1.0)
#define DBG(x) cerr<<(#x)<<"="<<x<<"\n";
//#define dprintf(...) 
#define hash _hash
//#define dprintf(...) fprintf(outFile,__VA_ARGS__)
 
#define FOREACH(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
#define ull unsigned long long
#define ll long long
#define N 2000010
 
template <class T,class U>inline void Max(T &a,U b){if(a<b)a=b;}
template <class T,class U>inline void Min(T &a,U b){if(a>b)a=b;}
 
//FILE* outFile;
 
inline void add(int &a,int b){a+=b;while(a>=mod)a-=mod;}
 
int pow(int a,int b){
    int ans=1;
    while(b){
        if(b&1)ans=ans*(ll)a%mod;
        a=(ll)a*a%mod;b>>=1;
    }
    return ans;
}

char s[1005];
vi v[26];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,ca=0,m,i,j,k,n;
    scanf("%d",&T);
    while(T--){
        printf("Case #%d: ",++ca);
        scanf("%s",s);
        n=strlen(s);
        rep(i,0,26)v[i].clear();
        rep(i,0,n)v[s[i]-'A'].pb(i);
        int last=n;
        string ans="",res="";
        per(i,0,26){
            while(!v[i].empty()){
                int y=v[i].back();v[i].pop_back();
                if(y>=last){
                    continue;
                }
                per(j,y+1,last)ans+=s[j];
                res+=s[y];
                last=y;
            }
        }
        reverse(all(ans));
        res=res+ans;
        printf("%s\n",res.c_str());
    }
    return 0;
}