#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    int a[10][10],b[10][10],t,a1,a2,f2,f1;
    //freopen("A-small-attempt2.in","r",stdin);
    //freopen("i.txt","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>a1;
        for(int j=1;j<=4;j++)
        for(int l=1;l<=4;l++)
        cin>>a[j][l];
        cin>>a2;
        for(int j=1;j<=4;j++)
        for(int l=1;l<=4;l++)
        cin>>b[j][l];
        f1=0;
        for(int k=1;k<=4;k++)
        for(int m=1;m<=4;m++)
        {
            if(a[a1][k]==b[a2][m])
            {
                if(f1==0)
                f2=a[a1][k];
                f1++;
            }
        }
        if(f1==1)
        printf("Case #%d: %d\n",i,f2);
        else if(f1>1)
        printf("Case #%d: Bad magician!\n",i);
        else
        printf("Case #%d: Volunteer cheated!\n",i);
    }
    return 0;
}
