#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<stack>
#include<queue>
#include<list>
#include<bitset>
#include<map>
//Template V1
#define nl printf("\n")
#define in(x) scanf("%d",&x)
#define out(x) printf("%d",x)
#define inll(x) scanf("%lld",&x)
#define outll(x) printf("%lld",x)
#define inc(x) scanf("%c",&x)
#define outc(x) printf(x)
#define ins(x) scanf("%s",&x)
#define outs(x) printf("%s",x)
#define loop(var,x,y) for(int var=x;var<y;var++)
#define rloop(var,x,y) for(int var=x-1;var>=y;var--)
#define cins(x) cin>>x
#define couts(x) cout<<x
#define reset(x,y) memset(x,y,sizeof(x));
#define stop fflush(stdin);getchar()
#define push_back PB
#define GOD using
#define BLESS namespace
#define YOU std;

GOD BLESS YOU

typedef long long ll;
typedef vector<int> vi;


inline void OPEN(const string &s) {
freopen((s + ".in").c_str(), "r", stdin);
freopen((s + ".out").c_str(), "w", stdout);
}

int main(){
   OPEN("BL");
int T;in(T);
int kasus=1;
    while(T--){
               double  C,F,X;
               scanf("%lf %lf %lf",&C,&F,&X);
               
               double min=(X/2.0);
               
               double t1=2.0;
               double t2=0.0;
               double t3=0.0;
               
               while(1){
                       
                        t2+=(C/t1);
                        
                        double tmp=(t2+(X/(t1+F)));
                        if(min>tmp){
                          min=tmp;
                          t1=t1+F;
                        }
                        else{
                             break;
                        }
               }
               
               printf("Case #%d: %.7lf\n",kasus++,min);
    }
}
