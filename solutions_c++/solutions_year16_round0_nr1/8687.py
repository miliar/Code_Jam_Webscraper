#include <iostream>
#include <iostream>
#include <bits/stdc++.h>
#include <cstdlib>
#include <time.h>
using namespace std;
int main()
{
freopen("AL.in","r",stdin);
freopen("output_L1","w",stdout);

    int r,flag=0;
    long long int N,T,M,i,F,TN=1;
    cin>>T;
    while(T--)
    {
    flag=0;
    int a[10]={0};


    cin>>N;
    i=1;
    M=N;
    if(N==0)
    {
     cout<<"case #"<<TN<<": "<<"INSOMNIA"<<endl;

    }
    else{
    while(flag==0)
    {


    M=i*N;
    F=M;

    while(M>0)
    {
    r=M%10;
    a[r]=1;
    M=M/10;

    }

    flag=1;
    for(int j=0;j<10;j++)
    {
    if(a[j]==0)
    flag=0;
    }
    i++;
    }
    cout<<"case #"<<TN<<": "<<F<<endl;
    }



    TN++;
    }
    return 0;
}
