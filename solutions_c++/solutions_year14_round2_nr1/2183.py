#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
#include<fstream>
using namespace std;
char str[2][105];
int repeat[2][105],k[2],l[2];
int main()
{
    int ics=0,t,n,i,j,flag,ans;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        memset(repeat,0,sizeof(repeat));
        for(i=0;i<n;i++){
            scanf("%s",str[i]);
        }
        l[0]=strlen(str[0]);
        l[1]=strlen(str[1]);
        for(i=0;i<2;i++){
            repeat[i][0]=1;
            k[i]=0;
            for(j=1;j<l[i];j++){
                if(str[i][j]==str[i][k[i]]){
                    repeat[i][k[i]]++;
                }else {
                    k[i]++;
                    str[i][k[i]]=str[i][j];
                }
            }
        }
        flag=1;
        ans=0;
        printf("Case #%d: ",++ics);
        if(k[0]!=k[1]){
            printf("Fegla Won\n");
            continue;
        }
        for(i=0;i<=k[0];i++){
            if(str[0][i]!=str[1][i]){
                flag=0;
                break;
            }else {
                ans+=abs(repeat[0][i]-repeat[1][i]);
            }
        }
        if(!flag){
            printf("Fegla Won\n");
        }else {
            printf("%d\n",ans);
        }
    }
    return 0;
}
