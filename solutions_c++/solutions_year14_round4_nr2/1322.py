#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
#define NN 12
#define inf 1000000000
using namespace std;
int T,N;
int A[NN],a[NN];
bool vis[NN];
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
            cin>>N;
            int maxv=0;
            int pos=-1;
            for(int i=0;i<N;++i){
                    scanf("%d",A+i);
                    if(A[i]>maxv){
                        maxv=A[i];
                        pos=i;
                    }
            }
            for(int i=0;i<N;++i)
                    a[i]=i;
            int ans=inf;
            do{
                int tot=0;
                int i;
                for(i=0;i<N;++i)
                    if(A[a[i]]==maxv)
                        break;
                int pos=i;
                int j;
                bool ok=true;
                for(j=pos-1;j>=0;--j)
                    if(A[a[j]]>=A[a[j+1]])break;
                if(j>=0)ok=false;
                for(j=pos+1;j<N;++j)
                    if(A[a[j]]>=A[a[j-1]])break;
                if(j<N)ok=false;
                if(ok){
                     //  if(a[0]==0 && a[1]==1 && a[2]==2)cout<<pos<<endl;
                   memset(vis,false,sizeof(vis));
                   for(int i=0;i<N;++i){
                           int j;
                           int cnt=0;
                           for(j=0;j<a[i];++j){
                               if(vis[j])cnt++;
                           }
                           vis[a[i]]=true;
                           tot+=abs(0-(a[i]-cnt));
                   } 
                   ans=min(ans,tot);
                }
            }while(next_permutation(a,a+N));
            printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
