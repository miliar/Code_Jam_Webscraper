#include<bits/stdc++.h>
using namespace std;

int ara[15];
int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("ACountingSheep.out","w",stdout);
    int T,cs=0;
    scanf("%d", &T);
    while(T--)
    {
        int n,keep;
        scanf("%d", &n);
        memset(ara, 0, sizeof(ara));
        if(n==0)
            printf("Case #%d: INSOMNIA\n", ++cs);

        else{
            int i=1, real_n=n;
            while(1){
                keep=n;

                while(keep>0)
                {
                    int remd=keep%10;
                    ara[remd]++;
                    keep=keep/10;

                }
                int flag=0;
                for(int p=0;p<10;p++){

                    if(ara[p]>0){
                        flag=1;
                    }
                    else{
                        flag=0;
                        break;
                    }

                }

                if(flag==1){
                    printf("Case #%d: %d\n", ++cs,n);
                    break;
                }

                i++;
                n=real_n*i;
            }
        }


    }


    return 0;
}
