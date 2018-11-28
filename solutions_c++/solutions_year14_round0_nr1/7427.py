#include <iostream>

using namespace std;
int count1=0;
int Magic(int a[][4],int b[][4],int c,int d)
{
    int p1;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if((a[c-1][i])==(b[d-1][j]))
              {
                 count1++;
                 if(count1==1)
                   p1 = a[c-1][i];// return (a[c-1][i]);
              }
        }
    }
    return p1;
}


int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int a[4][4],b[4][4],c,d;
        cin>>c;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>d;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>b[i][j];
            }
        }
        int p = Magic(a,b,c,d);
        if(count1==1)
        {cout<<"Case #"<<i+1<<": "<<p<<endl;}
       if(count1>1) cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
       if(count1==0) cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
       count1 = 0;
    }
}
