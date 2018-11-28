#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include<cmath>
#include <sstream>
#include <algorithm>
#include <iomanip>
using namespace std;

int war(double* n,double* k,int c)
{
    int i=0,j=0,points=0;
    while(true)
    {
        if(k[j]>n[i])
        {
            points++;
            i++;
            j++;
        }
        else
        {
            j++;
        }
        if(i==c||j==c)
            break;
    }
    points=c-points;

    return points;
}

int deceitful(double* n,double* k,int c)
{
    int i=0,j=0,points=0;
    while(true)
    {
        if(k[j]<n[i])
        {
            points++;
            i++;
            j++;
        }
        else
        {
            i++;
        }
        if(i==c||j==c)
            break;
    }
    return points;
}


//bool order (double i,double j) { return (i>j); }


int  main()
{
    freopen("D-large.in",  "r", stdin);
     freopen("Dlarge.out",  "w", stdout);
   /* freopen("d.in",  "r", stdin);
    freopen("d.out",  "w", stdout);*/

    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        int n,resultD=0,resultW=0;
        cin>>n;
        double naomi[n],ken[n];
        for(int j=0; j<n; j++)
        {
            cin>>naomi[j];
        }
        sort(naomi,naomi+n);
        for(int j=0; j<n; j++)
        {
            cin>>ken[j];
        }
        sort(ken,ken+n);
        resultD=deceitful(naomi,ken,n);
        resultW=war(naomi,ken,n);

        cout<<"Case #"<<i<<": "<<fixed<< std::setprecision(7) << resultD<<" "<<resultW<<endl;
    }

    return 0;
}
