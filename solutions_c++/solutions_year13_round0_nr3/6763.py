#include<stdio.h>
#include<iostream>
#include<fstream>
#include<math.h>
#define ll long long

using namespace std;

ll palindrome(ll k)
{
    ll x=k,j,sum=0;
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
    ll a,b;
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("output.txt");
    fin>>t;
    int p=0;
    while(t--)
    {
     p++;
     ll count=0;
     fin>>a>>b;
     for(ll i=sqrt(a);i<=sqrt(b)+1;i++)
     {
         if(palindrome(i))
         {
             ll k=i*i;
             if(k>=a&&k<=b){
             if(palindrome(k)) count++;}
         }
     }
     fout<<"Case #"<<p<<": "<<count;
     fout<<"\n";
    }
    return 0;
}