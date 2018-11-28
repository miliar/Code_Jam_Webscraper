#include<iostream>
#include<cmath>
#include<fstream>
#include<string.h>
using namespace std;
int f1(char s1[250],char s2[250])
{
    char s3[250],s4[250],c;
    int n1=0,n2=0,nr,i,v1[250]={0},v2[250]={0},n,d;
    i=0;
    while(i<strlen(s1))
    {
        c=s1[i];
        n1++;
        nr=0;
        while(s1[i]==c)
        {
            nr++;
            i++;
        }
        s3[n1]=c;
        v1[n1]=nr;
    }

    i=0;
    while(i<strlen(s2))
    {
        c=s2[i];
        n2++;
        nr=0;
        while(s2[i]==c)
        {
            nr++;
            i++;
        }
        s4[n2]=c;
        v2[n2]=nr;
    }
    if(n1!=n2)
        return -1;
    for(i=1; i<=n1; i++)
        if(s3[i]!=s4[i])
            return -1;
    nr=0;
    for(i=1; i<=n1; i++)
    {
        d=v1[i]-v2[i];
        if(d<0)
            d=0-d;
        nr=nr+d;
    }

    return nr;
}
int main()
{
    fstream f,g;
    f.open("A.in",ios::in);
    g.open("A.out",ios::out);
    char s1[250],s2[250];
    int T,k,i,N,nr;
    f>>T;
    for(k=1; k<=T; k++)
    {
        g<<"Case #"<<k<<": ";
        f>>N;
        f.getline(s1,250);
        f.getline(s1,250);
        f.getline(s2,250);
        cout<<s1<<" "<<s2<<endl;

        nr=f1(s1,s2);
        if(nr==-1)
            g<<"Fegla Won";
        else
            g<<nr;
        g<<endl;

    }
}
