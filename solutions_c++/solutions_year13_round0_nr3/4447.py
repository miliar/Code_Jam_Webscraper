/*
ID: m.maher1
PROG: palsquare
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include<algorithm>
#include<string.h>
#include<sstream>
using namespace std;
int main()
{
    ofstream cout ("palsquare.out");
    ifstream cin ("C-small-attempt0.in");
    int t,counter=0;
    cin>>t;
    while(t--)
    {counter++;
    long long base,i,j,n,arr[301],k,j1,k1,low,high;
    cin>>low>>high;
    int sum=0;
    base=10;
    for(i=1;i<100;i++)
    {
        j=i*i;
        j1=i;
        n=1;
        k=0;k1=0;
        long long miz;
        while(j!=0)
        {
            miz=j%base;
            if(miz>9)n*=10;
            k+=(n*(j%base));
            n*=10;
            j/=base;
        }
        n=1;
        while(j1!=0)
        {
            miz=j1%base;
            if(miz>9)n*=10;
            k1+=(n*(j1%base));
            n*=10;
            j1/=base;
        }
        string str1,str2;
        ostringstream convert;
        convert << k;
        str1 = convert.str();
        str2=str1;
        reverse(str1.begin(),str1.end());
        if(str1==str2){
             str1,str2;
        ostringstream convert;
        convert << k1;
        str1 = convert.str();
        str2=str1;
        reverse(str1.begin(),str1.end());
        if(str1==str2){

            if(k>=low&&k<=high)
            sum++;//cout<<k<<endl;
            }}
    }
    cout<<"Case #"<<counter<<": "<<sum<<endl;

    }
    return 0;
}
