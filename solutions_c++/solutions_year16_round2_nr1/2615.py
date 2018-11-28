
#include <bits/stdc++.h>

using namespace std;

#define REP(a,b) for(int a=0;a<(b);a++)
#define PER(a,b) for(int a=(b)-1;a>=0;a--)
#define DEBUG(...) fprintf(stderr,__VA_ARGS__)

typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;

////////////////////////////////////////////////

int T;
int mapp[256],n[10];
char str[2001];

int main(){
    scanf("%d",&T);
    REP(cas,T){
        REP(i,255)
            mapp[i]=0;
        scanf("%s",str);
        REP(i,strlen(str))
            mapp[str[i]]++;
        printf("Case #%d: ",cas+1);
        n[0]=mapp['Z'];
        n[4]=mapp['U'];
        n[2]=mapp['W'];
        n[1]=mapp['O']-n[0]-n[2]-n[4];
        n[3]=mapp['R']-n[0]-n[4];
        n[5]=mapp['F']-n[4];
        n[6]=mapp['X'];
        n[7]=mapp['S']-n[6];
        n[8]=mapp['T']-n[2]-n[3];
        n[9]=mapp['I']-n[5]-n[6]-n[8];
        REP(j,10)
            REP(i,n[j])
                printf("%d",j);
        printf("\n");
    }
    return 0;
}

