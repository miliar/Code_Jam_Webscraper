#include<algorithm>
#include<cstdio>
#include<cmath>
#include<iostream>
#include<string.h>
#include<time.h>
#include<queue>
#include<vector>
#include<stack>
#include<map>
using namespace std;
#define ll long long
template <class T>
void read(T &ret)
{
    int f=1; char ch=getchar();
    ret=0;
    while(ch<'0'||ch>'9'){if(ch=='-') f=-f; ch=getchar();}
    while(ch>='0'&&ch<='9'){ret=ret*10+ch-'0'; ch=getchar();}
    ret*=f;
}
const int N=1010;
int to[N],p[N];
int main(){
#ifdef gh546
freopen("b.in","r",stdin);
freopen("b.out","w",stdout);
#endif
    int TAT,cas=1;; scanf("%d",&TAT);
    while(TAT--){
        int n; scanf("%d",&n);
        for(int i=1;i<=n;i++){
            scanf("%d",&to[i]);
        }
        int ans=1;
        for(int i=1;i<=n;i++) p[i]=i;
        do{
            for(int i=ans+1;i<=n;i++){
                int flag=0;
                for(int j=1;j<=i;j++){
                    int id1=p[j], id2=p[j-1] ,id3=p[j+1];
                    if(j==1) id2=p[i];
                    if(j==i) id3=p[1];
                    if(to[id1]==id2||to[id1]==id3){
                        continue;
                    }
                    else{
                        flag=1; break;
                    }
                }
                if(!flag) {ans=max(ans,i);}
            }
            if(ans==n) break;
        }while(next_permutation(p+1,p+n+1));
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;
}
