#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;
typedef long long ll;
char str[15][3][10020];
int T,t,n,m;
int num[3],point[3],num2[3];
int dp[15][10300];
bool flag;
bool check(int pos){
    int i,j,k;
    //printf("ok\n");
    memset(num2,0,sizeof(num2));
    for(i=0;i<(1<<n);i++)
        if(str[n][pos][i]=='R')
            num2[0]++;
        else if(str[n][pos][i]=='P')
            num2[1]++;
        else if(str[n][pos][i]=='S')
            num2[2]++;
    if(num[0]==num2[0] && num[1]==num2[1] && num[2]==num2[2]){
        printf("%s\n",str[n][pos]);
        flag=1;
        return 1;
    }
    return 0;

}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k,b;
    scanf("%d",&T);
    point[0]=2;
    point[1]=0;
    point[2]=1;
    str[0][0][0]='R';
    str[0][1][0]='P';
    str[0][2][0]='S';
    for(i=0;i<=11;i++){
        for(j=0;j<=2;j++){
            b=point[j];
            if(strcmp(str[i][j],str[i][b])<0){
                strcat(str[i+1][j],str[i][j]);
                strcat(str[i+1][j],str[i][b]);
            }
            else{
                strcat(str[i+1][j],str[i][b]);
                strcat(str[i+1][j],str[i][j]);
            }
        }
    }
    //for(i=0;i<3;i++)
    //    printf("%s\n",str[2][i]);
    for(t=1;t<=T;t++){
        scanf("%d%d%d%d",&n,&num[0],&num[1],&num[2]);
        printf("Case #%d: ",t);
        flag=0;
        for(i=0;i<3;i++)
            if(check(i))
               break;
        if(!flag)
            printf("IMPOSSIBLE\n");
    }
}
