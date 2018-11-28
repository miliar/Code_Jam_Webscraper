#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("b-large.txt","w",stdout);
    int f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7,f_8,f_9;
    long long int num,result,result_a,cs=1,tc,i,j,r;
    scanf("%lld",&tc);
    while(tc--)
    {
        f_0=f_1=f_2=f_3=f_4=f_5=f_6=f_7=f_8=f_9=0;
        scanf("%lld",&num);
        if(num==0) printf("Case #%lld: INSOMNIA\n",cs++);
        for(i=1;i<=100; i++)
        {
            result=i*num;
            r=result;
            while(result!=0)
            {
                result_a=result%10;
                if(result_a==0) f_0=1;
                else if(result_a==1) f_1=1;
                else if(result_a==2) f_2=1;
                else if(result_a==3) f_3=1;
                else if(result_a==4) f_4=1;
                else if(result_a==5) f_5=1;
                else if(result_a==6) f_6=1;
                else if(result_a==7) f_7=1;
                else if(result_a==8) f_8=1;
                else if(result_a==9) f_9=1;
                result/=10;
            }
            if(f_0==1 && f_1==1 && f_2==1 && f_3==1 && f_4==1 && f_5==1 && f_6==1 && f_7==1 && f_8==1 && f_9==1)
            {
                printf("Case #%lld: %lld\n",cs++,r);
                break;
            }
        }
    }
    return 0;
}
