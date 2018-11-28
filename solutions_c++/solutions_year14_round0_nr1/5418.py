#include <iostream>
#include <stdio.h>
using namespace std;

int t;
int otgovor1,otgovor2;
int tablica1[5][5],tablica2[5][5];
bool used[17];
int chislo;
int br;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int i,j,k;

    cin>>t;

    for (i=1;i<=t;i++)
    {
        cin>>otgovor1;

        for (j=1;j<=4;j++)
        {
            for (k=1;k<=4;k++)
            cin>>tablica1[j][k];
        }

        cin>>otgovor2;

        for (j=1;j<=4;j++)
        {
            for (k=1;k<=4;k++)
            cin>>tablica2[j][k];
        }

        for (j=1;j<=16;j++)
        {
            used[j]=false;
        }

        for (j=1;j<=4;j++)
        {
            used[ tablica1[otgovor1][j] ]=true;
        }

        br=0;
        for (j=1;j<=4;j++)
        {
            if ( used[ tablica2[otgovor2][j] ] )
            {
                br++;
                chislo=tablica2[otgovor2][j];
            }
        }

        cout<<"Case #"<<i<<": ";

        if (br==0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        else if (br==1)
        {
            cout<<chislo<<endl;
        }
        else
        {
            cout<<"Bad magician!"<<endl;
        }
    }

    return 0;
}
