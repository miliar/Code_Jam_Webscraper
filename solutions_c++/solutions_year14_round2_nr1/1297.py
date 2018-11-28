/*
  Aditya Gourav
  @adi.pearl
*/
#include<bits/stdc++.h>
using namespace std;

//scanning
#define si(x) scanf("%d",&x)
#define ss(x) scanf("%s",x)
#define ssWSP(x) scanf(" %[^\r\n]",x)
#define sill(x) scanf("%lld",&x)
#define sd(x) scanf("%lf",&x)

//debugging
#define dbm1(msg,x) cerr<<(msg)<<" "<<(x)<<endl;
#define dbm2(msg,x,y) cerr<<(msg)<<" "<<(x)<<" "<<(y)<<endl;
#define dbm3(msg,x,y,z) cerr<<(msg)<<" "<<(x)<<" "<<(y)<<" "<<(z)<<endl;
#define dbm(msg) cerr<<(msg)<<endl;
#define db1(x) cerr<<(x)<<endl;
#define db2(x,y) cerr<<(x)<<" "<<(y)<<endl;
#define db3(x,y,z) cerr<<(x)<<" "<<(y)<<" "<<(z)<<endl;

//others
#define ForInc(var,beg,end) for(int var=beg;var<=end;++var)
#define ForDec(var,end,beg) for(int var=end;var>=beg;--var)
#define F(i,n) ForInc(i,0,n-1)
#define F1(i,n) ForInc(i,1,n)
#define ipArray(arr,size) ForInc(i,0,size-1) si(arr[i]);
#define ipllArray(arr,size) ForInc(i,0,size-1) sill(arr[i]);
#define ii pair<int,int>
#define mp make_pair
#define pb push_back
#define READ(f) freopen(f,"r",stdin);
#define WRITE(f) freopen(f,"w",stdout);
template<typename T> T gcd(T a, T b) { return (b == 0) ? abs(a) : gcd(b, a % b); }
template<typename T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> inline T mod(T a, T b) { return (a % b + b) % b; }
template<typename T> inline T sqr(T x) { return ((x) * (x)); }

const double EPS = 1e-9;
const double BIG = 1e19;
const int INF = INT_MAX;

typedef long long ll;

/* Main Code starts here :) */
struct s{
    char ch;int cnt;
};
struct s2{
    s p[100+10];
    int sz;
}x[100+10];
int n;
inline void func(string a, int idx){
    int sx=0;
    F(i,a.size()){
        int cnt=1;
        while(i<(a.size()-1) && a[i]==a[i+1]){i++;cnt++;}
        x[idx].p[sx].ch=a[i];x[idx].p[sx].cnt=cnt;sx++;
    }
    x[idx].sz=sx;
}
inline int getmin(int i){
    vector<int> v;
    int ret;
    F(j,n)v.pb(x[j].p[i].cnt);
    sort(v.begin(),v.end());
    int mn=v[(n/2)];int op=0;
    F(j,n)op+=abs(v[j]-mn);ret=op;
    if(!(n&1)){
        op=0;
        mn=v[(n/2)-1];
        F(j,n)op+=abs(v[j]-mn);
        ret=min(ret,op);
    }
    return ret;
}
int main(){
    READ("large.in");
    WRITE("large.out");
    int numcases;cin>>numcases;
    string str;
    for(int case_id=1;case_id<=numcases;++case_id){
        cin>>n;
        F(i,n){
            cin>>str;
            func(str,i);
        }
        bool possible=true;
        int ans=0;
        int prev=x[0].sz;   F1(i,n-1)if(x[i].sz!=prev){possible=false;break;}
        if(possible){
            //dbm("in");
            //db1(prev);
            F(i,prev){
                char pr=x[0].p[i].ch;
                F1(j,n-1){
                    if(x[j].p[i].ch!=pr){possible=false;break;}
                }
                if(!possible)break;
                ans+=getmin(i);
            }
        }
        printf("Case #%d: ",case_id);
        if(possible==false)printf("Fegla Won");
        else printf("%d",ans);
        printf("\n");
    }
}
