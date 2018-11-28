#include<iostream>
#include<stdio.h>
using namespace std ;

int magic(int);

main()
{
    int i,c=1;
    freopen("in.in","r",stdin) ;
    freopen("aout.txt","w",stdout) ;
    cin >> i;
    int A[i];
    while(i)
    {
        A[c]=magic(c);
        i--;
        c++;
    }
    for(i=1;i<c;i++)
    {
        if(A[i]<0)
            cout << "\nCase #"<<i<<": "<< (-A[i]);
        else if(A[i]>1)
            cout << "\nCase #"<<i<<": Bad magician!";
        else if (A[i]==0)
            cout << "\nCase #"<<i<<": Volunteer cheated!";
    }
}

int magic(int c)
{
    int X[4][4],i,j,l,Y[4],k=0,m,n;
    cin >> n;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            cin >> X[i][j];
    for(j=0;j<4;j++)
        Y[j]=X[n-1][j];
    cin >> n;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
            cin >> X[i][j];
    for(j=0;j<4;j++)
    {
        for (l=0;l<4;l++)
        {
          if(Y[j]==X[n-1][l])
          {
            k++;
            m=Y[j];
          }
        }
    }
    if(k==1)
       return (-m);
    else if(k>1)
        return 2;
    else if (k==0)
        return 0;
}





