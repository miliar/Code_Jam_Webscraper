#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

long long int arr[11];

long long power(long long a, long long b) {
        long long result = 1;
        long long temp = 1;
        long long mask = 1;
        for (int i = 0; i < 64; i++) {
            mask = (i == 0) ? 1 : (mask * 2);
            temp = (i == 0) ? a : (temp * temp);
            
            if ((b & mask) == mask) {
                result = (result * temp);
            }
        }
        return result;
}

long long int notPrime(long long int a, int x)
{
    long long int m;
    for(m=2;m<=sqrt(a);m++)
    {
        if(a%m==0)
        {
            arr[x]=m;
            return 1;
        }
    }
    return 0;
}

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("2output.txt","w",stdout);
    long long int n,t,i,a,b[16],j,sum2,sum3,sum4,sum5,sum6,sum7,sum8,sum9,k,count=0;
    scanf("%lld",&t);
    scanf("%lld%lld",&n,&j);
    i=1000000000000001;
    printf("Case #1: \n");
    while(i<=1111111111111111)
    {
        a=i;
        sum2=0,sum3=0,sum4=0,sum5=0,sum6=0,sum7=0,sum8=0,sum9=0;
        if(notPrime(a,10))//check for base10
        {
            for(k=0;k<16;k++)
            {
                b[15-k]=a%10;
                a=a/10;
                sum2+=b[15-k]*power(2,k);
            }
            if(notPrime(sum2,2))//check for base2
            {
                for(k=0;k<16;k++)
                    sum3+=b[15-k]*power(3,k);

                if(notPrime(sum3,3))//check for base3
                {
                    for(k=0;k<16;k++)
                        sum4+=b[15-k]*power(4,k);

                    if(notPrime(sum4,4))//check for base4
                    {
                        for(k=0;k<16;k++)
                            sum5+=b[15-k]*power(5,k);

                        if(notPrime(sum5,5))//check for base5
                        {
                            for(k=0;k<16;k++)
                                sum6+=b[15-k]*power(6,k);

                            if(notPrime(sum6,6))//check for base6
                            {
                                for(k=0;k<16;k++)
                                    sum7+=b[15-k]*power(7,k); 

                                if(notPrime(sum7,7))//check for base7
                                {
                                    for(k=0;k<16;k++)
                                        sum8+=b[15-k]*power(8,k);

                                    if(notPrime(sum8,8))//check for base8
                                    {
                                        for(k=0;k<16;k++)
                                            sum9+=b[15-k]*power(9,k);

                                        if(notPrime(sum9,9))//check for base9
                                        {
                                            printf("%lld ",i);//print number in base 10
                                            for(k=2;k<=10;k++)
                                                printf("%lld ",arr[k]);//print non trivial divisors of number from base 2 to 10
                                            printf("\n");
                                            count++;
                                        }//end of sum9
                                    }//end of sum8
                                }//end of sum7
                            }//end of sum6
                        }//end of sum5
                    }//end of sum4
                }//end of sum3
            }//end of sum2
        }//end of a
        long long int z=10,r=0;
        k=0;
        while (i!=0 || z!=0)
        {
            b[k++] =(i%10 + z%10 + r)%2;
            r =(i%10 + z%10 + r)/2;
            i = i/10;
            z = z/10;
        }
        if (r != 0)
            b[k++] = r;
        --k;
        for(k=15;k>=0;k--)
            i+=b[k]*power(10,k);
        if(count==50)
            break;
    }//end of main for loop
	return 0;
}