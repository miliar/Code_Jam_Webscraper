#include<fstream>
#include<string>
#include<cstdlib>
#include<sstream>
#include<cstdlib>
#include<iomanip>
#include<iostream>
using namespace std;
int main ()
{
    fstream fin;
    fstream fohash;
    fohash.open("A-small.out",ios::out);
    fin.open("A-small-attempt0.in",ios::in);
    char ch='0';
    int i=0,j=0,k=0,l=1,m=0,n = 1,a,b,c=1;
    fin.get(ch);
    while(fin && ch!=' ' && ch!='\n' && ch!='\t')
    {
        j = 10*j + (int)ch - 48;
        fin.get(ch);
    }
    fin.get(ch);
    for(;j>0;j--)
    {
        n=1;
        l=1;
        m=0;
        while(fin && ch!=' ' && ch!='\n' && ch!='/')
        {
            i = 10*i + (int)ch - 48;
            fin.get(ch);
        }
        fin.get(ch);
        while(fin && ch!=' ' && ch!='\n' && ch!='\t')
        {
            k = 10*k + (int)ch - 48;
            fin.get(ch);
        }
        fin.get(ch);
        l = k;
        while(l!=1)
        {
            if(l%2 == 0)
                l = l/2;
            else
            {
                m =1;
                break;
            }
        }
        if(m!=1)
        {
            while(i!=1)
            {
                i = i/2;
                n = 2*n;
            }
            cout<<n<<"\n";
            a = k/n;
            b=0;
            while(a!=1)
            {
                a = a/2;
                b++;
            }
            fohash<<"Case #"<<c++<<": "<<b<<"\n";
        }
        else
            fohash<<"Case #"<<c++<<": "<<"impossible\n";
        i = 0;
        k = 0;
    }
}
