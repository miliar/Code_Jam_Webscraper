#include<cstdio>

using namespace std;


int main(void)
{
    int cases, cas;
    int digit[10];
    scanf("%d",&cases);
    for(int cas=1;cas<=cases;cas++){
        long long int n;
        scanf("%lld",&n);

        if(n==0){
            printf("Case #%d: INSOMNIA\n",cas);
            continue;
        }

        //initialize
        for(int i=0;i<10;i++)
            digit[i] = 0;

        //for every number;
        long long int number = 0;
        int flag ;

        for(int i=1;;i++){
                number += n;
                flag = 1;
                long long int tmp = number;

                while(tmp){
                    digit[tmp%10] = 1;
                    tmp/=10;
                }

                for(int j=0;j<10;j++){
                    if(digit[j] ==0){
                        flag = 0;
                        break;
                    }
                }

                if(flag ==1){
                    break;
                }

        }

        printf("Case #%d: %lld\n",cas,number);

    }

    return 0;
}
