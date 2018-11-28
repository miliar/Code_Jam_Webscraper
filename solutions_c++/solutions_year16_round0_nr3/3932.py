#include <iostream>
#include <fstream>
#include<string>
#include <math.h>
using namespace std;
long long isPrime (long long  num)
{
     if (num % 2 == 0)
        return 2;
    else
    {
        long long divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);

        while (divisor <= upperLimit)
        {
            if (num % divisor == 0){
                return divisor;
            }
            divisor +=2;
        }
        return -1;
    }
}
long long st_in(string x,int base)
{
    long long n=0;
    for(int i=x.length()-1; i>=0; i--)
    {

       n=n+pow(base,x.length()-i-1)*(x[i]-'0');
    }
    return n;
}
string gen(int n,int k)
{
    string x="1";
    while(n>0)
    {
        if(n%2==0)
        {
            x="0"+x;
        }
        else
        {
            x="1"+x;
        }
        n/=2;
    }
    while(x.length()<k-1){
        x="0"+x;
    }
    x="1"+x;
    return x;
}
int main()
{
    string line;
    fstream in("C-small-attempt4.in", ios_base::in);
    ofstream out;
    out.open("out.txt");
    int i=0,t,n,j,k=0;
    long long si;

    in>>t;
    while(i<t)
    {
         out<<"case #"<<i+1<<":"<<endl;
        in>>n>>j;
        string z="";
        long long div[11];
        bool pri=false;
        for(int x=0; k<j&&x<pow(2,n-2); x++)
        {
            z=gen(x,n);
            pri=false;
           //cout<<z<<"  ";
            for(int y=2; !pri&&y<=10; y++)
            {
                 si=st_in(z,y);
                div[y]=isPrime(si);
             // cout<<si<<"  "<<y<<"  "<<div[y]<<endl;
                if(div[y]==-1)
                {
                    pri=true;
                    break;
                }
            }
            if(!pri)
            {
                k++;
                out<<z<<" ";
                for (int x=2; x<10; x++)
                {
                    out<<div[x]<<" ";
                }
                out<<div[10]<<endl;
            }
        }

        i++;
    }
    return 0;
}
