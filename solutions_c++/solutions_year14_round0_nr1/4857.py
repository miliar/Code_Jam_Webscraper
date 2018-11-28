#include <iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("xyzout10.txt","w",stdout);
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        int row1;
        cin>>row1;
        row1--;
        int a1[4][4];
        for(int i=0;i<4;i++)for(int j=0;j<4;j++)cin>>a1[i][j];
        int row2;
        cin>>row2;
        row2--;
        int a2[4][4];
        for(int i=0;i<4;i++)for(int j=0;j<4;j++)cin>>a2[i][j];
        int count=0;
        int temp;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a1[row1][i]==a2[row2][j]){count++;temp=a1[row1][i];}
            }
        }
        if(count==1)cout<<"Case #"<<test<<": "<<temp<<endl;
        else if(count>1)cout<<"Case #"   <<test<<": "<<"Bad magician!"<<endl;
        else cout<<"Case #"   <<test<<": "<<"Volunteer cheated!"<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
