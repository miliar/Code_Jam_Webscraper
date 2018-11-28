#include<iostream>
using namespace std;
#include<stdlib.h>
#include<math.h>
#include<stdio.h>

int cnt,hold;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;

    for(int i=1;i<=t;i++)
    {
        int r1,r2;
        int card1[10][10], card2[10][10];
        cnt=0;
        hold=0;

        cin>>r1;

        for(int j=1;j<=4;j++)
        {
            for(int t=1;t<=4;t++)
            {
                cin>>card1[j][t];
            }
        }

        cin>>r2;

        for(int j=1;j<=4;j++)
        {
            for(int t=1;t<=4;t++)
            {
                cin>>card2[j][t];
            }
        }

        for(int u=1;u<=4;u++)
        {
            int h=card1[r1][u];

            for(int g=1;g<=4;g++)
            {
                if(h == card2[r2][g])
                {
                    cnt++;
                    hold=h;
                }
            }
        }

        if(cnt == 1) cout<<"Case #"<<i<<": "<<hold<<endl;
        else if(cnt>1) cout<<"Case #"<<i<<": Bad magician!"<<endl;
        else if(cnt == 0) cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;

    }

    return 0;
}
