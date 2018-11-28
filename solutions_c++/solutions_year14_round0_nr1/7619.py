#include<iostream>
using namespace std;
int main()
{
    int t,n,a[5][5],b[5],i,j,k,n1,n2,cnt;
    cin>>t;

    for(k=1;k<=t;k++)
    {
        cin>>n1;
        for(i=1;i<5;i++)
            for(j=1;j<5;j++)
            cin>>a[i][j];

        for(i=1;i<5;i++)
            b[i]=a[n1][i];

        cin>>n2;
        for(i=1;i<5;i++)
            for(j=1;j<5;j++)
            cin>>a[i][j];
        cnt=0;
        for(i=1;i<5;i++)
        {

            for(j=1;j<5;j++)
            {
                if(a[n2][j]==b[i]){
                    cnt++;
                    n1=b[i];
                }
            }
        }
        cout<<"Case #"<<k<<": ";
        if(cnt==0)
            cout<<"Volunteer cheated!\n";
        else if(cnt==1)
            cout<<n1<<endl;
        else
            cout<<"Bad magician!\n";

    }
    return 0;
}
