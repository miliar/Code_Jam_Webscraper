#include<bits/stdc++.h>


using namespace std;

bool visit[10];

int newDigitis(long long n){
    int ret=0;
    do{
        int temp = n%10;
        if(visit[temp])continue;
        visit[temp]=true;
        ret++;
    }while(n/=10);
    return ret;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++){
        memset(visit,false,sizeof(visit));
        int cnt=0;
        long long N;
        cin>>N;
        if(N==0){
            printf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        for(int i=1;;i++){
            cnt+=newDigitis((long long)i*N);
            if(cnt==10){
                printf("Case #%d: %lld\n",t,i*N);
                break;
            }
        }
    }
    return 0;
}
