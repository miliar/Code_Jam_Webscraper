#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
using namespace std;

int cnt[255],ans[20];
char ina[2010];

int main () {
freopen("in.in","r",stdin);
freopen("out.txt","w",stdout);
    string ntos[10];
    int t,tt,l,i;
    ntos[0]="ZERO";
    ntos[1]="ONE";
    ntos[2]="TWO";
    ntos[3]="THREE";
    ntos[4]="FOUR";
    ntos[5]="FIVE";
    ntos[6]="SIX";
    ntos[7]="SEVEN";
    ntos[8]="EIGHT";
    ntos[9]="NINE";

    //for (i=0;i<ntos[1].length();i++) printf("%c",ntos[1][i]);

    scanf("%d",&tt);
    for (t=1;t<=tt;t++) {
        scanf("%s",ina);
        l=strlen(ina);
        memset(cnt,0,sizeof(cnt));
        for (i=0;i<l;i++) cnt[ina[i]]++;
        memset(ans,0,sizeof(ans));

        //ZERO Z
        for (i=0;i<ntos[0].length();i++) if (ntos[0][i]!='Z') {
            cnt[ntos[0][i]]-=cnt['Z'];
        }
        ans[0]+=cnt['Z'];
        cnt['Z']=0;

        //TWO W
        for (i=0;i<ntos[2].length();i++) if (ntos[2][i]!='W') {
            cnt[ntos[2][i]]-=cnt['W'];
        }
        ans[2]+=cnt['W'];
        cnt['W']=0;

        //FOUR U
        for (i=0;i<ntos[4].length();i++) if (ntos[4][i]!='U') {
            cnt[ntos[4][i]]-=cnt['U'];
        }
        ans[4]+=cnt['U'];
        cnt['U']=0;

        //SIX X
        for (i=0;i<ntos[6].length();i++) if (ntos[6][i]!='X') {
            cnt[ntos[6][i]]-=cnt['X'];
        }
        ans[6]+=cnt['X'];
        cnt['X']=0;

        //EIGHT G
        for (i=0;i<ntos[8].length();i++) if (ntos[8][i]!='G') {
            cnt[ntos[8][i]]-=cnt['G'];
        }
        ans[8]+=cnt['G'];
        cnt['G']=0;

        //THREE H
        for (i=0;i<ntos[3].length();i++) if (ntos[3][i]!='H') {
            cnt[ntos[3][i]]-=cnt['H'];
        }
        ans[3]+=cnt['H'];
        cnt['H']=0;

        //SEVEN S
        for (i=0;i<ntos[7].length();i++) if (ntos[7][i]!='S') {
            cnt[ntos[7][i]]-=cnt['S'];
        }
        ans[7]+=cnt['S'];
        cnt['S']=0;

        //FIVE V
        for (i=0;i<ntos[5].length();i++) if (ntos[5][i]!='V') {
            cnt[ntos[5][i]]-=cnt['V'];
        }
        ans[5]+=cnt['V'];
        cnt['V']=0;

        //NINE I
        for (i=0;i<ntos[9].length();i++) if (ntos[9][i]!='I') {
            cnt[ntos[9][i]]-=cnt['I'];
        }
        ans[9]+=cnt['I'];
        cnt['I']=0;

        //ONE
        for (i=0;i<ntos[1].length();i++) if (ntos[1][i]!='O') {
            cnt[ntos[1][i]]-=cnt['O'];
        }
        ans[1]+=cnt['O'];
        cnt['O']=0;

        printf("Case #%d: ",t);
        for (i=1;i<=100;i++) if (cnt[i]) puts("shit!");
        for (i=0;i<=9;i++) {
            for (int j=1;j<=ans[i];j++) printf("%d",i);
        }
        puts("");
    }
    return 0;
}
