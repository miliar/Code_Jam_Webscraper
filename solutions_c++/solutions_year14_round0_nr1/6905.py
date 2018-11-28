# include <iostream>

using namespace std;

int main()
{
    int n;

    cin>>n;
    for (int k=1;k<=n;k++)
    {


    int x,y,a[4][4],b[4][4];
    cin>>x;
    for (int i=0;i<4;i++)
    {
        for (int j=0;j<4;j++)
            cin>>a[i][j];
    }
    cin>>y;
    for (int i=0;i<4;i++)
    {
        for (int j=0;j<4;j++)
            cin>>b[i][j];
    }

    int flag=0,card=-1;

    for (int i=0;i<4;i++)
    {
        for (int j=0;j<4;j++)
        {

            if (a[x-1][i]==b[y-1][j])
            {card=a[x-1][i];flag++;}
        }

    }
    cout<<"\nCase #"<<k<<": ";
    if (card==-1)
            cout<<"Volunteer cheated!";
    else if(flag>1)
            cout<<"Bad magician!";
    else
        cout<<card;
    }
}




