#include<iostream>

using namespace std;

int main()
{
    int t,i,j,k,r1,r2,a[4][4],b[4][4],m,pos;
    cin>>t;
    t++;
    for(k=1;k<t;k++)
    {
        pos=-1;
        m=0;
        cin>>r1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>a[i][j];
        cin>>r2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            cin>>b[i][j];
        r1--;
        r2--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[r1][i]==b[r2][j])
                {
                    m++;
                    pos=i;
                    break;
                }
            }
        }
        if(m==1)
            cout<<"Case #"<<k<<": "<<a[r1][pos]<<"\n";
        else if(m==0)
            cout<<"Case #"<<k<<": Volunteer cheated!\n";
        else
            cout<<"Case #"<<k<<": Bad magician!\n";
    }
    return 0;
}
