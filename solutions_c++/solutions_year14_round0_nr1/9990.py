#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int main()
{
    int i,j,rowa,rowb,tot,t;
    int board[6][6],res[5][5];

    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);

    cin>>tot;

    for(t=1;t<=tot;t++)
    {
        cin>>rowa;

        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>board[i][j];
                if(i==rowa)
                {
                    res[j][0]=board[i][j];
                    res[j][1]=i;
                }
            }
        }

        cin>>rowb;

        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>board[i][j];
                for(int k=1;k<=4;k++)
                {
                    if(res[k][0]==board[i][j])
                        res[k][2]=i;
                }
            }
        }

        int cnt=0,val;
        for(j=1;j<=4;j++)
        {
            if(rowb==res[j][2])
            {
                val=res[j][0];
                cnt++;
            }
        }

        cout<<"Case #"<<t<<": ";
        if(cnt==1)
            cout<<val;
        else if(cnt>1)
            cout<<"Bad magician!";
        else if(cnt==0)
            cout<<"Volunteer cheated!";
        cout<<endl;
    }


    fclose(stdin);
    fclose(stdout);
    return 0;
}
