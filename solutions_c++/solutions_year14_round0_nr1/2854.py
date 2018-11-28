#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A1.in","r",stdin);
	freopen("A1.out","w",stdout);
	int first[5][5],sec[5][5],arr1[17],arr2[17],i,j,t,flag,row,res,ii;
	cin>>t;
	for(ii=1;ii<=t;ii++)
	{
          memset(arr1,0,sizeof(arr1));
          memset(arr2,0,sizeof(arr2));
          cin>>row;
          for(i=1;i<=4;i++)
          {
              for(j=1;j<=4;j++)
                  cin>>first[i][j];
          }
          for(i=1;i<=4;i++)
               arr1[first[row][i]]++;
          cin>>row;
          for(i=1;i<=4;i++)
          {
              for(j=1;j<=4;j++)
                  cin>>sec[i][j];
          }
          for(i=1;i<=4;i++)
               arr2[sec[row][i]]++;
          flag=0;
          for(i=1;i<=16;i++)
          {
                if(arr1[i]&&arr2[i])
                {
                     flag++;
                     res=i;
                }
          }
          cout<<"Case #"<<ii<<": ";
          if(flag==0)
             cout<<"Volunteer cheated!\n";
          if(flag==1)
             cout<<res<<"\n";
          if(flag>1)
             cout<<"Bad magician!\n";
      }
 }
             
