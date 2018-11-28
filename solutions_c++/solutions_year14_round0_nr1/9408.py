#include <iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int a[4][4],b[4][4];
    int T;
    scanf("%d",&T);
    int m,n;
    int t=1;
    while(t<=T){
        scanf("%d",&m);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&a[i][j]);
        scanf("%d",&n);
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                scanf("%d",&b[i][j]);
        int cnt=0,num=0;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(a[m-1][i]==b[n-1][j]){
                cnt++;
                num=a[m-1][i];
            }
        printf("Case #%d: ",t);
        if(cnt==0) printf("Volunteer cheated!\n");
        if(cnt==1) printf("%d\n",num);
        if(cnt>1) printf("Bad magician!\n");
        t++;
    }
    return 0;

}
