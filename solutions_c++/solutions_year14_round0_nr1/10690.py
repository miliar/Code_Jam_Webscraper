#include<iostream>
#include<string>
#include<cstdio>

using namespace std;

int main()
{
        freopen( "A-small-attempt1.in", "r", stdin );
	    freopen( "output.txt", "w", stdout );
    int T,x,card[4][4],row1[4],row2[4],cnt;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cnt=0;
        cin>>x;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>card[j][k];

                if(x==j+1)
                {
                    row1[k]=card[j][k];
                }

            }
        }

        cin>>x;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>card[j][k];
                if(x==j+1)
                {
                    row2[k]=card[j][k];
                }

            }
        }

        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(row1[j]==row2[k])
                {
                    x=row1[j];
                    cnt++;
                }
            }
        }

        cout<<"Case #"<<i<<": ";

        if(cnt==0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }

        else if(cnt==1)
        {
            cout<<x<<endl;
        }

        else
        {
            cout<<"Bad magician!"<<endl;
        }
    }
return 0;
}
