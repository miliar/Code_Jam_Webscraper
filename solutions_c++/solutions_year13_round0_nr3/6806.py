#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;
int main()
{
    ifstream fi;
    ofstream fo;
    char file1[40], file2[20];
    int g, r, s=0, l=0, i, j;
    int a, b;
    int t, k;
    cout<<"\n enter input file name";
    cin>>file1;
    cout<<"\n enter output file name";
    cin>>file2;
    fi.open(file1);
    fo.open(file2);
    fi>>t;
    for(i=0; i<t; i++)
    {
             k=0;
             fi>>a>>b;
             a=int(ceil(sqrt(a)));
             b=int(sqrt(b));
             for(int j=a; j<=b; j++)
             {
                     s=0;
                     r=0;
                     g=j;
                     while(g!=0)
                     {
                                r=g%10;
                                g=g/10;
                                s=s*10+r;
                     }
                     if(s==j)
                     {
                             l=0;
                             r=0;
                             g=j*j;
                             while(g!=0)
                             {
                                        r=g%10;
                                        g=g/10;
                                        l=l*10+r;
                             }
                             if(l==j*j)
                             k++;
                     }
             }
             fo<<"Case #"<<i+1<<": "<<k<<"\n";
    }
    fi.close();
    fo.close();
    cout<<"\n work done";
    system("PAUSE");
    return 0;
}
           
