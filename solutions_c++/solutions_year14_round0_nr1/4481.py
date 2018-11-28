#include<cstdio>
#include<iostream>
#include<algorithm>

using namespace std;
int main()
{
    int t,ans1,ans2,p0[5][5],p1[5][5],i,j,count1,ans;
    cin>>t;
    for(int k=1;k<=t;k++)    {
       cin>>ans1;

       for(i=1;i<5;i++)
       {
           for(j=1;j<5;j++)
           {
               cin>>p0[i][j];
           }
       }

        cin>>ans2;
        for(i=1;i<5;i++)
       {
           for(j=1;j<5;j++)
           {
               cin>>p1[i][j];
           }
       }

       count1=0;
        for(i=1;i<5;i++)
       {
           for(j=1;j<5;j++)
           {
               if(p0[ans1][i]== p1[ans2][j])
               {
                   count1++;
                   ans=p0[ans1][i];
                   break;
               }
           }
       }

  cout<<"Case #"<<(k)<<": ";
       if(count1==0)
        cout<<"Volunteer cheated!";
       else if(count1==1)
        cout<<ans;
        else
            cout<<"Bad magician!";

            cout<<endl;
    }
    return 0;
}

