#include<cstdio>
#include<cstring>
using namespace std;
int T,n,ac,len,k,cnt[200],p,ok,x,avg[200],c;
int abs(int x){
    return ((x>=0)?x:-x);    
}
char s[1000][200],tmp[200];
int main(){
    scanf("%d",&T);
    for (int o=1; o<=T; o++){
        ac=0;
        scanf("%d",&n);
        for (int i=1; i<=n; i++)
            scanf("%s",s[i]);
        len=strlen(s[1]);
        tmp[0]=s[1][0]; k=0;
        for (int i=1; i<len; i++)
            if (s[1][i]!=s[1][i-1]) tmp[++k]=s[1][i];
        for (int i=0; i<=k; i++) cnt[i]=0;
        ok=1;
        for (int i=2; i<=n; i++){
            len=strlen(s[i]); p=-1;
            for (int j=0; j<len; j++){
                if (j==0||s[i][j]!=s[i][j-1]) ++p;
                if (s[i][j]!=tmp[p]) ok=0;
            }
            if (p!=k) ok=0;
        }
        if (ok){
           for (int i=1; i<=n; i++){
               len=strlen(s[i]); p=-1;
               for (int j=0; j<len; j++){
                   if (j==0||s[i][j]!=s[i][j-1]) ++p;
                   ++cnt[p];    
               }
           }
           for (int i=0; i<=k; i++){
               avg[i]=cnt[i]/n;
               if ((cnt[i]%n)>=(n/2.0)) ++avg[i];
           }
           for (int i=1; i<=n; i++){
               len=strlen(s[i]); p=-1;
               for (int j=0; j<len; j++){
                   if (j==0||s[i][j]!=s[i][j-1]){
                      if (j>0){
                         ac+=abs(c-avg[p]);
                      }
                      ++p; c=1;
                   }
                   else ++c;
                   if (j==len-1) ac+=abs(c-avg[p]);
               }
           }
           printf("Case #%d: %d\n",o,ac);
        }
        else printf("Case #%d: Fegla Won\n",o);
    }
    return 0;      
}
