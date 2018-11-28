#include<cstdio>
#include<string.h>
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int allt,nowt=0;
    scanf("%d",&allt);
    while(++nowt <= allt){
        char pan[105];
        scanf("%s",pan);
        //printf("%s\n",pan);
        int stat[105]={},len = strlen(pan),cnt=0;
        for(int i=len-1;i>=0;--i){
            stat[i] += stat[i+1];
            if(pan[i] == '-' && stat[i]%2 == 0){
                stat[i]++;
                cnt++;
            }
            else if(pan[i] == '+' && stat[i] %2 == 1){
                stat[i]++;
                cnt++;
            }
        }
        printf("Case #%d: %d\n",nowt,cnt);
    }
    return 0;
}
