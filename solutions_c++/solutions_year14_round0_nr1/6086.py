#include <iostream>
using namespace std;
int main ()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,k1,k2,a[5][5],b[5][5],c,h;
    cin>>t;
    for (int i=0;i<t;i++)
    {
        cin>>k1;
        for (int j1=1;j1<=4;j1++)
        for (int j2=1;j2<=4;j2++)
        cin>>a[j1][j2];
        cin>>k2;
        for (int j1=1;j1<=4;j1++)
        for (int j2=1;j2<=4;j2++)
        cin>>b[j1][j2];
        c=0;
        for (int j1=1;j1<=4;j1++)
        for (int j2=1;j2<=4;j2++)
        {
            if (a[k1][j1]==b[k2][j2]) 
            {
               c++;
               if (c==1) h=a[k1][j1];
               }
            }
        cout<<"Case #"<<i+1<<": ";
        if (c==0) cout<<"Volunteer cheated!";
        else if (c==1) cout<<h;
        else cout<<"Bad magician!";
        cout<<endl;
        }
    fclose(stdin);
    fclose(stdout);
    }
