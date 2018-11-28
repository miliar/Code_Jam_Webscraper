
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    fstream x,y;
    x.open("A-small-attempt3.txt");
    y.open("P_A.txt");
    int n,t,i,j,c,sum,p;
    int a[20];
    x>>t;
    for(i=1;i<=t;i++)
    {

        x>>n>>p;
        for(j=n;j>=0;j--)
        {
            a[j]=p%10;
            p=p/10;
        }
        /*for(j=0;j<=n;j++)
        {
            cout<<a[j];
        }
        cout<<'\n';*/
        c=0;
        sum=a[0];
        for(j=1;j<=n;j++)
        {
            if((j>sum+c)&&(a[j]!=0))
                c+=(j-(sum+c));
            sum+=a[j];
            //cout<<c<<" ";
        }
        //cout<<"\n";
        //cout<<"Case #"<<i<<": "<<c<<"\n";
        y<<"Case #"<<i<<": "<<c<<"\n";
    }
    x.close();
    y.close();
    return 0;
}


