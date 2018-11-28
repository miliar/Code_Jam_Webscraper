#include<cstdio>
#include<cstring>

char s[110];

int main () {
//freopen("B-large.in","r",stdin);
//freopen("out.txt","w",stdout);
    int t,tt,sum,i,j,l;
    scanf("%d",&tt);
    for (t=1;t<=tt;t++) {
        scanf("%s",s);
        sum=0;
        l=strlen(s);
        s[l]='+';
        for (i=1;i<=l;i++) if (s[i]!=s[i-1]) sum++;
        printf("Case #%d: %d\n",t,sum);
    }
    return 0;
}
