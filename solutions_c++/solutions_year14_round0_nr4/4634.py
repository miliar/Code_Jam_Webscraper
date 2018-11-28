#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;
struct P
{
    double x;
    int id;
}no[3000];

bool cmp(P aa, P ab)
{
    return aa.x<ab.x;
}

double a[2000],b[2000];

int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int t,tt,n,i,tans,ans,tem,num;
    scanf("%d",&t);
    tt = 0;
    while(t--){
        tt++;
        scanf("%d",&n);
        num = 0;
        for(i = 1; i <= n; i++){
            scanf("%lf",&a[i]);
            no[num].id = 1;
            no[num++].x = a[i];
        }
        for(i = 1; i <= n; i++){
            scanf("%lf",&b[i]);
            no[num].id = 2;
            no[num++].x = b[i];
        }
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        sort(no,no+num,cmp);
        tans = 0;
        tem = 0;
        for(i = num-1; i >= 0; i--){
            if(no[i].id==2)
                tem++;
            else{
                if(tem>0){
                    tem--;
                    tans++;
                }
            }
        }
        for(i = n; i >= 1; i--)
            if(a[n]>b[i]){
                tem = i;
                break;
            }
        num = 0;
        for(i = 1; i <= tem; i++){
            no[num].x = b[i];
            no[num++].id = 2;
            no[num].x = a[n-i+1];
            no[num++].id = 1;
        }
        sort(no,no+num,cmp);
        tem = 0;
        ans = 0;
        for(i = num-1; i >= 0; i--){
            if(no[i].id==1)
                tem++;
            else{
                if(tem>0){
                    tem--;
                    ans++;
                }
            }
        }
        printf("Case #%d: %d %d\n",tt,ans,n-tans);
    }
    return 0;
}
