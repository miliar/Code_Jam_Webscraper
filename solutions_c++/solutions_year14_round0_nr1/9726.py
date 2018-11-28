#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int mag[4][4],mag2[4][4],frst,scnd,t,cntr,which;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        cntr=0;
        cin >> frst;

        for(int r=0;r<4;r++)
            for (int k=0;k<4;k++)
            cin>>mag[r][k];

        cin>>scnd;
        for(int r=0;r<4;r++)
            for (int k=0;k<4;k++)
            cin>>mag2[r][k];
frst--;scnd--;
        for(int r=0;r<4;r++)
            for (int k=0;k<4;k++)
            {//cout <<mag[frst][r]<<" : "<< mag2[scnd][k]<<endl;
                if (mag[frst][r]==mag2[scnd][k])
                {
                    cntr++;
                    which=mag[frst][r];
                }

            }
    if (cntr==0)
        cout <<"Case #"<<i<<": " <<"Volunteer cheated!"<<endl;
    else if (cntr==1)
        cout <<"Case #"<<i<<": " <<which<<endl;
    else if (cntr>1)
        cout <<"Case #"<<i<<": " <<"Bad magician!"<<endl;
    }


    return 0;
}
