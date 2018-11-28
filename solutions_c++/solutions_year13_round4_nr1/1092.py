#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

typedef struct A{
    int x,y;
}AA;
AA a[10005];

int com(const void *aa,const void *bb){
    AA c,d;
    c = *(AA*)(aa);
    d = *(AA*)(bb);
    if(c.x!=d.x)    return c.x>d.x ? 1 : -1;
    return c.y>d.y ? 1 : -1;
}
bool ok(int i,int j){
    if(a[j].x>=a[i].x && a[j].x<=a[i].y && a[j].y>a[i].y)
        return true;
    return false;
}

int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T,t,N,n,M,m,i,j;
    cin >> T;
    for(t=0;t<T;t++){
        cin >> N >> M;
        int all = 0;
        for(m=0;m<M;m++){
            int xx,yy,pp;
            cin >> xx >> yy >> pp;
            for(i=0;i<pp;i++){
                a[all].x = xx;
                a[all].y = yy;
                all++;
            }
        }
        qsort(a,all,sizeof(a[0]),com);
        int ini = 0;
        for(i=0;i<all;i++){
            int gap = a[i].y-a[i].x;
            int tmp = (N+N-(gap-1))*gap/2;
            //printf("%d %d %d\n",gap,tmp,N);
            ini += tmp;
        }
        for(i=0;i<all;i++){
            for(j=i+1;j<all;j++){
                if(ok(i,j)){
                    int tmp = a[i].y;
                    a[i].y = a[j].y;
                    a[j].y = tmp;
                }
            }
        }
        int aft = 0;
        for(i=0;i<all;i++){
            int gap = a[i].y-a[i].x;
            int tmp = (N+N-(gap-1))*gap/2;
            aft += tmp;
        }
        int ans;
        //printf("%d %d\n",ini,aft);
        printf("Case #%d: %d\n",t+1,ini-aft);
    }

    return 0;
}
