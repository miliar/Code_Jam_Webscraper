#include<bits/stdc++.h>
typedef long long LL;
using namespace std;

int main()
{
    int t;
    //freopen("A-large.in","rt",stdin);
    //freopen("output.cpp","wt",stdout);
    scanf("%d",&t);
    for(int x=1;x<=t;x++){
        LL n;
        scanf("%lld",&n);
        printf("Case #%d: ",x);
        if(n==0){
            printf("INSOMNIA\n");
            continue;
        }
        bool visited[11];
        for(int i=0;i<=9;i++){
            visited[i]=false;
        }
        int flag=0;
        for(LL i=1;1;i++){
            LL temp=n*i;
            //cout<<temp<<"\n";
            while(temp){
                LL remain=temp%10;
                //cout<<"remain="<<remain<<endl;
                visited[remain]=true;
                temp/=10;
            }
            int j;
            for(j=0;j<=9;j++){
                //cout<<visited[i]<<" ";
                if(visited[j]!=true){
                    break;
                }
            }
            //cout<<endl;
            if(j==10){
                printf("%lld\n",i*n);
                break;
            }
        }

    }
    return 0;
}
