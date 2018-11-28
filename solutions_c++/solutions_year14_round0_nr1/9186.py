#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int vis[20];
int main(){
    int t;
    int ca=1,i,j,res,x;
    int n,m;
    cin>>t;
    while(t--){
        memset(vis,0,sizeof(vis));
        cin>>n;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>x;
                if(i==n-1){
                    vis[x]=1;
                }
            }
        }
        cin>>m;
        int cnt=0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>x;
                if(i==m-1){
                    if(vis[x]){
                        res=x;
                        cnt++;
                    }
                }
            }
        }
        printf("Case #%d: ",ca++);
        if(cnt==0){
            printf("Volunteer cheated!\n");
        }
        else if(cnt==1){
            printf("%d\n",res);
        }
        else{
            printf("Bad magician!\n");
        }
    }
    return 0;
}
