#include<iostream>

using namespace std;

#define local
#ifdef local
#include<fstream>
ifstream fin("A-small-attempt5.in");
ofstream fout("A-small-attempt4.out");
ofstream ff("data.out");
#define cin fin
#define cout fout
#endif // local

int main()
{
    int t,m,n;
    int i,j,k;
    cin>>t;
    for(i=1; i<=t; i++)
    {
        int a[5][5]= {0},b[5][5]= {0};
        int sam=0,s=0;
        cin>>m;
        for(j=1; j<=4; j++)
            for(k=1; k<=4; k++)
                cin>>a[j][k];
        cin>>n;
        for(j=1; j<=4; j++)
            for(k=1; k<=4; k++)
                cin>>b[j][k];
        for(j=1; j<=4; j++)
        {
            for(k=1; k<=4; k++)
            {
                if(a[m][j]==b[n][k])
                {
                    sam++;
                    s=j;
                }
            }
        }
        if(sam==1)
            cout<<"Case #"<<i<<": "<<a[m][s]<<endl;
        else if(sam>1)
            cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
        else
            cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
    }

    return 0;
}
