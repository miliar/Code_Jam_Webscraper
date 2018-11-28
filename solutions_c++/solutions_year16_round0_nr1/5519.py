#include<iostream>
#include<fstream>
using namespace std;

int sheep(int n)
{
    long long int newn=n;
    int a[10],i,temp,rem,c=0;
    for(i=0;i<10;i++)
        a[i]=0;
    while(1)
    {
        temp=newn;
        while(temp>0)
        {
            rem=temp%10;
            if(a[rem]==0)
            {
                a[rem]=1;
                c++;
            }
            temp/=10;
        }
        if(c==10)
            return newn;
        newn+=n;
    }
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");
    int t;
    fin>>t;
    for(int k=0;k<t;k++)
    {
        int n;
        fin>>n;
        if(n==0)
            fout<<"Case #"<<(k+1)<<": INSOMNIA"<<endl;
        else
            fout<<"Case #"<<(k+1)<<": "<<sheep(n)<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
