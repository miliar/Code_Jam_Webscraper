#include<bits/stdc++.h>


using namespace std;
#define ll long long int

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output6.txt","w",stdout);

    int t;
    scanf("%d",&t);

    while(t--)
    {
        int N,J;
        scanf("%d %d",&N,&J);
        int k=0;


            printf("Case #1:\n");

            for(ll i=32769;i<65536&&k<J;i=i+2)
            {
                int B[18];
                int j=0;

                ll temp=i;
                while(temp)
                {
                    B[j++]=temp%2;
                    temp=temp/2;
                }

                int flag=1;

                for(ll base=2;base<=10;base++)
                {
                    long long int num=0;
                    long long int mul=1;

                    for(int in=0;in<=15;in++)
                    {
                        num=num+mul*B[in];
                        mul=mul*base;
                    }

                    int flag1=1;
                    for(ll m=2;m*m<=num;m++)
                    {
                        if(num%m==0)
                            flag1=0;
                    }

                    if(flag1==1)
                    {
                        flag=0;
                        break;
                    }

                }

                if(flag==1)
                {
                    J--;
                    for(int m=15;m>=0;m--)
                        printf("%d",B[m]);

                    for(ll base=2;base<=10;base++)
                    {
                        long long int num=0;
                        long long int mul=1;

                        for(int in=0;in<=15;in++)
                        {
                            num=num+mul*B[in];
                            mul=mul*base;
                        }

                        for(ll m=2;m*m<=num;m++)
                        {
                            if(num%m==0)
                            {
                                printf(" %d",m);
                                break;
                            }
                        }

                    }

                    printf("\n");
                }

            }


    }

}
