#include<cstdio>
#include<algorithm>
using namespace std;
int i,j,t,mx,n[105],tc[105][1005],d[105][1005];

int pancake(int curtime) {
    int ti,temp,temp2=0x7fffffff;
    if(curtime>mx)return 0x7fffffff;
    for(ti=mx;ti;ti--)
        if(d[i][ti]){temp=ti;break;}
    for(ti=1;ti<=temp/2;ti++) {
        d[i][temp]--;
        d[i][temp-ti]++;
        d[i][ti]++;
        temp2=min(temp2,pancake(curtime+1));
        d[i][ti]--;
        d[i][temp-ti]--;
        d[i][temp]++;
    }
    return min(temp2,curtime+temp);
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(i=0;i<t;i++) {
        scanf("%d",&n[i]);
        for(j=0;j<n[i];j++) {
            scanf("%d",&tc[i][j]);
            if(mx<tc[i][j])mx=tc[i][j];
            d[i][tc[i][j]]++;
        }
        printf("Case #%d: %d\n",i+1,pancake(0));
        mx=0;
    }
}
