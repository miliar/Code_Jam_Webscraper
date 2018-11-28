#include<cstdio>  
#include<cstdlib>  
#include<cstring>  
#define L 1000050  
#define M 10050  
using namespace std;  
int next[M];  
char par[M],ori[L];  
int main(){  
    int t,l1,l2,i,j,ans;  
    for(scanf("%d",&t);t--;){  
        scanf("%s",par);  
        scanf("%s",ori);  
        memset(next,-1,sizeof next);//ÇónextÊý×é  
        l1=strlen(par);  
        i=0;j=-1;  
        while(i<l1){  
            if(j==-1||par[i]==par[j])next[++i]=++j;  
            else j=next[j];  
        }  
        l2=strlen(ori);  
        i=j=ans=0;  
        while(i<l2){  
            if(j==-1){i++;j++;}  
            if(ori[i]==par[j]){  
                if(j==l1-1){  
                   ans++;  
                    j=next[j];  
                }else{i++;j++;}  
            }else j=next[j];  
        }  
        printf("%d\n",ans);  
    }  
    return 0;  
}  
