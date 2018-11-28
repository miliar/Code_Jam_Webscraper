#include "stdio.h"
#include "iostream"
using namespace std;
int main(){
    int t;
    freopen("A-large(1).in","r",stdin);
    freopen("a-large.out","w",stdout);
    scanf("%d",&t);
    for(int l=1;l<=t;l++){
        string d;
        int p,hashx[26]={},num[10]={};
        cin>>d;
        for(int i=0;i<d.length();i++) hashx[d[i]-'A']++;

        p=hashx['Z'-'A'];
        num[0]+=p;
        hashx['Z'-'A']-=p,hashx['E'-'A']-=p,hashx['R'-'A']-=p,hashx['O'-'A']-=p;

        p=hashx['W'-'A'];
        num[2]+=p;
        hashx['T'-'A']-=p,hashx['W'-'A']-=p,hashx['O'-'A']-=p;

        p=hashx['U'-'A'];
        num[4]+=p;
        hashx['F'-'A']-=p,hashx['O'-'A']-=p,hashx['U'-'A']-=p,hashx['R'-'A']-=p;

        p=hashx['X'-'A'];
        num[6]+=p;
        hashx['S'-'A']-=p,hashx['I'-'A']-=p,hashx['X'-'A']-=p;

        p=hashx['G'-'A'];
        num[8]+=p;
        hashx['E'-'A']-=p,hashx['I'-'A']-=p,hashx['G'-'A']-=p,hashx['H'-'A']-=p,hashx['T'-'A']-=p;

        p=hashx['O'-'A'];
        num[1]+=p;
        hashx['O'-'A']-=p,hashx['N'-'A']-=p,hashx['E'-'A']-=p;

        p=hashx['R'-'A'];
        num[3]+=p;
        hashx['T'-'A']-=p,hashx['H'-'A']-=p,hashx['R'-'A']-=p,hashx['E'-'A']-=p,hashx['E'-'A']-=p;

        p=hashx['F'-'A'];
        num[5]+=p;
        hashx['F'-'A']-=p,hashx['I'-'A']-=p,hashx['V'-'A']-=p,hashx['E'-'A']-=p;

        p=hashx['S'-'A'];
        num[7]+=p;
        hashx['S'-'A']-=p,hashx['E'-'A']-=p,hashx['V'-'A']-=p,hashx['E'-'A']-=p,hashx['N'-'A']-=p;

        p=hashx['I'-'A'];
        num[9]+=p;
        hashx['N'-'A']-=p,hashx['I'-'A']-=p,hashx['N'-'A']-=p,hashx['E'-'A']-=p;

        printf("Case #%d: ",l);
        for(int i=0;i<10;i++){
            for(int j=0;j<num[i];j++) printf("%d",i);
        }
        printf("\n");
    }
}
