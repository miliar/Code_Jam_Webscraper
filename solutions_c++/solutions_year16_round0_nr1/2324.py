#include<bits/stdc++.h>
using namespace std;
int n;
int done[22];
bool check(){
    for(int i=0;i<10;i++)if(!done[i])return 0;
    return 1;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("myout","w",stdout);
    int _,cas=1;scanf("%d",&_);    
    while(_--){
        scanf("%d",&n);
        printf("Case #%d: ",cas++);
        if(n==0)puts("INSOMNIA");
        else{
            memset(done,0,sizeof(done));
            for(int i=n;;i+=n){
                int x=i;
                while(x){
                    done[x%10]=1;
                    x/=10;
                }
                if(check()){
                    printf("%d\n",i);
                    break;
                }
            }
        }
    }
}
