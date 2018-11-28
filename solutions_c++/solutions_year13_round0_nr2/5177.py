#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <deque>
using namespace std;
#define ot(x) cout<<x<<endl
#define cen cout<<endl
#define rep(a,b,c) for(i=a;i<b;i+=c)
#define rep2(a,b,c) for(j=a;j<b;j+=c)
#define repi(a,b,c) for(j=a;j>b;j-=c)


int i,t,n,k,m,j,con,r,minm=1005,maks,poin;
long long int tmp,x,y;


int main(){
    scanf("%d\n",&t);
    k=0;int kon,tl;
    y=t;
    while(y--){
        int a[105][105]={0},b[105]={0},total=0;
        scanf("%d%d",&n,&m);
        rep(0,n,1){
            rep2(0,m,1){
                scanf("%d",&a[i][j]);
                if(!b[a[i][j]])total++;
                b[a[i][j]]++;
            }
        }
        tl=0;
        for(int l=0;l<=100;l++){
            if(b[l]!=0){
                kon=1;
                rep(0,n,1){
                    rep2(0,m,1){
                        int tmb=0,tmc=0;
                        if(a[i][j]==l){
                            for(int u=0;u<n;u++)
                                if(a[u][j]<=l)tmb++;
                            for(int u=0;u<m;u++)
                                if(a[i][u]<=l)tmc++;
                            if(tmb!=n && tmc!=m){
                                kon=0;
                                printf("Case #%d: NO\n",k+1);
                                j=m+1;
                                i=n+1;
                                l=101;
                            }
                        }
                    }
                }
                if(kon)
                    tl++;
            }
        }
        if(tl==total)
            printf("Case #%d: YES\n",k+1);
        k++;
    }

    return 0;
}

/*
1 1 1 2 3 3 4
1 2 1 3 1 3 4
9
1 1 1 1 1 2 3 3 3
*/
