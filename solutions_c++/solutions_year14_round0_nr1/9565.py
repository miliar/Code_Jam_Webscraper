#include<iostream>
#include<map>
#include<cstdio>
using namespace std;
int main()
{

    int t,n,k,e,i,j,q,s;
    int a[6][6];
    cin>>t;
    n=4;
    for (e=1;e<=t;e++)
    {
       map<int,int> mp;
       q=0;
       s=0;
       cin>>k;
       for (i=1;i<=n;i++)
        for (j=1;j<=n;j++)
        {
            cin>>a[i][j];
            if (i==k){mp[a[i][j]]++;}
        }
       cin>>k;
       for (i=1;i<=n;i++)
        for (j=1;j<=n;j++)
       {
          cin>>a[i][j];
          if (i==k){mp[a[i][j]]++;if (mp[a[i][j]]==2){s++;q=a[i][j];};}
       }
       cout<<"Case #"<<e<<": ";
       if (s==1){cout<<q<<endl;}
       if (s==0){cout<<"Volunteer cheated!"<<endl;}
       if (s>1){cout<<"Bad magician!"<<endl;}
    }
}
