#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<string>
#include<bitset>
#define LL long long

const int MAXN=0;
const int MAXM=0;
const long long LLINF=9000000000000000000;
const int INF=2147483647;//careful because of floyed and so on
const int MOD=1000000007;
double eps=0.00000001;

using namespace std;

int T;
char s[2007];
int cnt_ch[26],cnt_nb[10];

void g_clear(){
    memset(cnt_ch,0,sizeof(cnt_ch));
    memset(cnt_nb,0,sizeof(cnt_nb));
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
            g_clear();
            scanf("%s",s+1);
            int len=strlen(s+1);
            for (int i=1;i<=len;i++){
                    cnt_ch[s[i]-'A']++;
            }
            cnt_nb[0]=cnt_ch['Z'-'A'];
            cnt_ch['Z'-'A']-=cnt_nb[0];
            cnt_ch['E'-'A']-=cnt_nb[0];
            cnt_ch['R'-'A']-=cnt_nb[0];
            cnt_ch['O'-'A']-=cnt_nb[0];
            cnt_nb[8]=cnt_ch['G'-'A'];
            cnt_ch['E'-'A']-=cnt_nb[8];
            cnt_ch['I'-'A']-=cnt_nb[8];
            cnt_ch['G'-'A']-=cnt_nb[8];
            cnt_ch['H'-'A']-=cnt_nb[8];
            cnt_ch['T'-'A']-=cnt_nb[8];
            cnt_nb[3]=cnt_ch['H'-'A'];
            cnt_ch['T'-'A']-=cnt_nb[3];
            cnt_ch['H'-'A']-=cnt_nb[3];
            cnt_ch['R'-'A']-=cnt_nb[3];
            cnt_ch['E'-'A']-=cnt_nb[3];
            cnt_ch['E'-'A']-=cnt_nb[3];
            cnt_nb[6]=cnt_ch['X'-'A'];
            cnt_ch['S'-'A']-=cnt_nb[6];
            cnt_ch['I'-'A']-=cnt_nb[6];
            cnt_ch['X'-'A']-=cnt_nb[6];
            cnt_nb[7]=cnt_ch['S'-'A'];
            cnt_ch['S'-'A']-=cnt_nb[7];
            cnt_ch['E'-'A']-=cnt_nb[7];
            cnt_ch['V'-'A']-=cnt_nb[7];
            cnt_ch['E'-'A']-=cnt_nb[7];
            cnt_ch['N'-'A']-=cnt_nb[7];
            cnt_nb[2]=cnt_ch['T'-'A'];
            cnt_ch['T'-'A']-=cnt_nb[2];
            cnt_ch['W'-'A']-=cnt_nb[2];
            cnt_ch['O'-'A']-=cnt_nb[2];
            cnt_nb[4]=cnt_ch['R'-'A'];
            cnt_ch['F'-'A']-=cnt_nb[4];
            cnt_ch['O'-'A']-=cnt_nb[4];
            cnt_ch['U'-'A']-=cnt_nb[4];
            cnt_ch['R'-'A']-=cnt_nb[4];
            cnt_nb[5]=cnt_ch['F'-'A'];
            cnt_ch['F'-'A']-=cnt_nb[5];
            cnt_ch['I'-'A']-=cnt_nb[5];
            cnt_ch['V'-'A']-=cnt_nb[5];
            cnt_ch['E'-'A']-=cnt_nb[5];
            cnt_nb[1]=cnt_ch['O'-'A'];
            cnt_ch['O'-'A']-=cnt_nb[1];
            cnt_ch['N'-'A']-=cnt_nb[1];
            cnt_ch['E'-'A']-=cnt_nb[1];
            cnt_nb[9]=cnt_ch['N'-'A']/2;
            cnt_ch['N'-'A']-=cnt_nb[9];
            cnt_ch['I'-'A']-=cnt_nb[9];
            cnt_ch['N'-'A']-=cnt_nb[9];
            cnt_ch['E'-'A']-=cnt_nb[9];
            printf("Case #%d: ",cas);
            /*printf("\n");
            for (int i=0;i<26;i++){
                    if (cnt_ch[i]!=0) printf("%c%d ",'A'+i,cnt_ch[i]);
            }
            printf("\n");*/
            for (int i=0;i<10;i++){
                    while (cnt_nb[i]!=0){
                            printf("%d",i);
                            cnt_nb[i]--;
                    }
            }
            printf("\n");
    }
    return 0;
}
/*
4
OZONETOWER
WEIGHFOXTOURIST
OURNEONFOE
ETHER

1
ONEONEONEONENINE
*/
