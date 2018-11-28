#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
char s[2005];
int a[30];
int ans[30];
int main(){
    int t;
    freopen("A-large.in","r",stdin);
    freopen("Aoutput.txt","w",stdout);
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++){
        scanf("%s",s);
        int n=strlen(s);
        for(int i=0;i<30;i++){
            a[i]=0;
        }
        for(int i=0;i<n;i++){
            a[s[i]-'A']++;
        }
        ans[0]=a['Z'-'A'];
        ans[2]=a['W'-'A'];
        ans[4]=a['U'-'A'];
        ans[6]=a['X'-'A'];
        ans[8]=a['G'-'A'];
        a['Z'-'A']-=ans[0]; a['E'-'A']-=ans[0]; a['R'-'A']-=ans[0]; a['O'-'A']-=ans[0];
        a['T'-'A']-=ans[2]; a['W'-'A']-=ans[2]; a['O'-'A']-=ans[2];
        a['F'-'A']-=ans[4]; a['O'-'A']-=ans[4]; a['U'-'A']-=ans[4]; a['R'-'A']-=ans[4];
        a['S'-'A']-=ans[6]; a['I'-'A']-=ans[6]; a['X'-'A']-=ans[6];
        a['E'-'A']-=ans[8]; a['I'-'A']-=ans[8]; a['G'-'A']-=ans[8]; a['H'-'A']-=ans[8]; a['T'-'A']-=ans[8];
        ans[1]=a['O'-'A'];
        ans[3]=a['R'-'A'];
        ans[5]=a['F'-'A'];
        ans[7]=a['S'-'A'];
        ans[9]=a['I'-'A']-ans[5];
        printf("Case #%d: ",tc);
        for(int i=0;i<10;i++){
            for(int j=0;j<ans[i];j++){
                printf("%d",i);
            }
        }
        printf("\n");
    }
}
