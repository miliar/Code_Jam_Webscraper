#include <iostream>

using namespace std;

int main()
{
    int q1[100][4][4],q2[100][4][4],ans[100][2],t,i,j,m,n,x,y,ctr=0;
    cin>>t;
    if((t<0)||(t>100))
    {
        exit(1);
    }
    for(x=1;x<=t;x++)
    {

    cin>>ans[x][0];
    if((ans[x][0]<1)||(ans[x][0]>4))
    {
        exit(1);
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>q1[x][i][j];
        }
    }
    cin>>ans[x][1];
    if((ans[x][1]<1)||(ans[x][1]>4))
    {
        exit(1);
    }
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>q2[x][i][j];
        }
    }
    }
    for(x=1;x<=t;x++)
    {
        ctr=0;

    for(m=0;m<4;m++)
    {
        for(n=0;n<4;n++)
        {
            if(q1[x][ans[x][0]-1][m]==q2[x][ans[x][1]-1][n])
            {
                y=q1[x][ans[x][0]-1][m];
                ctr++;
            }
        }
    }
    switch(ctr)
    {
        case 0:
            cout<<"\nCase #"<<(x)<<": Volunteer cheated!";
            break;
        case 1:
            cout<<"\nCase #"<<(x)<<": "<<y;
            break;
        case 2:
        case 3:
        case 4:
            cout<<"\nCase #"<<(x)<<": Bad magician!";
            break;
        default:
            cout<<"error";
    }
    }
    return 0;
}
