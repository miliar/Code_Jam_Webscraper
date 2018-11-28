#include <iostream>
#include <cmath>
#include <utility>
#include <cstdio>

using namespace std;


/* Function to calculate (base^exponent)%modulus */
long long int modular_pow(long long int base, int exponent,
                          long long int modulus)
{
    /* initialize result */
    long long int result = 1;
 
    while (exponent > 0)
    {
        /* if y is odd, multiply base with result */
        if (exponent & 1)
            result = (result * base) % modulus;
 
        /* exponent = exponent/2 */
        exponent = exponent >> 1;
 
        /* base = base * base */
        base = (base * base) % modulus;
    }
    return result;
}
 
/* method to return prime divisor for n */
long long int PollardRho(long long int n)
{
    /* initialize random seed */
    srand (time(NULL));
 
    /* no prime divisor for 1 */
    if (n==1) return n;
 
    /* even number means one of the divisors is 2 */
    if (n % 2 == 0) return 2;
 
    /* we will pick from the range [2, N) */
    long long int x = (rand()%(n-2))+2;
    long long int y = x;
 
    /* the constant in f(x).
     * Algorithm can be re-run with a different c
     * if it throws failure for a composite. */
    long long int c = (rand()%(n-1))+1;
 
    /* Initialize candidate divisor (or result) */
    long long int d = 1;  
 
    /* until the prime factor isn't obtained.
       If n is prime, return n */
    while (d==1)
    {
        /* Tortoise Move: x(i+1) = f(x(i)) */
        x = (modular_pow(x, 2, n) + c + n)%n;
 
        /* Hare Move: y(i+1) = f(f(y(i))) */
        y = (modular_pow(y, 2, n) + c + n)%n;
        y = (modular_pow(y, 2, n) + c + n)%n;
 
        /* check gcd of |x-y| and n */
        d = __gcd(abs(x-y), n);
 
        /* retry if the algorithm fails to find prime factor
         * with chosen x and c */
        if (d==n) return -1;
    }
 
    return d;
}


int next(int A[],int n)
{
    int i=n-2;
    while(i>0&&A[i]==1) {
        A[i]=0;
        i--;
    }
    if(i>0) {
        A[i]=1;
        return n-i-1;
    }
    return -1;
    
}

int main()
{
    int k,i,c,flag;
    
    int n=16,j=50,x,divisor[11];
    int num[16]={0};
    long long int val[11],add[11]={0};
    num[0]=1;
    num[n-1]=1;
    for(i=2;i<=10;i++) {
        val[i]=(long long int)pow(i,n-1)+1;
    }
    printf("Case #1:\n");
    while(j) {
        flag=1;
        for(i=2;i<=10;i++) {
            val[i]=val[i]+add[i];
            if(flag!=0) {
                divisor[i]=PollardRho(val[i]);
                if(divisor[i]<0||divisor[i]==val[i]||val[i]%divisor[i]!=0) {
                    flag=0;
                }
            }
        }
        if(flag) {
            for(i=0;i<n;i++) {
                cout<<num[i];
            }
            cout<<" ";
            for(i=2;i<=10;i++) {
                cout<<divisor[i]<<" ";   /**/
            }
            cout<<endl;
            j--;
        }
        x=next(num,n);
        //cout<<x;
        for(i=2;i<=10;i++) {
            add[i]=(long long int)pow(i,x)-i*(((long long int)pow(i,x-1)-1)/(i-1));
        }
    }
    return 0;
}
