#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
     fstream f1,f2;
    f1.open("input.in",ios::in);
    f2.open("output.txt",ios::out);
    int t;
    f1>>t;
    int ans1,ans2,matches,magic,i,j,k,a[10][10],b[10][10];
    for(k=1;k<=t;k++)
    {
        matches=0;
        f1>>ans1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            f1>>a[i][j];
        f1>>ans2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            f1>>b[i][j];
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[ans1-1][i]==b[ans2-1][j])
                {
                    matches++;
                    magic=a[ans1-1][i];
                }
            }
        }
        if(matches==1)
              f2<<"Case #"<<k<<": "<<magic<<"\n";
        else if(matches==0)
            f2<<"Case #"<<k<<": Volunteer cheated!\n";
        else
            f2<<"Case #"<<k<<": Bad magician!\n";
    }
    return 0;
}
