#include <cstdio>

using namespace std;

int T,l,x,len;
char s[10008],pre[10008],suf[10008],M[128][128];
bool NEG[128][128]={0},pneg[10008],sneg[10008];

inline bool ima() {
    char mid;
    bool mneg;
    for (int i=0; i<len-2; i++) {
        if (pre[i]!='i' || pneg[i]) continue;
        mid='1';
        mneg=0;
        for (int j=i+1; j<len-1; j++) {
            mneg=mneg^NEG[mid][s[j]];
            mid=M[mid][s[j]];
            if (mid=='j' && !mneg && suf[j+1]=='k' && !sneg[j+1]) return 1;
        }
    }
    return 0;
}

int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);

    M['1']['1']='1';
    M['1']['i']='i';
    M['1']['j']='j';
    M['1']['k']='k';

    M['i']['1']='i';
    M['i']['i']='1'; NEG['i']['i']=1;
    M['i']['j']='k';
    M['i']['k']='j'; NEG['i']['k']=1;

    M['j']['1']='j';
    M['j']['i']='k'; NEG['j']['i']=1;
    M['j']['j']='1'; NEG['j']['j']=1;
    M['j']['k']='i';

    M['k']['1']='k';
    M['k']['i']='j';
    M['k']['j']='i'; NEG['k']['j']=1;
    M['k']['k']='1'; NEG['k']['k']=1;

    scanf("%d",&T);
    for (int t=1; t<=T; t++) {
        scanf("%d %d",&l,&x);
        scanf("%s",s);
        len=l*x;
        for (int i=l; i<len; i++) s[i]=s[i%l];

        pre[0]=s[0];
        pneg[0]=0;
        for (int i=1; i<len; i++) {
            pre[i]=M[pre[i-1]][s[i]];
            pneg[i]=pneg[i-1]^NEG[pre[i-1]][s[i]];
        }

        suf[len-1]=s[len-1];
        sneg[len-1]=0;
        for (int i=len-2; i>=0; i--) {
            suf[i]=M[s[i]][suf[i+1]];
            sneg[i]=NEG[s[i]][suf[i+1]]^sneg[i+1];
        }

        if (ima()) printf("Case #%d: YES\n",t);
        else printf("Case #%d: NO\n",t);
    }

    return 0;
}
