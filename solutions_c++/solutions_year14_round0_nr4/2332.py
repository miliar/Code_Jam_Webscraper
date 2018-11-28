#include<cstdio>
#include<algorithm>
#include<cstring>

using namespace std;

#define N 1005
double d1[N],d2[N];
bool s1[N],s2[N];
int t,n;
/*
int dece(){
    int i,j,ret=0;
    memset(s1,0,sizeof(s1));
    memset(s2,0,sizeof(s2));
    for(i=0;i<n;i++){
        bool lose=true;
        for(j=0;j<n;j++)if(s1[j]&&d1[j]>d2[i]){
            lose=false;
            s1[j]=true;
            ret++;
            break;
        }
        if(lose){
            for(j=0;j<n;j++)if(!s1[j]){
                s1[j]=true;
                break;
            }
        }
    }
    return ret;
}
*/
int dece(){
    int i,ret=0;
    for(i=0;i<n;i++)if(d1[i]>d2[ret])ret++;
    return ret;
}
int war(){
    int i,j,ret=0;
    memset(s2,0,sizeof(s2));
    for(i=0;i<n;i++){
        bool lose=false;
        for(j=0;j<n;j++)if(!s2[j]&&d2[j]>d1[i]){
            lose=true;
            s2[j]=true;
            break;
        }
        if(!lose){
            ret++;
            for(j=0;j<n;j++)if(!s2[j]){
                s2[j]=true;
                break;
            }
        }
    }
    return ret;
}

int main(){
    scanf("%d",&t);
    int cas=1;
    while(t--){
        scanf("%d",&n);
        int i;
        for(i=0;i<n;i++)scanf("%lf",d1+i);
        for(i=0;i<n;i++)scanf("%lf",d2+i);
        sort(d1,d1+n);
        sort(d2,d2+n);
        printf("Case #%d: %d %d\n",cas++,dece(),war());
    }
    return 0;
}
