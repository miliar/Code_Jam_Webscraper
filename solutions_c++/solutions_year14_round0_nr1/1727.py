#include<iostream>
using namespace std;
int main()
{
 int g,t,i,j,z=0,ans1,sec;
 int arr[20][20],num[20],let[20];
 cin>>t;
 for(g=0;g<t;g++)
 {
  cin>>ans1;
  for(i=0;i<4;i++)
  { for(j=0;j<4;j++)
    {
     cin>>arr[i][j];
    } 
  }
  
  for(j=0;j<4;j++)
  num[j]=arr[ans1-1][j];

  cin>>ans1;
  for(i=0;i<4;i++)
  { for(j=0;j<4;j++)
    {
     cin>>arr[i][j];
    } 
  }
   
  for(j=0;j<4;j++)
  let[j]=arr[ans1-1][j];

  for(i=0;i<4;i++)
  {  for(j=0;j<4;j++)
       if(num[i]==let[j]) { sec=num[i];  z++;  }
  }

  if(z==1)
  cout<<"Case #"<<g+1<<": "<<sec<<endl;

  else if(z>1)
  cout<<"Case #"<<g+1<<": Bad magician!"<<endl;

  else
  cout<<"Case #"<<g+1<<": Volunteer cheated!"<<endl;

  z=0;
 }

 return 0;
}