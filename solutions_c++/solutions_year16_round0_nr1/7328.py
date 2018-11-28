#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int *find1(int *a, int t)
{
    int i,j,p;
    while(t!=0)
    {
        p=t%10;
        a[p]=1;
        t=t/10;
    }
    return a;
}
int main()
{
    int i,j,a[10]= {0},p=0,n,t[100],sum=0,c=1,temp;
    ifstream fin;
    fin.open("input.in");
    ofstream fout;
    fout.open("output.txt");
    fin>>n;
    for(i=0; i<n; i++)
        fin>>t[i];
    for(i=0; i<n; i++)
    {
        if(t[i]==0)
        {
            if(i==0){
            fout<<"Case #"<<(i+1)<<": "<<"INSOMNIA";}
            else
              fout<<"\nCase #"<<(i+1)<<": "<<"INSOMNIA";
        }
        else
        {
            temp=t[i];
            while(1)
            {
                find1(a,t[i]);
                for(int j=0; j<10; j++)
                    sum=sum+a[j];
                if(sum==10)
                    break;
                t[i]+=temp;
                c++;
                sum=0;
            }
            p=c*temp;
            if(i==0){
            fout<<"Case #"<<(i+1)<<": "<<p;}
            else
              fout<<"\nCase #"<<(i+1)<<": "<<p;
            for(j=0; j<10; j++)
                a[j]=0;
            c=1;
        }

    }
}
