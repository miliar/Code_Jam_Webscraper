#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
int main()
{
    int c, r1, r2, a1[4][4], a2[4][4], v=0, t=0;
    cin>>c;
    freopen("output1.txt","w",stdout);
    for (int i=1; i<=c; i++)
    {
        cin>>r1;
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            cin>>a1[j][k];
        }
        cin>>r2;
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            cin>>a2[j][k];
        }
        for (int j=0; j<4; j++)
        {
            for (int k=0; k<4; k++)
            {
                if ((a1[r1-1][j])==(a2[r2-1][k]))
                {
                    v=a1[r1-1][j];
                    t++;
                }
            }
        }
        cout<<"Case #"<<i<<": ";
        if (t==1)
        cout<<v;
        else if (t>1)
        cout<<"Bad magician!";
        else if (t==0)
        cout<<"Volunteer cheated!";
        v=0;
        t=0;
        cout<<'\n';
    }
    return 0;
}
