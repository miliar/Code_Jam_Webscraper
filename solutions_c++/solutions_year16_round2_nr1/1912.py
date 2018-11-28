#include<stdio.h>
#include<string.h>
char str[10010];
int cnt[300], num_cnt[20];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i, j, tt, T;
    scanf("%d", &T);
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%s", str);
        for(i='A'; i<='Z'; ++i) cnt[i]=NULL;
        for(i=0; i<10; ++i) num_cnt[i]=0;
        for(i=0; i<strlen(str); ++i)
        {
            ++cnt[str[i]];
        }
        num_cnt[0]=cnt['Z'];
        cnt['E']-=cnt['Z'];
        cnt['R']-=cnt['Z'];
        cnt['O']-=cnt['Z'];
        cnt['Z']=0;
        num_cnt[2]=cnt['W'];
        cnt['T']-=cnt['W'];
        cnt['O']-=cnt['W'];
        cnt['W']=0;
        num_cnt[6]=cnt['X'];
        cnt['S']-=cnt['X'];
        cnt['I']-=cnt['X'];
        cnt['X']=0;
        num_cnt[4]=cnt['U'];
        cnt['F']-=cnt['U'];
        cnt['O']-=cnt['U'];
        cnt['R']-=cnt['U'];
        cnt['U']=0;
        num_cnt[5]=cnt['F'];
        cnt['I']-=cnt['F'];
        cnt['V']-=cnt['F'];
        cnt['E']-=cnt['F'];
        cnt['F']=0;
        num_cnt[7]=cnt['V'];
        cnt['S']-=cnt['V'];
        cnt['E']-=cnt['V'];
        cnt['E']-=cnt['V'];
        cnt['N']-=cnt['V'];
        cnt['V']=0;
        num_cnt[3]=cnt['R'];
        cnt['T']-=cnt['R'];
        cnt['H']-=cnt['R'];
        cnt['E']-=cnt['R'];
        cnt['E']-=cnt['R'];
        cnt['R']=0;
        num_cnt[1]=cnt['O'];
        cnt['N']-=cnt['O'];
        cnt['E']-=cnt['O'];
        cnt['O']=0;
        num_cnt[8]=cnt['G'];
        cnt['E']-=cnt['G'];
        cnt['I']-=cnt['G'];
        cnt['H']-=cnt['G'];
        cnt['T']-=cnt['G'];
        cnt['G']=0;
        num_cnt[9]=cnt['I'];
        printf("Case #%d: ", tt);
        for(i=0; i<=9; ++i)
        {
            for(j=1; j<=num_cnt[i]; ++j) printf("%d", i);
        }
        printf("\n");
    }
}
