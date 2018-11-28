#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int cnt=0;
    while(cnt<t)
    {
                cnt++;
                int n,m;
                cin>>n>>m;
                int arr[n][m];
                
                for(int i=0;i<n;i++)
                for(int j=0;j<m;j++)
                cin>>arr[i][j];
                /*
                if((m==1)||(n==1))
                {cout<<"Case #"<<cnt<<": YES"<<endl; continue;}
                int g=0,l=0,flag1=0,flag2=0;
                for(int i=0;i<n;i++)
                {
                        for(int j=0;j<m-1;j++)
                        {
                                if((arr[i][j+1]>arr[i][j])&&(l==0)&&(g==0))
                                g++;
                                else if((arr[i][j+1]<arr[i][j])&&(g==0)&&(l==0))
                                l++;
                                else if((arr[i][j+1]>arr[i][j])&&(l==0)&&(g!=0))
                                continue;
                                else if((arr[i][j+1]<arr[i][j])&&(g==0)&&(l!=0))
                                continue;
                                else if((arr[i][j+1]<arr[i][j])&&(g==1)&&(l==0))
                                l++;
                                else if((arr[i][j+1]>arr[i][j])&&(l==1)&&(g==0))
                                g++;
                                else if((arr[i][j+1]>arr[i][j])&&(l==1)&&(g==1)&&(arr[i][j]<arr[i][j+1]))
                                {flag1=1;}
                                else if((arr[i][j+1]<arr[i][j])&&(l==1)&&(g==1)&&(arr[i][j]>arr[i][j+1]))
                                {flag1=1;}
                        }
                        l=0;g=0;
                }
                
                for(int j=0;j<m;j++)
                {
                        for(int i=0;i<n-1;i++)
                        {
                                if((arr[i+1][j]>arr[i][j])&&(l==0)&&(g==0))
                                g++;
                                else if((arr[i+1][j]<arr[i][j])&&(g==0)&&(l==0))
                                l++;
                                else if((arr[i+1][j]>arr[i][j])&&(l==0)&&(g!=0))
                                continue;
                                else if((arr[i+1][j]<arr[i][j])&&(g==0)&&(l!=0))
                                continue;
                                else if((arr[i+1][j]<arr[i][j])&&(g==1)&&(l==0))
                                l++;
                                else if((arr[i+1][j]>arr[i][j])&&(l==1)&&(g==0))
                                g++;
                                else if((arr[i+1][j]>arr[i][j])&&(l==1)&&(g==1)&&(arr[i][j]<arr[i][j+1]))
                                {flag2=1;}
                                else if((arr[i+1][j]<arr[i][j])&&(l==1)&&(g==1)&&(arr[i][j]>arr[i][j+1]))
                                {flag2=1;}
                        }
                        l=0;g=0;
                }
                if((flag1==1)&&(flag2==1))
                cout<<"Case #"<<cnt<<": NO"<<endl;
                else cout<<"Case #"<<cnt<<": YES"<<endl;
                
    }
    
   */
   
   /*int cnt1=0,cnt2=0,flag=0;
   for(int i=0;i<n;i++)
   {
           cnt1=0;cnt2=0;
           for(int j=0;j<m;j++)
           {
                   if(arr[i][j]==1)
                   cnt1++;
                   else
                   cnt2++;
           }
           if(cnt1==m)
           continue;
           else if(cnt2==m)
           continue;
           else
           for(int k=0;k<m;k++)
           {
                   if(arr[i][k]==1)
                   {
                                   for(int l=i;l<n;l++)
                                   {if(arr[l][k]==2)
                                   flag=1;}
                   }
           }
           
   }
   if(flag==1)
   cout<<"Case #"<<cnt<<": NO"<<endl;
   else cout<<"Case #"<<cnt<<": YES"<<endl;
*/
int flag=0,f1=0,f2=0;
for(int i=0;i<n;i++)
for(int j=0;j<m;j++)
{
        f1=0;f2=0;
        if(arr[i][j]==1)
        {
                        for(int x=0;x<m;x++)
                        {
                                if(arr[i][x]==2)
                                {f1= -1;
                                
                                break;}
                        }   
                        for(int x=0;x<n;x++)
                        {
                                if(arr[x][j]==2)
                                {f2=-1;
                                
                                break;}
                        }   
                        if((f1==-1)&&(f2==-1))
                        {
                                            flag=1;
                                            break;
                        }
        }
        
}
if(flag==1)
cout<<"Case #"<<cnt<<": NO"<<endl;
   else cout<<"Case #"<<cnt<<": YES"<<endl;
    
}

}
