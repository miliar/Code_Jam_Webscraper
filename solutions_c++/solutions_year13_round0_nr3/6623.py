#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

long long int fair();
long long int check(long long int);

long long int a,b;

int main()
{
    ifstream read;
    ofstream write;
    read.open("i.txt",ios::in);
    write.open("small.out",ios::out);
    long long int t;


    long long int y=0;

    read>>t;
    for(long long int i=1; i<=t; i++)
    {
        read>>a>>b;
        y=fair();
        write<<"Case #"<<i<<": "<<y<<"\n";

    }
    return 0;
}

long long int fair()
{   long long int result=0;
    long long int y=0;

    for(long long int i=a; i<=b; i++)
    {


           result=check(i);
            if(result==i)
            {
                for(long long int j=1; j<=i; j++)
                if(j*j==i)
                {   result=check(j);
                    if(result==j)
                    y++;

                }
            }

    }
    return y;
}

long long int check(long long int c)
{
    long long int num=0;
    long long int result=0;
    long long int m=c;
    long long int i=1;
    long long int j=1;
    while(c>9)
    {
        num=c%10;
        while(m>9)
        {

          i=i*10;
          m=c/i;
        }
        result+=num*i;
        i=1;
        c=c/10;
        m=c;
    }
    result+=c;
    return result;
}
