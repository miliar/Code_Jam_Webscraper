#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
long long int o,i=0;
int mat[5][5]={
                {0,1,2,3,4},
                {1,1,2,3,4},
                {2,2,-1,4,-3},
                {3,3,-4,-1,2},
                {4,4,3,-2,-1}
            };
string inp;
int calc1()
{
    int * arr = new int[o+1];
    arr[i]=inp[i]-103;
    for(i;i<o;i++)
    {
        if(arr[i]==1 && i==o-1)
        {
            return 1;
        }
        arr[i+1]=mat[abs(arr[i])][inp[i+1]-103];
        if(arr[i]<0)
            arr[i+1]=arr[i+1]*-1;
    }
    return 0;
}
int calc4()
{
    int * arr = new int[o+1];
    arr[i]=inp[i]-103;
    for(i;i<o;i++)
    {
        if(arr[i]==4)
        {
            if(i==o-1)
                return 1;
            else
            {
                i++;
                return calc1();
            }
        }
        arr[i+1]=mat[abs(arr[i])][inp[i+1]-103];
        if(arr[i]<0)
            arr[i+1]=arr[i+1]*-1;
    }
    return 0;
}
int calc3()
{
    int * arr = new int[o+1];
    arr[i]=inp[i]-103;
    for(i;i<o-1;i++)
    {
        if(arr[i]==3)
        {
            i++;
            return calc4();
        }
        arr[i+1]=mat[abs(arr[i])][inp[i+1]-103];
        if(arr[i]<0)
            arr[i+1]=arr[i+1]*-1;
    }
    return 0;
}
int calc2()
{
    int * arr = new int[o+1];
    i=0;
    arr[i]=inp[i]-103;
    for(i;i<o-1;i++)
    {
        if(arr[i]==2)
        {
            i++;
            return calc3();
        }
        arr[i+1]=mat[abs(arr[i])][inp[i+1]-103];
        if(arr[i]<0)
            arr[i+1]=arr[i+1]*-1;
    }
    return 0;
}
int main()
{
    int t;
    ifstream fin;
    ofstream fout;
    fout.open("output.txt",ios::out);
    fin.open("C-small-attempt0.in",ios::in);
    fin>>t;
    int l=t;
    long long int n,m;
    while(t--)
    {
        fin>>n>>m;
        o=n*m;
        string temp="";
        char in;
        inp="";
        for(int i=0;i<n;i++)
        {
            fin>>in;
            temp+=in;
        }
        for(int i=0;i<m;i++)
            inp+=temp;
        int flag=0;
        flag=calc2();
        fout<<"Case #"<<l-t<<": ";
        if(flag==1)
            fout<<"YES\n";
        else
            fout<<"NO\n";
    }
    fin.close();
    fout.close();
    return 0;
}
