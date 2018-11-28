#include <iostream>
#include <bitset>
#include <math.h>
/*size of integers array*/
#define PRIMES 700000 /*size of primes array*/
using namespace std;
int bSearch(int n,int array[], int start, int end){
    int middle = (start+end)/2;

    if (start>end)
        return 0;

    if (n==array[middle])
        return 1;

    if (n>array[middle])
        return bSearch(n,array,middle+1, end);
    else
        return bSearch(n,array,start,middle-1);
}
long long int  power(int n, int p)
{
    if(p==0)
    return 1;
    long long int power=1;
    for(int i=0;i<p;i++)
    power*=n;
    return power;
}
long long int convert(string s,int size,int base )
{
    long long int number=0,current=size;
    for(int i=0;i<size;i++)
    number+=int(s[i]-'0')*power(base,--current);
    return number;
}

int main(){
    int i,j;
    int *primes,*numbers;
    int count = 0;
    long long int  LIMIT =sqrt(power(10,16)-1)/3;
    primes = new int[PRIMES];
    numbers = new int[LIMIT];

    /*fill the array with natural numbers*/
    for (i=0;i<LIMIT;i++){
        numbers[i]=i+2;
    }

    /*sieve the non-primes*/
    for (i=0;i<LIMIT;i++){
        if (numbers[i]!=-1){
            for (j=2*numbers[i]-2;j<LIMIT;j+=numbers[i])
                numbers[j]=-1;
        }
    }

    /*transfer the primes to their own array*/
    j = 0;
    for (i=0;i<LIMIT&&j<PRIMES;i++)
        if (numbers[i]!=-1)
            primes[j++] = numbers[i];

    for (i=2;i<10000000;i++)
        if (bSearch(i,primes,0,j-1))
            count++;
    //cout<<primes[j-1]<<endl;
    //printf("count=%d\n",count);
    cout<<"Case #1:"<<endl;
    int t,n,J;
    cin>>t>>n>>J;
    for(int i=pow(2,n-1)+1;i<=pow(2,n)-1 && J>0;i=i+2)
    {

        string binary = bitset<16>(i).to_string(); //to binary

        int flag=1;
        long long int a[11]={0},b[11]={0};
        for(int k=2;k<=10;k++)
        {
            //cout<<binary<<endl;
           long long int number=convert(binary,n,k);
           b[k]=number;
            //cout<<"number : "<<number<<endl;
            if(number<=10570841)
            {
                if (bSearch(number,primes,0,j-1))
                {

                    flag=0;
                    break;
                }
            }
            else
            {
                int flag1=1;
                for(int j=0;j<count;j++)
			    {
				    if(number%primes[j]==0 )
				    {
					    flag1=0;
				    	break;
			    	}
                }
                if(flag1==1)
                {
                    flag=0;
                   // cout<<"the binary number is "<<binary<<" : "<<number<<endl;

                    break;
                }

            }
        }
        if (flag==1)
        {
            J--;
            for(int k=2;k<=10;k++)
            {
                for(int l=0;l<count;l++)
                    {
                        if(b[k]%primes[l]==0)
                        {
                            a[k]=primes[l];
                            break;

                        }
                    }
            }
                cout<<binary<<" ";
                for(int m=2;m<=10;m++)
                cout<<a[m]<<" ";
                cout<<endl;
                //for(int m=2;m<=10;m++)
                //cout<<b[m]<<" ";
                //cout<<endl;

        }
    }
    //unsigned long long decimal = std::bitset<16>(binary).to_ulong();
    //std::cout<<decimal<<"\n";
    return 0;
}

