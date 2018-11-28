#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a[1002];
    int ra[1002];
   freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    scanf("%d",&t);
    int smax;
    for(int i=1;i<=t;i++){
            memset(a,0,sizeof a);
            memset(ra,0,sizeof ra);
        cin >> smax;
        string str;
        cin >> str;

    for(int j=0;j<=smax;j++)
        a[j]=str[j]-'0';

    int tot=0;
    ra[0]=a[0];
    for(int j=1;j<=smax;j++){
       ra[j]=ra[j-1]+a[j];
       if(ra[j-1]<j && a[j]>0){
        tot=tot+ (j-ra[j-1]);
        ra[j]=ra[j] + (j-ra[j-1]);
       }
    }
    printf("Case #%d: %d\n",i,tot);

    }
    return 0;
}
