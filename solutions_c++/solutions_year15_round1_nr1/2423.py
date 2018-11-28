//Problem A
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<stack>
#include<utility>
#include<cstring>
#include<string>
#define ll long long
#define OO (int)2e9
#define INF (ll)2e17
#define pb push_back
#define mp make_pair
#define rep(x,a,b,c) for(int x=a;x<=b;x+=c)
#define repp(x,a,b) rep(x,a,b,1)
#define rev(x,a,b,c) for(int x=a;x>=b;x-=c)
#define revv(x,a,b) rev(x,a,b,1)
using namespace std;

int t,n,a,m,p,ra,rb;
int d[1005]={};

int main(){
    scanf("%d",&t);
    repp(x,1,t){
        scanf("%d",&n);
        p=1;
        a=m=ra=rb=0;
        repp(y,1,n){
            scanf("%d",&d[y]);
            a=d[y-1]-d[y];
            if(a>0)ra+=a;
            m=max(m,a);
        }
        repp(y,1,n-1){
            if(m>d[y])rb+=d[y];
            else rb+=m;
        }
        printf("Case #%d: %d %d\n",x,ra,rb);
    }
//    system("pause");
    return 0;
}
