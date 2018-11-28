#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

bool sip;
int A[10005], casos, x, y, mid, ctos, cap, emp, ter;

int main()
{
    freopen("ji.in","r",stdin);
    freopen("jo.out","w",stdout);
    scanf("%d",&casos);
    for(int v=1; v<=casos; v++){
        scanf("%d%d",&ctos,&cap);
        for(int i=1; i<=ctos; i++)
            scanf("%d",&A[i]);
        sort(A+1, A+ctos+1);
        x= ctos%2==0 ? ctos/2 : ctos/2+1;
        y=ctos;
        while(x<y){
            mid=(x+y)/2;
            sip=true;
            emp=ctos-(mid-(ctos-mid));
            ter=1;
            while(ter<emp){
                if(A[ter]+A[emp]>cap){
                    sip=false;
                    break;
                }
                ++ter;
                --emp;
            }
            if(sip){
                y=mid;
            }
            else
                x=mid+1;
        }
        printf("Case #%d: %d\n",v,x);
    }
    return 0;
}
