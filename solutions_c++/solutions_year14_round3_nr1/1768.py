#include<fstream>
#include<iostream>
#include<string.h>
#include<cmath>
using namespace std;
long long cmmdc(long long a,long long b)
{
    while(a!=b)
    {
        if(a>b)
            a=a-b;
        if(a<b)
            b=b-a;
    }
    return a;
}
int main()
{
    fstream f,g;
    f.open("A.in",ios::in);
    g.open("A.out",ios::out);
    long long T,ind,P,Q,ok,rez,nr,minim,i;
    char s[300];
    f>>T;
    for(ind=1; ind<=T; ind++)
    {
        g<<"Case #"<<ind<<": ";
        f>>s;
        P=Q=0;
        ok=0;
        for(i=0; i<strlen(s); i++)
        {
            if(ok==1)
                Q=Q*10+(s[i]-'0');
            if(s[i]!='/' && ok==0)
                P=P*10+(s[i]-'0');
            if(s[i]=='/')
                ok=1;
        }
        rez=cmmdc(P,Q);
        P=P/rez;
        Q=Q/rez;
        minim=100000000000000;

        while(P!=0)
        {
            if(Q<minim)
                minim=Q;
            P=P-1;
            if(P!=0)
            {
                rez=cmmdc(P,Q);
                P=P/rez;
                Q=Q/rez;
            }
        }
        nr=0;
        ok=0;
        while(minim!=1 && ok==0)
        {
            if(minim%2!=0)
                ok=1;
            minim=minim/2;
            nr++;

        }
        if(ok==1)
            g<<"impossible"<<'\n';
        else
            g<<nr<<'\n';


    }

}
