#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;
int n,m,num,cas;
char x[60][60];
bool work(int res){
    for(int i=2;i<=m;i++){
        if(res/i>=2 && res%i!=1 && (res/i<n || (res/i==n && res%i==0))){
            for(int k=1;k<=n;k++){
                for(int j=1;j<=m;j++){
                    if(k==1&&j==1)printf("c");
                    else if(k<=res/i && j<=i)printf(".");
                    else if(k==res/i+1 && j<=res%i)printf(".");
                    else printf("*");
                }
                printf("\n");
            }
            return true;
        }
    }
    for(int i=2;i<=n;i++){
        if(res/i>=2 && res%i!=1 && (res/i<n || (res/i==m && res%i==0))){
            for(int k=1;k<=n;k++){
                for(int j=1;j<=m;j++){
                    if(k==1&&j==1)printf("c");
                    else if(k<=i && j<=res/i)printf(".");
                    else if(j==res/i+1 && k<=res%i)printf(".");
                    else printf("*");
                }
                printf("\n");
            }
            return true;
        }
    }
    memset(x,0,sizeof(x));
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            if(num>0 && m-j>2){
                x[i][j]='*';
                num--;
            }else if(i+1==n&&j+1==m){
                x[i][j]='c';
            }else {
                x[i][j]='.';
                res--;
            }
        }
    }
    if(num>0)return false;
    else{
        for(int i=0;i<n;i++)
            printf("%s\n",x[i]);
        return true;
    }
}
void solve(int no){
    scanf("%d%d%d",&n,&m,&num);
    int res=n*m-num;
    if(num==0){
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(i==0&&j==0)printf("c");
                else printf(".");
            }
            printf("\n");
        }
    }else if(res==1){
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(i==0&&j==0)printf("c");
                else printf("*");
            }
            printf("\n");
        }
    }else if(n==2 || m==2){
        if(res==2 || res%2==1){
            printf("Impossible\n");
            cas++;
        }else{
            if(n==2){
                printf("c");
                for(int i=2;i<=m;i++){
                    if(i<=res/2)printf(".");
                    else printf("*");
                }
                printf("\n");
                for(int i=1;i<=m;i++){
                    if(i<=res/2)printf(".");
                    else printf("*");
                }
                printf("\n");
            }else{
                printf("c.\n");
                for(int i=2;i<=n;i++){
                    if(i<=res/2)printf("..\n");
                    else printf("**\n");
                }
            }
        }
    }else if(n==1||m==1){
        res--;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(i==1&&j==1)printf("c");
                else if(res>0){
                    res--;
                    printf(".");
                }else printf("*");
            }
            printf("\n");
        }
    }else if(res==2 || res==3 || res==5 || res==7){
        printf("Impossible\n");
        cas++;
    }else{
        bool ok=work(res);
        if(!ok){
            cas++;
            printf("Impossible\n");
        }
    }
    return;
}
int main()
{
    //freopen("C-small-attempt1.in","r",stdin);
    //freopen("out.txt","w",stdout);
    //freopen("out.txt","r",stdin);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d:\n",i);
        solve(i);
    }
    return 0;
}
