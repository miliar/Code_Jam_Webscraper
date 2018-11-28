#include <bits/stdc++.h>
using namespace std;
long long divisor;

long long powe(long long a,long long b)
{
    if(b == 0)
        return 1;
    long long ac = a;
    for(long long i = 2;i<=b;i++)
        ac*=a;
        return ac;

}
 long long ifprime(long long n)
 {
     if(n==0)
        return 0;
     if(n == 1)
     {
         return 0;
         divisor = 1;
     }

     for(long long i = 2;i<= n/i;i++)
     {
         if(n%i == 0)
         {
             divisor = i;
             return 0;
         }
     }
     return 1;
 }
long long check(long long b,long long marked[])
{
    long long sum = 0;
    for(long long i = 0;i<=15;i++)
    {
            sum+=marked[i]*pow(b,i);
    }
    if(ifprime(sum))
    return 0;
    return 1;
}
int main()
{
    long long t;
    cin>>t;
    long long co = 0;
    while(t--)
    {
        co++;
        long long n,jo;
        cin>>n>>jo;
        long long str = powe(2,n-1)+1;
        long long lim = powe(2,n);
        for(long long i = str;i<=lim;i++)
        {
            if(1&i && (1<<(n-1))&(i))
            {
                //long long coun = 16;
                long long ico = i;
                long long marked[16] = {0};
                long long j = 0;
                while(j<n)
                {
                    if(i&(1<<j))
                    {
                        marked[j] = 1;
                    }
                    j++;
                }
                long long ha= 0;
                long long a[20];
                for(long long i =2;i<=10;i++)
                {
                        if(check(i,marked))
                        {
                            a[ha] = divisor;
                          ha++;

                        }
                        else
                            break;
                }
                if(ha == 9 && jo)
                {
                    for(long long j = n-1;j>=0;j--)
                        cout<<marked[j];
                    cout<<" ";
                    for(long long j=0;j<9;j++)
                        cout<<a[j]<<" ";
                    cout<<endl;
                    jo--;
                }
                if(jo == 0)
                    return 0;

            }
        }




    }
}

