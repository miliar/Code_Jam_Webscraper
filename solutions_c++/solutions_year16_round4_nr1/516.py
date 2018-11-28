#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/hash_policy.hpp>
#define f first
#define s second
using namespace std;
using namespace __gnu_pbds;
typedef pair<int,int>par;
typedef pair<int,int>par;
typedef pair<int,par>pr;
map<par,pr>mp;
pr F(int n,int x){
    if(mp.find(par(n,x))!=mp.end())return mp[par(n,x)];
    int ar[3]={0};
    if(!n){
        ar[x]=1;
        }
    else{
        pr a=F(n-1,x);
        pr b=F(n-1,(x+1)%3);
        ar[0]=a.f+b.f;
        ar[1]=a.s.f+b.s.f;
        ar[2]=a.s.s+b.s.s;
        }
    auto ret=pr(ar[0],par(ar[1],ar[2]));
    mp[par(n,x)]=ret;
    //printf("~%d %d %d %d %d\n",n,x,ar[0],ar[1],ar[2]);
    return ret;
    }
void G(int n,int x){
    //printf("%d %d\n",n,x);
    if(!n){
        if(x==0)putchar('P');
        if(x==1)putchar('R');
        if(x==2)putchar('S');
        }
    else{
        pr a=F(n-1,x);
        pr b=F(n-1,(x+1)%3);
        if(a>b)
            G(n-1,x),G(n-1,(x+1)%3);
        else
            G(n-1,(x+1)%3),G(n-1,x);
        }
    }
int main() {
    int T;
    scanf("%d",&T);
    int t=0;
    while(T--){t++;
        int n,r,p,s;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        int ar[3]={0};
        pr x=F(n,0);
        ar[0]=x.f;
        ar[1]=x.s.f;
        ar[2]=x.s.s;
        //printf("%d %d %d\n",ar[0],ar[1],ar[2]);
        printf("Case #%d: ",t);
        if(ar[0]==p&&ar[1]==r&&ar[2]==s){
            G(n,0);puts("");
            }
        else if(ar[2]==p&&ar[0]==r&&ar[1]==s){
            G(n,1);puts("");
            }
        else if(ar[1]==p&&ar[2]==r&&ar[0]==s){
            G(n,2);puts("");
            }
        else{
            puts("IMPOSSIBLE");
            }
        }
    return 0;
    }


//15005 2
//20005 5
//25005 9
//30005 13
//35005 20
//40005 27
//45005 36
