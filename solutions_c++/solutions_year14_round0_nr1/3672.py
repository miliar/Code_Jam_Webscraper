#include<iostream>
using namespace std;
int main()
{
    freopen ("A-small-attempt0.in","r",stdin);
	freopen ("out.in","w",stdout);
    int t,ans1,ans2,ans,arr1[5][5],arr2[5][5];
    cin>>t;
    int x=1;
    while(x<=t)
    {
              cin>>ans1;
              for(int i=1;i<=4;i++)
              {
                      for(int j=1;j<=4;j++)
                      {
                              cin>>arr1[i][j];
                              }
                                 }
              cin>>ans2;
              for(int i=1;i<=4;i++)
              {
                      for(int j=1;j<=4;j++)
                      {
                              cin>>arr2[i][j];
                              }
                                 }
                           int ctr=0;
                                     for(int k=1;k<=4;k++)
                                     {
                                             for(int l=1;l<=4;l++)
                                             {
                                                     if(arr1[ans1][k]==arr2[ans2][l])
                                                     {ctr++;ans=arr1[ans1][k];break;}
                                             }    
                                     }
       if(ctr==1)
                 cout<<"Case #"<<x<<": "<<ans<<"\n";
              else if(ctr==0)
              cout<<"Case #"<<x<<": "<<"Volunteer cheated!"<<"\n";
              else
              cout<<"Case #"<<x<<": "<<"Bad magician!"<<"\n";
              x++;
              }


//system("pause");
return 0;
}
