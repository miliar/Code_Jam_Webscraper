#include <fstream>
#include <math.h>
using namespace std;
long long power(long long a, long long b)
{
    long long ans = 1;
    while(b > 0)
    {
        if(b%2 == 1)
            ans *= a;
        a *= a;
        b = b>>1;
    }
    return ans;
}
int main()
{
    long long N,J,count=0,i,j,t,start,max,k,l,flag,y,sum,pos,fac;
    long long a[20],b[11];
    ifstream ip;
    ip.open("C-small-attempt0.in");
    ofstream op;
    op.open("output.in");
    ip>>t;
    op<<"Case #"<<t<<":"<<endl;
    while(t--)
    {
        ip>>N>>J;
        start = power(2,N-1)+1;
        max = power(2,N);
        for(i=start;i<max;i=i+2)
        {
            if(count==J)
                break;
            k=i;
            l=0;
            while(k!=0)
            {
                a[l++]=k%2;
                k=k/2;
            }
            flag=y=0;
            for(j=2;j<=10;j++)
            {
                sum=pos=0;
                for(k=0;k<l;k++)
                {
                    sum = sum + a[k] * power(j,pos);
                    pos++;
                }
                for(fac=2;fac<=sqrt(sum);fac++)
                    if(sum%fac==0)
                        break;
                if(fac<=sqrt(sum))
                    b[y++]=fac;
                else
                {
                    flag=1;
                    break;
                }
            }
            if(flag!=1)
            {
                for(j=l-1;j>=0;j--)
                    op<<a[j];
                op<<" ";
                for(j=0;j<y;j++)
                    op<<b[j]<<" ";
                op<<"\n";
                count++;
            }
        }
    }
    ip.close();
    op.close();
    return 0;
}
