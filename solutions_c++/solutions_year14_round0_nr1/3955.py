#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A.out","w",stdout);
    int x,y,A[4][4],B[4][4],sum[17],T,cont,sol;
    cin>>T;
    for(int k=1;k<=T;k++)
    {
        memset(sum,0,sizeof sum);
        cont = 0;
        cin>>x;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>A[i][j];
        cin>>y;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>B[i][j];

        x--;
        y--;
        for(int i=0;i<4;i++)
        {
            sum[A[x][i]]++;
            sum[B[y][i]]++;
        }
        for(int i=0;i<17;i++)
        {
            if(sum[i]==2)
            {
                sol = i;
                cont++;
            }
        }
        cout<<"Case #"<<k<<": ";
        if(cont == 1)
        {
            cout<<sol<<endl;
        }
        else if(cont > 1)
        {
            cout<<"Bad magician!"<<endl;
        }
        else
        {
            cout<<"Volunteer cheated!"<<endl;
        }
    }
    return 0;
}
