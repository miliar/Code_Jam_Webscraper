#include<cstdio>
#include<cstring>

using namespace std;

int main(){
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A-small-attempt4.txt","w",stdout);
    int t,r,num[20],n,ans;
    scanf("%d",&t);
    for(int kase=1; kase<=t; kase++){
        memset(num,0,sizeof(num));

        scanf("%d",&r);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++){
                 scanf("%d",&n);
                 if(r==i)num[n]++;
            }

        scanf("%d",&r);
        for(int i=1; i<=4; i++)
            for(int j=1; j<=4; j++){
                 scanf("%d",&n);
                 if(r==i)num[n]++;
            }

        int flag=0;
        for(int i=1; i<=16; i++){
             if(!flag&&num[i]==2){
                 flag=1;
                 ans = i;
             }
             else if(num[i]==2){
                 flag=2;
             }
        }
        switch(flag){
             case 0:
                  printf("Case #%d: Volunteer cheated!\n",kase);
                  break;
             case 1:
                  printf("Case #%d: %d\n",kase,ans);
                  break;
             case 2:
                  printf("Case #%d: Bad magician!\n",kase);
                  break;
        }
    }
    return 0;
}
