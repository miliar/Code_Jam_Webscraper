#include<iostream>
#include<fstream>

using namespace std;
fstream f1,f2;
int main()
{
    int a[100][100],b[10000],c[10000],l,m,n,k,o,i,j,u=0,cas,s,key,flag=0;
    f1.open("B-large.in",ios::in);
    f2.open("outo.out",ios::out);
    f1>>cas;

while(f1)
{l=-1;

    f1>>m;
    f1>>n;
    s=m*n;
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            f1>>a[i][j];
        }
    }
    for(i=0;i<s;i++)
    {
        b[i]=0;
        c[i]=0;
    }

        for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {   l++;
            key=a[i][j];
            for(k=0;k<n;k++)
            {
                if(a[i][k]<=key)
                b[l]++;
            }
            for(o=0;o<m;o++)
            {
                if(a[o][j]<=key)
                c[l]++;
            }


    }
}
for(i=0;i<s;i++)
{
    if(b[i]==n||c[i]==m)
    flag=1;
    else
    {
        flag=0;
        break;
    }

}
 if(u<cas)
    {


 f2<<"Case #"<<u+1;
 f2<<": ";
if(flag==1)
f2<<"YES";
else
f2<<"NO";
 f2<<"\n";
 u++;
    }

}
return 0;
}


