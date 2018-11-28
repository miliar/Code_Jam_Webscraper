#include<iostream>
#include<cstdio>
using namespace std;
void input(int A[4][4])
{
    int i,j;
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            cin>>A[i][j];
        }
    }
}
int main()
{
    int T,x,r1,r2,A[4][4],B[4][4],i,j,count,ans;
    cin>>T;
    for(x=1;x<=T;x++)
    {
        count=0;
        cin>>r1;
        input(A);
        cin>>r2;
        input(B);
        r1--;
        r2--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(A[r1][i]==B[r2][j])
                {
                    count++;
                    ans=j;
                }
            }
        }
        cout<<"Case #"<<x<<": ";
        switch(count)
        {
            case 0: cout<<"Volunteer cheated!\n";
            break;
            case 1: cout<<B[r2][ans]<<"\n";
            break;
            default: cout<<"Bad magician!\n";
            break;
        }
    }
}
