#include<bits/stdc++.h>

using namespace std;

ofstream fout("output.txt");

long long convertToBase(long long num, int base)
{
    long long b10=0;
    long long i=0;
    while(num>0)
     {
         long long x=num%10;
         double exponent=pow(base,i);
         long long val=(x*exponent);
         b10=b10+val;
         num=num/10;
         i++;
     }
    return b10;
}

long long isPrime(long long number){

    if(number < 2) return 1ll;
    if(number == 2) return 1ll;
    if(number % 2 == 0) return 2ll;
    for(long long i=3; (i*i)<=number; i+=2){
        if(number % i == 0 )
            return i;
    }
    return 1ll;
}

long long convertToBinary(long long num)
{
     long long binaryNum=0;

     long long i=0;

     while(num>0)
     {
         long long x=num%2;
         double exponent=pow(10,i);
         long long val=(x*exponent);
         binaryNum=binaryNum+val;
         num=num/2;
         i++;
     }
     return binaryNum;
}

int main()
{
    long long n=16,j=50;

    fout<<"Case #1: "<<endl;

    for(long long i=((1<<(n-1)) + 1);i<(1<<n);i=i+2)
    {
        long long nums[9] = {0};
        int flag=1;

        long long x=convertToBinary(i);

        if(x&1)
        {
            for(int k=2;k<=10;k++)
            {
                long long num=convertToBase(x,k);
                long long prime = isPrime(num);
                if(prime != 1ll)
                {
                    nums[k-2]=prime;
                }
                else
                {
                    flag=0;
                    break;
                }
            }

            if(flag==1)
            {
                fout<<x<<" ";
                for(int i=0;i<9;i++)
                    fout<<nums[i]<<" ";

                fout<<endl;

                j--;
            }
        }

        if(j==0)
            break;
    }

    return 0;
}
