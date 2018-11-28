#include<bits/stdc++.h>
using namespace std;
#define lt unsigned long long int
lt fun(int a[],int n,int i,int s)
{
    if(i>=s)
        return 0;
    return (pow(n,i)*a[i])+fun(a,n,i+1,s);
}
bool isPrime (lt num)
{
    if (num <=1)
        return false;
    else if (num == 2)
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        lt divisor = 3;
        double num_d = static_cast<double>(num);
        lt upperLimit = static_cast<lt>(sqrt(num_d) +1);

        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}
lt factor(lt a)
{
    lt i=2;
    while(a%i!=0)
    {
        i++;
    }
    return i;
}
int main()
{
    ifstream fp;
    fp.open("C-small-attempt0.in",ios::in);
    ofstream fo;
    fo.open("out4.txt",ios::out);
    int a[100];
    int n,j,i,k,c=0,t;
    lt z,b[12];
    fp>>t;
    fp>>n>>k;
    fo<<"Case #1"<<": "<<endl;
    for(i=0;i<n;i++)
    {
        a[i]=0;
    }
    a[n-1]=a[0]=1;
    while(c!=k)
    {

        //c=k;
        for(i=2;i<=10;i++)
        {
            b[i]=fun(a,i,0,n);
            if(isPrime(b[i]))
                break;
        }
        if(i>10)
        {
            fo<<b[i-1]<<" ";
            for(i=2;i<=10;i++)
                fo<<factor(b[i])<<" ";
            c++;
            fo<<endl;
        }
        //c++;
        for(j=1;a[j]!=0;j++);
        a[j]=1;
        for(--j;j>1;j--)
            a[j]=0;
    }

}
