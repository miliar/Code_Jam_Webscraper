#include <iostream>

using namespace std;

int main()
{
    int t;
    int con;
    int z;
    int ch1,ch2;
    int a[4][4];
    int b[4][4];
    cin>>t;
    for (int i=0; i<t; i++)
    {
        cin >>ch1;
        for (int k=0; k<4; k++)
            for(int j=0; j<4; j++)
                cin >>  a[k][j];
        cin >>ch2;
        for (int k=0; k<4; k++)
            for(int j=0; j<4; j++)
                cin >>  b[k][j];
        //a[ch1] b[ch2]
        con=0;
        for (int k=0; k<4; k++)
        {

            for (int j=0; j<4; j++)
            {
                if (a[ch1-1][k]==b[ch2-1][j])
                {
                    con++;
                    z=k;
                }

            }
        }
        if (con==1)
            cout<<"Case #"<<i+1<<": "<<a[ch1-1][z]<<endl;
        else if(con>1)
            cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
        else
            cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
