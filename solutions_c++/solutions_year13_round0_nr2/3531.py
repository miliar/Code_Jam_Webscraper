#include <iostream>
#include <fstream>
using namespace std;

int main()
{   ofstream file1("output.txt");
    ifstream file("B-large.in");
    int p,q,n,k;
    file>>n;
    for(int s=1;s<=n;s++)
    {file>>p;
    file>>q;
    int a[p][q];
    for(int i=0;i<=p-1;i++)
    for(int j=0;j<=q-1;j++)
    file>>a[i][j];
    int z,x,y;
     y=0;
       for(int i=0;i<=p-1;i++)
    for(int j=0;j<=q-1;j++)
    {z=x=0;
     k=a[i][j];
    for(int m=0;m<=q-1;m++)
    {if(k<a[i][m])
    {z++;}}
    for(int m=0;m<=p-1;m++)
    {if(k<a[m][j])
    {x++;}}
    if(x!=0&&z!=0)
    {y++;}
          }
        if(y==0)
        {file1<<"Case #"<<s<<": YES"<<"\n";}
        else{file1<<"Case #"<<s<<": NO "<<"\n";}
          }

     }

