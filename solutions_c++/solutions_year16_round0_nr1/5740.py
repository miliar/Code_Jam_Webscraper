#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("input.in");
    ofstream out("out.in");
    long long int t,n,i,j,k,a,b;
    in>>t;
    for(i=1;i<=t;i++)
    {
        in>>n;
        int chk[10];
        for(j=0;j<10;j++)
            chk[j]=0;
        long long int sum=0;
        j=1;
        if(n==0)
            out<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
        {
        sum=0;
        while(1)
        {
            a=j*n;
            b=a;
            while(a)
            {
                k=a%10;
                a/=10;
                //cout<<a<<" ";
                if(chk[k]==0)
                {
                    chk[k]=1;
                    sum++;
                }
            }
          //  cout<<endl;
           if(sum==10)
                break;
           j++;
        }
        out<<"Case #"<<i<<": "<<b<<endl;
        }
    }
}
