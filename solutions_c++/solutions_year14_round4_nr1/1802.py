#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
int T,N,X;
int s[20];
int a[20];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
            scanf("%d%d",&N,&X);
    for(int i=0;i<N;++i)
            scanf("%d",&s[i]);
    for(int i=0;i<N;++i)
            a[i]=i;
    int ans=N;
    do{
            int tot=0;
            int sum=0;
            int cnt=0;
            for(int i=0;i<N;++i){
                    if(cnt<2){
                        if(sum+s[a[i]]<=X){
                             sum+=s[a[i]];
                             cnt++;
                        } else {
                          sum = s[a[i]];
                          cnt=1;
                          tot++;
                        }
                    } else {
                      sum=s[a[i]];
                      cnt=1;
                      tot++;
                    }
            } 
            if(sum>0)tot++;
            ans=min(ans,tot);
    }while(next_permutation(a,a+N));
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
