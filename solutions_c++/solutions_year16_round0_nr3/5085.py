#include <stdio.h>
using namespace std;

int dp[20];
int number[20];
bool isprime(long long int x)
{
    for (long long int l=2;l*l <= x; l++)
        if ( x % l == 0 ) return false;
    return true;

}

long long int divisor(long long int x)
{
    for (long long int l=2;l*l<=x;l++)
        if ( x % l == 0 ) return l;
}


void solve()
{   
    int count=0;
    dp[0] = 1;
    dp[15] = 1;
    for (int num=0;num<(1<<14);num++)
    {
        
        for (int l=1,ll=num;l<=14;l++,ll/=2)
            dp[l] = ll % 2;

        for (int r=2;r<=10;r++)
            number[r] = 0;

        bool allcomposite = true;
        for (int r = 2; r <= 10;r++)
        {
            number[r] = 0;
            for (int l=15;l>=0;l--)
                number[r] = number[r] * r + dp[l];
            if ( isprime(number[r]) ) allcomposite = false;
       }

       if ( allcomposite && count < 2 )
       {
            
            printf("\n");
            count++;
            for (int i=15;i>=0;i--) printf("%d",dp[i]);
            printf(" ");
            for (int r=2;r<=10;r++) printf("%lld ",divisor(number[r]));
        
       }
    }
 
}

int main()
{
    int T=1;
    for (int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
