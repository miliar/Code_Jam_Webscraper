#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#define maxn 10100
using namespace std;
int c[9]={0,1,-1,2,-2,3,-3,4,-4};
int n,m,T,k,len,flag;
char s[maxn];
int a[maxn],ans[maxn];
int Get(int s1,int s2){
    int flag=0;
    if(s1<0) flag++,s1=-s1;
    if(s2<0) flag++,s2=-s2;
    if(flag==1) flag=-1;
        else flag=1;
    if(s1==s2){
        if(s1==1) return 1*flag;
            else return -1*flag;
    }
    if(s1==1) return s2*flag;
    if(s2==1) return s1*flag;
    if(s1==2){
        if(s2==3) return 4*flag;
        if(s2==4) return -3*flag;
    }
    if(s1==3){
        if(s2==2) return -4*flag;
        if(s2==4) return 2*flag;
    }
    if(s1==4){
        if(s2==2) return 3*flag;
        if(s2==3) return -2*flag;
    }
}
int Get2(int s1,int s2){
    for(int i=1;i<=8;i++)
        if(Get(s1,c[i])==s2) return c[i];
}
int main(){
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++){
        memset(ans,0,sizeof(ans));
        flag=0;
        scanf("%d%d",&n,&m);
        scanf("%s",&s[0]);
        k=len=strlen(s);
        for(int i=1;i<m;i++)
            for(int j=0;j<k;j++) s[len++]=s[j];
        for(int i=0;i<len;i++){
            if(s[i]=='i') a[i]=2;
            if(s[i]=='j') a[i]=3;
            if(s[i]=='k') a[i]=4;
        }
        ans[0]=a[0];
        for(int i=1;i<len;i++) ans[i]=Get(ans[i-1],a[i]);
        //for(int i=0;i<len;i++) printf("%d %d\n",i,ans[i]);
        for(int i=1;i<len&&flag==0;i++)
            for(int j=i+1;j<len&&flag==0;j++)
                if(ans[i-1]==2&&Get2(ans[i-1],ans[j-1])==3&&Get2(ans[j-1],ans[len-1])==4) flag=1;
        printf("Case #%d: ",cas);
        if(flag) printf("YES\n");
            else printf("NO\n");
    }
}

