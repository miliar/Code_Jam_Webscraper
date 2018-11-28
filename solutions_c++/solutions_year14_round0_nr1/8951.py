#include<iostream>
using namespace std;
int main()
{
    int t;
    int c,m, a[4][4], b[4][4], c1,c2;
    cin>>t;
    for(int i = 0; i < t; i++)
    {
        c = 0;
        cin>>c1;
        for(int j = 0; j < 4; j++)
            cin>>a[j][0]>>a[j][1]>>a[j][2]>>a[j][3];
        cin>>c2;
        for(int j = 0; j < 4; j++)
            cin>>b[j][0]>>b[j][1]>>b[j][2]>>b[j][3];
        for(int j = 0; j <4; j++)
            {
                for(int k = 0; k< 4; k++)
                {
                    cout<<a[c1-1][j]<<"\t"<<b[c2-1][k]<<endl;
                    if(a[c1-1][j] == b[c2-1][k])
                    {
                        c++;
                        m = k;
                    }
                }
            }
        cout<<"Case #"<<i+1<<": ";
        if(c == 0)
            cout<<"Volunteer cheated!\n";
        else if( c==1)
            cout<<b[c2-1][m]<<endl;
        else if( c>1)
            cout<<"Bad magician!\n";
    }
return 0;
}
