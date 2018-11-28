#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int i,j,k;
    int t;
    ifstream cin("input.in");
    ofstream cout("output.out");
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int a,b;
        cin>>a;
        a--;

        int ar[4][4];
        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        cin>>ar[i][j];

        int r1[4];
        for(i=0;i<4;i++)
        r1[i]=ar[a][i];

         cin>>b;
         b--;

        for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        cin>>ar[i][j];

        int co=0,ans;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(ar[b][i]==r1[j])
                {ans=r1[j];co++;}
            }
        }

        if(co==1)
        cout<<"Case #"<<k<<": "<<ans<<"\n";
        else if(co==0)
        cout<<"Case #"<<k<<": Volunteer cheated!\n";
        else
        cout<<"Case #"<<k<<": Bad magician!\n";
    }
    return 0;
}
