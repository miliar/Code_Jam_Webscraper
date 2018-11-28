#include<bits/stdc++.h>
#include<fstream>
using namespace std;
#define MAX 1562510


int main()
{
    freopen("C:\\Users\\Anick\\Desktop\\in.txt","r",stdin);
    freopen("C:\\Users\\Anick\\Desktop\\out.txt","w",stdout);

    int t;
    int A[5][5];
    int B[5][5];
    int a,b,c,ans,tc=1;

    cin>>t;
    while(t--)
    {
        cin>>a;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>A[i][j];

        cin>>b;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>B[i][j];

        c=0,ans=0;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                if(A[a][i]==B[b][j])
                {
                    c++;
                    ans=A[a][i];
                }

        cout<<"Case #"<<tc++<<": ";
        if(c==0)
            cout<<"Volunteer cheated!"<<endl;
        else if(c>1)
            cout<<"Bad magician!"<<endl;
        else
            cout<<ans<<endl;
    }
}
