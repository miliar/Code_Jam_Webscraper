#include <iostream>
#include<fstream>
#include<cstdio>
using namespace std;

int nmax, cati,t,adauga;
char a[1100],b,c='0';


int main()
{
    int i,j;
    
    ifstream f("date.in");
    ofstream g("date.out");
    
    f>>t;
    for(i=1;i<=t;++i){
                          f>>nmax;
                          adauga=0;
                          f>>a;
                          cati=a[0]-c;
                          for(j=1;j<=nmax&&cati<nmax;++j){
                                                       if(cati<j)
                                                       {adauga+=(j-cati); cati=j+(a[j]-c);}
                                                       else
                                                       cati+=(a[j]-c);
                                                       }
                          g<<"Case #"<<i<<": "<<min(nmax,adauga)<<"\n";
                          }
                          
    

    system("pause");
    return 0;
}
