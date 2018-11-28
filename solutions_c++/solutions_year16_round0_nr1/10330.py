#include<cstdio>
#include<cstring>
int main(){
    int N,n,t,m=1,s;
    int arr_1[20];
    int vis[11];
    memset(arr_1,0,sizeof(arr_1));
    memset(vis,0,sizeof(vis));
    //freopen("A-large.in","r",stdin);
    //freopen("test.txt","w",stdout);
    scanf("%d",&s);
    while(s--){
        scanf("%d",&n);
        int i_count=0;
        N = n;
        t = n;
        while(n){
            for(int i = 0;i <= 20;i++){
                if(n%10==0&&n/10==0)
                    break;
                arr_1[i] = n%10;
                if(vis[arr_1[i]] == 0){
                    vis[arr_1[i]] = 1;
                    i_count++;
                    if(i_count == 10)
                        break;
                }
                n = n/10;
            }
            memset(arr_1,0,sizeof(arr_1));
            N += t;
            n = N;
            if(i_count == 10)
                break;
        }
        if(n!=0)
            printf("Case #%d: %d\n",m,N-t);
        else
            printf("Case #%d: INSOMNIA\n",m);
        memset(arr_1,0,sizeof(arr_1));
        memset(vis,0,sizeof(vis));
        m++;
    }

    return 0;
}
