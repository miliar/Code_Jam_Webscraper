#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
int main()
{
    ofstream fout("c:\\me5.txt");
    ifstream fin("c:\\A-small-attempt3.in");
    int num,i,j,k;
    double n=123,m=1,divide,rank,divider=1;
    for(i=0;i<40;i++)
    {
        divider*=0.5;
    }
    cin>>num;
    for(k=0;k<num;k++)
    {
    scanf("%lf/%lf",&n,&m);


    n=n/m;

    divide=n/divider;

    if(divide/(1024*1024)-int(divide/(1024*1024))<0.0000001)
    {
        rank=1;
        for(j=0;j<40;j++)
        {
            rank*=2;
            if(rank>divide)
            {

                fout<<"Case #"<<k+1<<": "<<40-j<<endl;
                break;
            }
        }

    }
    else
    fout<<"Case #"<<k+1<<": "<<"impossible"<<endl;
    //cout<<int(divide);
    //cout<<divide;

    }
    //cout<<m;
    return 0;



}
