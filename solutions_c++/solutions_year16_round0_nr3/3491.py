#include <iostream>
#include <string>
#include <memory.h>
#include <map>
#include <vector>
#include <math.h>
#include <fstream>
using namespace std;
int NUM;
int sum[35];
int prime[12];
long long Count=0;
ofstream file;
int Const = 0;
int require;

long long Pow(int i,int j)
{
    long long End=1;
    while(j--)
    {
        End = End*i;
    }
    return End;
}
bool IsPrime(long long num, int pos)
{
    for(long long i=2;i<=pow(num,0.5);i++)
        if(num%i==0)
    {
        prime[pos] = i;
        return false;
    }
    return true;
}
bool ReSolve(int Length)
{
    memset(prime,0,sizeof(prime));
    for(int i=2;i<=10;i++)
    {
        Count = 0;
        for(int j=0;j<Length;j++)
        {
            Count += sum[j]*Pow(i,Length-1-j);
        }
        if(IsPrime(Count,i))
            return false;
    }
    return true;

}
void Solve(int Length, int pos)
{
    if(Const==require)
        return;

    if(pos==Length-1)
    {
        if(ReSolve(Length))
        {
            Const++;
            for(int i=0;i<Length;i++)
                file<<sum[i];
            for(int i=2;i<11;i++)
                file<<" "<<prime[i];
            file<<"\n";
        }
        return;

    }
    sum[pos]=0;
    Solve(Length,pos+1);
    sum[pos]=1;
    Solve(Length,pos+1);
}
int main()
{
    cin>>NUM;
    int Case = 0;

    file.open("output.txt");
    while(NUM--)
    {
        memset(sum,0,sizeof(sum));
        int Length;

        Const=0;
        cin>>Length>>require;
        Case++;
        file<<"Case #"<<Case<<":\n";
        sum[0]=1;
        sum[Length-1]=1;
        Solve(Length,1);

    }

    file.close();
    return 0;
}
