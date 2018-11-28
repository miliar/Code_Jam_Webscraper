#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("a.txt","r",stdin);
    //freopen("b.txt","w",stdout);
    int t,i,j,visit[17],cas=1;
    scanf("%d",&t);
    while(t--){
        int r,tmp;
        memset(visit,0,sizeof(visit));
        scanf("%d",&r);
        for(i=0;i<16;i++){
            scanf("%d",&tmp);
            if(i/4+1==r)  visit[tmp]++;
        }
        scanf("%d",&r);
        for(i=0;i<16;i++){
            scanf("%d",&tmp);
            if(i/4+1==r)  visit[tmp]++;
        }
        int cnt=0,ti;
        for(i=1;i<=16;i++){
            if(visit[i])  cnt++;
            if(visit[i]==2)  ti=i;
        }
        if(cnt==8)  {printf("Case #%d: Volunteer cheated!\n",cas++);continue;}
        if(cnt==7)  {printf("Case #%d: %d\n",cas++,ti);continue;}
        else  printf("Case #%d: Bad magician!\n",cas++);
    }
    return 0;
}
