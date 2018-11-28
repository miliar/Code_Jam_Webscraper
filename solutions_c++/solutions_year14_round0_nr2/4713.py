#include<iostream>
#include<fstream>
#include<string>
#include<cstdlib>
#include<sstream>
#include<cstdlib>
#include<iomanip>
using namespace std;
int main ()
{
    fstream fin;
    fstream fohash;
    fohash.open("B_small.out",ios::out);
    fin.open("B-small-attempt0.in",ios::in);
    char ch='0';
    int i=0,j=0,k,l=1;
    double a = 0,b = 0.1,c=2.0,a1 = 0,a2 = 0,t = 0.0,n=0;
    cout<<fixed;
    fohash<<fixed;
    fin<<fixed;
    cout<<setprecision(7);
    fin<<setprecision(7);
    fohash<<setprecision(7);
     while(fin && ch!=' ' && ch!='\n' && ch!='\t')
        {
            j = 10*j + (int)ch - 48;
            fin.get(ch);
        }
        fin.get(ch);
        for(;j>0;j--)
        {
            while(fin  && ch!=' ' && ch!='\n' && ch!='\t')
        {
            if(i==0&&ch!='.')
                a = 10*a + (int)ch - 48;
            else if(i==0 && ch=='.')
                i = 1;
            else
            {
                a = a + ((int)ch - 48)*b;
                b = b/10;
            }
            fin.get(ch);
        }
        cout<<a<<" ";
        b = 0.1;
        i = 0;
        fin.get(ch);

        while(fin&&ch!=' '&&ch!='\n'&&ch!='\t')
        {
            if(i==0 && ch!='.')
            {
                a1 = 10*a1 + (int)ch - 48;
            }
            else if(i==0 && ch=='.')
                i = 1;
            else
            {
                a1 = a1 + ((int)ch - 48)*b;
                b = b/10;
            }
            fin.get(ch);
        }
        cout<<a1<<" ";
        b = 10;
        i = 0;
        fin.get(ch);
        while(fin&&ch!=' '&&ch!='\n'&&ch!='\t')
        {
            if(i==0&&ch!='.')
                a2 = 10*a2 + (int)ch - 48;
            else if(i==0 && ch=='.')
                i = 1;
            else
            {
                n=((int)ch - 48)/b;
                a2 = a2+n;
                b = b*10;
            }
            fin.get(ch);
        }
        cout<<setprecision(6)<<a2<<"\n";
        b = 0.1;
        i = 0;
        fin.get(ch);

        while((a/c + a2/(c+a1)) < (a2/c))
        {
            t = a/c+t;
            c = c + a1;
        }
        t = t + a2/c;
        fohash<<"case #"<<l<<": "<<t<<"\n";
        l++;
        a = 0;
        a1 = 0;
        a2 = 0;
        t = 0;
        c = 2;
        }
    fin.close();
    fohash.close();
    return(0);
}
