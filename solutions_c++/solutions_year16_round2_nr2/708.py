#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <bitset>
#include <map>

using namespace std;

#define MAXN 100
#define INF 0x3f3f3f3f
#define mo 1000000007
typedef long long LL;

int n; LL m;
char a[MAXN],b[MAXN];
char ans1[MAXN],ans2[MAXN];
char res1[MAXN],res2[MAXN];

void Check(int i,LL d,int k)
{
    for(;i<n;++i){
        if(k==1){
            if(a[i]=='?') res1[i]='0';
            else res1[i]=a[i];
            if(b[i]=='?') res2[i]='9';
            else res2[i]=b[i];
            d=d*10+res1[i]-res2[i];
        }
        else{
            if(a[i]=='?') res1[i]='9';
            else res1[i]=a[i];
            if(b[i]=='?') res2[i]='0';
            else res2[i]=b[i];
            d=d*10+res2[i]-res1[i];
        }
    }
    if(m==-1||d<m){
        m=d;
        for(int j=0;j<n;++j) ans1[j]=res1[j],ans2[j]=res2[j];
        ans1[n]=ans2[n]='\0';
    }
    else if(d==m){
        int j,flag=-1;
        for(j=0;j<n;++j){
            if(res1[j]<ans1[j]){ flag=1; break; }
            if(res1[j]>ans1[j]){ flag=0; break; }
        }
        if(flag==1){
            for(j=0;j<n;++j) ans1[j]=res1[j],ans2[j]=res2[j];
            ans1[n]=ans2[n]='\0';
        }
        if(flag==0) return;
        for(j=0;j<n;++j){
            if(res2[j]<ans2[j]){ flag=1; break; }
            if(res2[j]>ans2[j]){ flag=0; break; }
        }
        if(flag==1){
            for(j=0;j<n;++j) ans1[j]=res1[j],ans2[j]=res2[j];
            ans1[n]=ans2[n]='\0';
        }
    }
}


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j,t;
    for(scanf("%d",&t),i=1;i<=t;++i){
        scanf("%s%s",a,b); n=strlen(a); m=-1;
        for(j=0;j<n;++j){
            if(a[j]=='?'&&b[j]=='?'){
                res1[j]='1'; res2[j]='0'; Check(j+1,1,1);
                res1[j]='0'; res2[j]='1'; Check(j+1,1,-1);
                res1[j]=res2[j]='0';
            }
            else if(a[j]=='?'){
                if(b[j]<'9') res1[j]=b[j]+1,res2[j]=b[j],Check(j+1,1,1);
                if(b[j]>'0') res1[j]=b[j]-1,res2[j]=b[j],Check(j+1,1,-1);
                res1[j]=res2[j]=b[j];
            }
            else if(b[j]=='?'){
                if(a[j]<'9') res1[j]=a[j],res2[j]=a[j]+1,Check(j+1,1,-1);
                if(a[j]>'0') res1[j]=a[j],res2[j]=a[j]-1,Check(j+1,1,1);
                res1[j]=res2[j]=a[j];
            }
            else{
                if(a[j]>b[j]){
                    res1[j]=a[j]; res2[j]=b[j]; Check(j+1,a[j]-b[j],1);
                    break;
                }
                else if(a[j]<b[j]){
                    res1[j]=a[j]; res2[j]=b[j]; Check(j+1,b[j]-a[j],-1);
                    break;
                }
                res1[j]=a[j]; res2[j]=b[j];
            }
        }
        if(j>=n) Check(n,0,0);
        printf("Case #%d: %s %s\n",i,ans1,ans2);
    }
    return 0;
}
