#include<bits/stdc++.h>
//#include <fstream>
//#include <iostream>
using namespace std;
long long int cal(long long int N,int j)
{
    long long int arr[10]= {0},stat=0,i=1,temp,res;
    while(stat!=10)
    {
        temp=N*i;
        res=temp;
        i++;
        while(temp)
        {
            if(arr[temp%10]==0)
            {
                stat++;
                arr[temp%10]=1;
            }
            temp=temp/10;
        }
    }
    return res;
}
int main()
{
    long long int t,N,j;
    char fin[100],fout[100];
    cin>>fin>>fout;
    ofstream outfile;
    ifstream infile;
    outfile.open (fout);
    infile.open(fin);
    infile>>t;
    for(j=1; j<=t; j++)
    {
        infile>>N;
        if(N==0)
        {
            outfile<<"Case #"<<j<<": ";
            outfile<<"INSOMNIA"<<endl;
        }
        else
        {
            long long int res=cal(N,j);
            outfile<<"Case #"<<j<<": ";
            outfile<<res<<endl;
        }
    }
    outfile.close();
    infile.close();
    return 0;
}
