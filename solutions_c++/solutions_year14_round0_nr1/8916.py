#include <iostream>

using namespace std;
int nt;
int ans1[100];
int ans2[100];
int ans1ar[100][4][4];
int ans2ar[100][4][4];
char out[100];
//int cnt;
int match;
int numcmp;
int main()
{
   cin>>nt;
   for(int i=0;i<nt;i++)
   {
    cin>>ans1[i];
    for (int j=0;j<4;j++)
      { for(int k=0;k<4;k++)
       {cin>>ans1ar[i][j][k];
       }
      }
     cin>>ans2[i];
    for (int j=0;j<4;j++)
      { for(int k=0;k<4;k++)
       {cin>>ans2ar[i][j][k];
       }
      }  
   }
  // cout<< "out"<<ans1[0];
  /* for (int j=0;j<4;j++)
      { for(int k=0;k<4;k++)
       {cout<<ans2ar[0][j][k];
       }cout<<endl;
      }*/
   
   for(int i=0;i<nt;i++)
   {
       cout<<"Case #"<<i+1<<": ";
      int cnt=0; 
       for(int k=0;k<4;k++) // 1st array loop
       {numcmp=ans1ar[i][ans1[i]-1][k];
       for(int j=0;j<4;j++)
       {
        if(numcmp==ans2ar[i][ans2[i]-1][j])
        {cnt++;match=numcmp;}
       }
       }
      /* if(cnt==1){*out[i]=match;}
       if(cnt==0){*out[i]='Volunteer cheated!';}
       if(cnt>1){*out[i]='Bad magician!';}*/
       
       if(cnt==1){cout<<match;}
       if(cnt==0){cout<<"Volunteer cheated!";}
       if(cnt>1){cout<<"Bad magician!";}
       cout<<endl;
       
   }
   /*for(i=0;i<nt;i++)
   {
    cout<<"Case #"<<i+1<<": "<<out[i];   
   }*/
   return 0;
}
