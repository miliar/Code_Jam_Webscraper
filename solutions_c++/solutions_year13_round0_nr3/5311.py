#include<stdio.h>
#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int palindrome(int k)
{
    int x=k,j,sum=0;
    while(x>0)
    {
        j=x%10;
        sum=sum*10+j;
        x/=10;
    }
    if(sum==k) return 1;
    else return 0;
}

int main()
{
    int t;
    int a,b;
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    fin>>t;
    int p=0;
    while(t--)
    {
     p++;
     int count=0;
     fin>>a>>b;
     for(int i=a;i<=b;i++)
     {
         if(palindrome(i))
         {
             int k=sqrt(i);
             if((k*k==i)&&palindrome(sqrt(i))) count++;
         }
     }
     fout<<"Case #"<<p<<": "<<count;
     fout<<"\n";
    }
    return 0;
}