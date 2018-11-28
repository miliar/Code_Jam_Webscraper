#include <fstream>
#include<iostream>
#include<string.h>
using namespace std;

int arr[10];

void digit(int n)
{
    int temp;
    while(n)
    {
        temp=n%10;
        arr[temp]=1;
        n=n/10;
    }
}
int check()
{

    for(int i=0;i<10;i++)
        {
           if(arr[i]==0)
             return 1;
        }
    return 0;
}
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.out");
    long long int t,n,k;
    fin>>t;
     for(int i=0;i<t;i++)
     {
         k=1;
         for(int j=0;j<10;j++)
            arr[j]=0;
       fin>>n;
       if(n==0)
       {
           fout<<"Case #"<<i+1<<": INSOMNIA\n";
           continue;

       }
       while(check()!=0)
       {
           digit(k*n);
           k++;
        }
        fout<<"Case #"<<i+1<<": "<<n*(k-1)<<endl;
     }
    return 0;
}
