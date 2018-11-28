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


int i,t,n,k,m,x,y,a[1007],b[100],j,con,r,minm=1005,maks,poin;
long long int tmp;


int main(){
    string s[6], ss;
    int ar[100]={1,2,3,11,22};
    scanf("%d",&n);
    rep(0,n,1){
        tmp=0;
        scanf("%d%d",&x,&y);
        printf("Case #%d: ",i+1);
        rep2(0,12,1){
            if(ar[j]*ar[j]>=x&&ar[j]*ar[j]<=y)
                tmp++;
        }
        ot(tmp);
    }
    return 0;
}

/*
1 1 1 2 3 3 4
1 2 1 3 1 3 4
9
1 1 1 1 1 2 3 3 3
*/
