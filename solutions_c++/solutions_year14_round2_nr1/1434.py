#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;
char simp[101][101];
char s[101][101];
int num[101][101];
FILE *fp;
int abs(int n);
void clear(int n);
int mid(int k,int n);

int main(){
    int t,n,ri,i,j,top,flag,count,ans,m;
    fp=fopen("a.txt","w");
    scanf("%d",&t);
    for (ri=1;ri<=t;ri++){
        clear(n);
        scanf("%d",&n);
        for (i=1;i<=n;i++){
            top=0;
            scanf("%s",s[i]);
            simp[i][0]=s[i][0];
            count=1;
            for (j=1;j<strlen(s[i]);j++)
                if (s[i][j]!=s[i][j-1]){
                   simp[i][++top]=s[i][j];
                   num[i][top]=count;
                   count=1;
                }
                else count++;
            num[i][top+1]=count;
            /*for (j=0;j<=top+2;j++)
                printf("%c",simp[i][j]);
            printf("\n");*/
        }
        
        flag=1;
        fprintf(fp,"Case #%d: ",ri);
        for (i=2;i<=n;i++)
            if (strcmp(simp[i-1],simp[i])!=0){
               //fprintf(fp,"Fegla Won\n");
               //fprintf(fp,"%d\n",i);
               flag=0;
            }
        ans=0;
        if (flag){
           for (i=1;i<=top+1;i++){
               m=mid(i,n);
               for (j=1;j<=n;j++)
                   ans+=abs(num[j][i]-m);
           }
           fprintf(fp,"%d\n",ans);
        }    
        else fprintf(fp,"Fegla Won\n");    
    }
    return 0;
}

int abs(int n){
    if (n>=0) return n;
    return -n;
}

void clear(int n){
     int i,j;
     for (i=1;i<=n;i++)
     for (j=0;j<=100;j++){
         s[i][j]='\0';
         simp[i][j]='\0';
         num[i][j]=0;
     }
}

int mid(int k,int n){
    int temp[101];
    int i;
    for (i=1;i<=n;i++)
        temp[i-1]=num[i][k];
    sort(temp,temp+n);
    return temp[n/2];
}
