#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("mag.out","w",stdout);

    int t;
    cin>>t;

    for(int k=1;k<=t;k++)
    {
        int c;
        cin>>c;
        int checking_array[17]={0};
        int a[4][4];
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>a[i][j];




        int d;
        cin>>d;

        int b[4][4];
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
             cin>>b[i][j];

         int cnt=0,com=0;

         for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                if(a[c][i]==b[d][j])
            {

                com=a[c][i];cnt++;
            }






         cout<<"Case #"<<k<<": ";
        if(cnt>1)
            cout<<"Bad magician!\n";
        else if(cnt==1)
            cout<<com<<endl;
        else if(cnt==0)
            cout<<"Volunteer cheated!\n";





    }
    return 0;
}
