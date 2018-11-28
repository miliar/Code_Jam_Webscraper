#include <iostream>

using namespace std;

int main()
{
    int test,i;
    cin>>test;
    for(i=1;i<=test;i++)
    {
       int a[4][4],x,b[4][4],y;
       int c[16]={0},count=0,m;
       cin>>x;
       for(int j=0;j<4;j++)
       {
           cin>>a[j][0]>>a[j][1]>>a[j][2]>>a[j][3];
       }
       cin>>y;
        for(int j=0;j<4;j++)
       {
           cin>>b[j][0]>>b[j][1]>>b[j][2]>>b[j][3];
       }
        for(int k=0;k<4;k++)
        {
            c[a[x-1][k]-1]++;
            c[b[y-1][k]-1]++;
        }
        for(int l=0;l<16;l++)
        {
            if(c[l]==2)
                { count++;
                m=l+1;
                }
            else
                continue;
        }
        if(count==1)
        {
            cout<<"Case #"<<i<<":"<<" "<<m<<endl;
        }
        if(count>1)
        {
           cout<<"Case #"<<i<<":"<<" "<<"Bad magician!"<<endl;
        }
        if(count==0)
        {
            cout<<"Case #"<<i<<":"<<" "<<"Volunteer cheated!"<<endl;
        }
    }
    return 0;
}
