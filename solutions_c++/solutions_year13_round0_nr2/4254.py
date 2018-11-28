#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<fstream>
#include<string>
using namespace std;
int findmax(int *a,int n)
{
    int i,r=0;
    for(i=0;i<n;i++)
    {
        if(a[i]>r)
        {
            r=a[i];
        }
    }
    return r;
}
int main()
{
    int n,m,**a,**b,**c;
    string s;
    ifstream fin;
    ofstream fout;
    fin.open("cji2.txt");
    fout.open("cjo2.txt");
    int t,i,j,k,flag=0,temp;
    fin>>t;
    getline(fin,s);
    for(k=0;k<t;k++)
    {
        flag=0;
        fin>>n>>m;
        getline(fin,s);
        a=new int*[n];
        c=new int*[n];
        b=new int*[m];
        for(i=0;i<n;i++)
        {
            c[i]=new int[m];
            a[i]=new int[m];
        }
        for(i=0;i<m;i++)
        {
            b[i]=new int[n];
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                fin>>a[i][j];
                c[i][j]=100;
            }
            getline(fin,s);
        }

        for(i=0;i<n;i++)
        {
            temp=findmax(a[i],m);
            for(j=0;j<m;j++)
            {
                if(a[i][j]>=temp);
                {
                    c[i][j]=100;
                    c[i][j]-=100-temp;
                }
            }
        }

        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                b[j][i]=a[i][j];
            }
        }

        for(i=0;i<m;i++)
        {
            temp=findmax(b[i],n);
            for(j=0;j<n;j++)
            {


                if(a[j][i]>=temp)
                 {

                     c[j][i]=100;
                    c[j][i]-=100-temp;
                 }
            }
        }

        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(a[i][j]!=c[i][j])
                {
                    flag=1;
                }
            }
        }
        if(flag==1)
        {
            fout<<"Case #"<<k+1<<": "<<"NO"<<endl;

        }
        else
        {
            fout<<"Case #"<<k+1<<": "<<"YES"<<endl;
        }
    }
    fout.close();
    return 0;
}
