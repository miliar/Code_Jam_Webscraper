#include<iostream>
using namespace std;
int main()
{
int t;
cin>>t;for(int o=0;o<t;o++)
{
                 int a;
                 cin>>a;
                 int arr[4][4];int check1[4];
                 for(int i=0;i<4;i++)
                 {for(int j=0;j<4;j++)
                 {cin>>arr[i][j];
                     if(i==a-1)
                     {check1[j]=arr[i][j];} 
				   }
                         }
                 int b;
                 cin>>b;
                 int arr2[4][4];int check2[4];
                 for(int i=0;i<4;i++)
                 {for(int j=0;j<4;j++)
                 {cin>>arr2[i][j];
                        if(i==b-1)
                     {check2[j]=arr2[i][j];  }
						}
                         }
                 
                 int count=0;int index=0;
                  for(int i=0;i<4;i++)
                 {for(int j=0;j<4;j++)
                 {if(check1[i]==check2[j])
                	 {count=count+1;index=check1[i];}
                          }
                          }
                 
                 if(count==1)
                 cout<<"Case #"<<o+1<<": "<<index<<endl;
                 else
                 if(count>1)
                 cout<<"Case #"<<o+1<<": Bad magician!"<<endl;
                 else
                 if(count==0)
                 cout<<"Case #"<<o+1<<": Volunteer cheated!"<<endl;
                 }


}
