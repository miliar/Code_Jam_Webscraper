#include <iostream>

using namespace std;


int main()
{
   int a[4][4],ip_1,ip_2,op,b[16],ans;
   cin>>ip_1;
   for(int k=0;k<ip_1;k++)
   {
       op=0;
       cin>>ip_2;
       
   for(int i=0;i<4;i++)
   { for(int j=0;j<4;j++)
    {
       cin>>a[i][j];
        b[a[i][j]-1]=0;
       if(i==ip_2-1)
       b[a[i][j]-1]=1;
    }
   }
    
    
    cin>>ip_2;
       
   for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
    {
       cin>>a[i][j];
        if(i==ip_2-1)
       if(++b[a[i][j]-1]==2)
       {
           op++;
           ans=a[i][j];
       }
    }
    if(op>1)
    cout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
    else if(op==1)
    cout<<"Case #"<<k+1<<": "<<ans<<endl;
    else 
    cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;
   }
   
   return 0;
}

