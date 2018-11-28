#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.out");
    int m=0,i,j;
    int arr[501];
    fin>>m;
    arr[1]=1;
    for(i=2;i<=500;i++)
    arr[i]=2*i-1;
    for(j=1;j<=m;j++)
    {
    int r,t=0;
    fin>>r>>t;

    i=r+1;
    int sum=0,count=0;
    while(1)
    {

        sum+=arr[i];
        i=i+2;
        if(sum>t)
        break;
        count++;

    }
    fout<<"Case #"<<j<<": "<<count<<endl;
    }


}
