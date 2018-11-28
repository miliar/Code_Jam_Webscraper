#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main()
{
    int T;
    cin>>T;

    for(int t=1;t<=T;t++){
        long long i=1,j,n,flag,x,N,a[10];
        cin>>N;

        if(!N){
            printf("Case #%d: INSOMNIA\n",t);
            continue;
        }
        memset(a,0,sizeof a);
        n=N;
        while(1)
        {
            x = n;
            while(x)
            {
                a[x%10]++;
                x/=10;
            }
            for(j=0;j<=9;j++){
                if(!a[j])
                break;
            }
            if(j==10){
                flag = 1;
                break;
            }
            if(i==1000){
                flag = 2;
                break;
            }

            n += N;
            i++;
        }
        if(flag == 1){
            printf("Case #%d: %lld\n",t,n);
        }else{
            printf("Case #%d: INSOMNIA\n",t);
        }
    }
    return 0;
}
