#include <bits/stdc++.h>
#define snd(a) scanf("%d",&(a))
#define snlld(a) scanf("%lld",&(a))
#define rep(i,n) for((i)=0;(i)<(n);(i)+=1)
#define reps(i,s,n) for((i)=(s);(i)<(n);(i)+=1)
#define tr(container,it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define pb push_back
#define pf push_front
#define all(a) (a).begin(),(a).end()
#define rall(a) (a).rbegin(),(a).rend()
#define fill(a,v) memset((a),(v),sizeof(a))
#define sz size()
#define mp make_pair
#define mod  1000000007
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
template<class T> inline T poww(T b,T p){ll a=1;while(p){if(p&1){a=(a*b);}p>>=1;b=(b*b);}return a;}
template<class T> inline T poww2(T b,int p){T a=1;while(p){if(p&1){a=(a*b);}p>>=1;b=(b*b);}return a;}
template<class T> inline T modpoww(T b,T p,T mmod){if(p==0&&b==0)return 0;ll a=1;while(p){if(p&1){a=(a*b)%mmod;}p>>=1;b=(b*b)%mmod;}return a%mmod;}
template<class T>  inline T gcd(T a,T b){ if(b>a)return gcd(b,a);return ((b==0)?a:gcd(b,a%b));}
inline void scand(vector<int>& a,int n){int b;int i; rep(i,n){snd(b);a.pb(b);}}
template<class T> inline void scan(vector<T>& a,int n){T b;int i; rep(i,n){cin>>b;a.pb(b);}}
#define pii pair<int,int>
#define vpii vector<pii >
#define vi vector<int>
#define vvi vector<vi >
#define vl vector<long long>
#define fr first
#define sd second


int mul(int a, int b){
    int sgna=1,sgnb=1;
    if(a<0)sgna=-1;
    if(b<0)sgnb=-1;
    a=abs(a);
    b=abs(b);
    if(a==1){
        return b*sgna*sgnb;
    }
    else if(a==2){
        if(b==1)return a*sgna*sgnb;
        else if(b==2)return -1*sgna*sgnb;
        else if(b==3)return 4*sgna*sgnb;
        else if(b==4)return -3*sgna*sgnb;
    }
    else if(a==3){
        if(b==1)return a*sgna*sgnb;
        else if(b==2)return -4*sgna*sgnb;
        else if(b==3)return -1*sgna*sgnb;
        else if(b==4)return 2*sgna*sgnb;
    }
    else if(a==4){
        if(b==1)return a*sgna*sgnb;
        else if(b==2)return 3*sgna*sgnb;
        else if(b==3)return -2*sgna*sgnb;
        else if(b==4)return -1*sgna*sgnb;
    }

}
int fi[10010];
int bk[10010];
int main(){
    int i,j,k,t;
    snd(t);
    int tt;
    rep(tt,t){
       int l,x;
       string str,s="";
       cin>>l>>x;
       cin>>str;
       vi a;
       rep(i,x){
        rep(j,str.sz){
            if(str[j]=='i')a.pb(2);
            else if(str[j]=='j')a.pb(3);
            else if(str[j]=='k')a.pb(4);
        }
       }

    //   rep(i,l*x)cout<<a[i]<<" ";cout<<"\n";
       fill(fi,0);
       fill(bk,0);
       int p=1;
       rep(i,a.sz){
         p=mul(p,a[i]);
        // cout<<"p=" <<p<<"\n";
         if(p==2)fi[i]=1;
       }
       p=1;
       for(j=a.sz-1;j>=0;j--){
            p=mul(a[j],p);
           // cout<<"p="<<p<<" ";
            if(p==4)bk[j]=1;
        }
        //cout<<"::\n";

       // rep(i,a.sz)cout<<fi[i]<<" ";cout<<" --fi\n";
       // rep(i,a.sz)cout<<bk[i]<<" ";cout<<" --bk\n";

        int fo=0;
        rep(i,a.sz){
            if(fi[i]){
                p=1;
                reps(j,i+1,a.sz-1){
                    p=mul(p,a[j]);
                    if(p==3&&bk[j+1]){
                        fo=1;
                        break;
                    }
                }
            }
            if(fo)break;
        }

        printf("Case #%d: %s\n",tt+1,(fo?"YES":"NO"));
    }
}





























