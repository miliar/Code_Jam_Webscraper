#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int main()
{
    bool x_II[][4] = {1,0,1,0,
                      0,0,0,0,
                      1,0,1,0,
                      0,0,0,0};
    bool x_III[][4] = {1,1,1,1,
                       1,1,0,1,
                       1,0,0,0,
                       1,1,0,1};
    bool x_IV[][4] = {1,1,1,1,
                      1,1,1,1,
                      1,1,1,0,
                      1,1,0,0};
    ifstream f1;
    ofstream f2;
    f1.open("D-small-attempt0.in");
    f2.open("output.out");
    int c=1,t,x,r,col;
    f1>>t;
    while(c<=t)
    {
               f2<<"Case #"<<c++<<": ";
               f1>>x>>r>>col;
               if(x==1)f2<<"GABRIEL\n";
               else if(x==2)
               {
                    if(x_II[r-1][col-1])f2<<"RICHARD\n";
                    else f2<<"GABRIEL\n";
                    }
               else if(x==3)
               {
                    if(x_III[r-1][col-1])f2<<"RICHARD\n";
                    else f2<<"GABRIEL\n";
                    }
               else 
               {
                    if(x_IV[r-1][col-1])f2<<"RICHARD\n";
                    else f2<<"GABRIEL\n";
                    }
               }
    f1.close();
    f2.close();
    //system("pause");
    return 0;
    }
