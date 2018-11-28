#include<iostream>
#include<cstdio>
#include<cmath>
#include<map>

using namespace std;

int t,c,r;
long long int n,m,l;
int digit[11];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    c = 0;
    while(t--)
    {
        ++c;
        scanf("%I64d",&n);
        for(int i=0;i<10;i++)
           digit[i] = 0;

        if(n==0){
            printf("Case #%d: INSOMNIA\n",c);
            continue;
        }

        long long int total_digit = 0,j=1;
        l = n;
        while(total_digit < 10){
             n = l*j; ++j;
             m = n;
             do{
                r = m%10;
                m = m/10;
                if(digit[r]==0){
                    ++total_digit;
                    digit[r]= 1;
                    //printf("n => %I64d r = %d t_d = %d\n",n,r,total_digit);
                }
             }while(m!=0);

             if(total_digit > 9){
                printf("Case #%d: %I64d\n",c,n);
                break;
             }
        }
    }

    return 0;
}
