#include <stdio.h>
#include <fstream>
#include <string.h>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <map>
#define PI acos(-1.0)
#define M 1000005  //10^6
#define eps 1e-8
#define moo 1000000007
using namespace std;
int a[100][100];
int c[10];
int d[10];
int main ()
{
    int m,n,i;

    ofstream fout ("1.out");
    ifstream fin ("1.in");

    int T;
    fin>>T;
    int dd=T;
    while(dd--)
    {
        int n;
        fin>>n;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
                fin>>a[i][j];
        }
        for(int i=1;i<=4;i++)
            c[i]=a[n][i];

        fin>>n;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
                fin>>a[i][j];
        }
        for(int i=1;i<=4;i++)
            d[i]=a[n][i];
        int flag=0,pick;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(c[i]==d[j])
                {
                    flag++;
                    if(flag==1)
                        pick=c[i];
                    break;
                }
            }
        }
        if(flag==0)
            fout<<"Case #"<<T-dd<<": "<<"Volunteer cheated!"<<endl;
        else if(flag==1)
            fout<<"Case #"<<T-dd<<": "<<pick<<endl;
        else if(flag>1)
            fout<<"Case #"<<T-dd<<": "<<"Bad magician!"<<endl;
    }
    return 0;
}
