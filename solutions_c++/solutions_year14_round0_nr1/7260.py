#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stdlib.h>
#include <queue>
#include <map>
#include <stack>
#define s(T) scanf("%d",&T)
#define ls(T) scanf("%ld",&T)
#define us(T) scanf("%u",&T)
#define uls(T) scanf("%lu",&T)
#define SIZE 65535
#define mx 4
using namespace std;
int main()
{
	int a[mx][mx],b[mx][mx],c[mx],d[mx],i,j,m,n,k,p,q,T,f1,f2;
	ifstream filei ("A-small-attempt0.in");
	ofstream fileo ("output.txt");
	if(filei.is_open())
    {
        while(filei>>p)
        {
            T=p;
            for(k=1; k<=T; ++k)
            {
                filei>>p;
                m=p-1;
                for(i=0; i<4; ++i)
                    for(j=0; j<4; ++j)
                {
                    filei>>p;
                    a[i][j]=p;
                    if(i==m)
                    {
                        c[j]=p;
                    }
                }
                filei>>p;
                n=p-1;
                for(i=0; i<4; ++i)
                    for(j=0; j<4; ++j)
                    {
                        filei>>p;
                        b[i][j]=p;
                        if(i==n)
                            d[j]=p;
                    }
                    //for(i=0; i<mx; ++i)
                      //  cout<<c[i]<<" "<<d[i]<<endl;
                f1=0;
                for(i=0; i<mx; ++i)
                {
                    q=c[i];
                    for(j=0; j<mx; ++j)
                    {
                        if(q==d[j])
                         {
                             ++f1;
                             if(f1==1)
                                f2=d[j];
                         }
                    }
                }
                cout<<f1;
                if(f1==1)
                    fileo<<"Case #"<<k<<": "<<f2<<endl;
                else if(f1==0)
                    fileo<<"Case #"<<k<<": Volunteer cheated!"<<endl;
                else
                    fileo<<"Case #"<<k<<": Bad magician!"<<endl;
            }
        }
    }
    else
        cout<<"Problem!";
	return 0;
}
