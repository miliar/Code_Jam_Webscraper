#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;
int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int a[4][4],b[4][4],c[4],d[4],n,T,xemo,omex,contador,variable;
    cin>>T;
    for(int h=1;h<=T;h++)
    {
        contador=0;
        for(int u=1;u<=2;u++)
        {
            if(u==1){cin>>xemo;}
            else{cin>>omex;}
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                {
                    cin>>n;
                    if(u==1)
                    {
                        a[i][j]=n;
                        if(i==xemo-1){c[j]=a[i][j];}
                        if(a[i][j]>16){contador=contador+2;}
                    }
                    else
                    {
                        b[i][j]=n;
                        if(i==omex-1){d[j]=b[i][j];}
                        if(b[i][j]>16){contador=contador+2;}
                    }
                }
            }
        }
        for(int k=0;k<4;k++)
        {
            for(int e=0;e<4;e++)
            {
                if(c[k]==d[e])
                {
                    contador++;
                    variable=c[k];
                }
            }
        }
        if(contador==0){cout<<"Case #"<<h<<": Volunteer cheated!"<<endl;}
        if(contador==1){cout<<"Case #"<<h<<": "<<variable<<endl;}
        if(contador>1){cout<<"Case #"<<h<<": Bad magician!"<<endl;}
    }
    return 0;
}
