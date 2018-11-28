#include<iostream>
using namespace std;
int main()
{
    freopen("AB2.in","r",stdin);
	freopen("AB2.out","w",stdout);
	int t,res,flag,i,j,n,min,max,count,k;
	int index[105];
	char ch,arr[105][105];
	cin>>t;
	for(int ii=1;ii<=t;ii++)
	{
         res=0;
         flag=0;
         cin>>n;
         for(i=0;i<n;i++)
            index[i]=0;
         for(i=0;i<n;i++)
             cin>>arr[i];
         //for(i=0;i<n;i++)
           //  cout<<arr[i];
         for(i=0;arr[0][i]!='\0';)
         {
              ch=arr[0][i];
              min=1000;
              max=0;
              for(j=0;j<n;j++)
              {
                   k=index[j];
                   count=0;
                   while(arr[j][k]==ch)
                   {
                       count++;
                       k++;
                   }
                   index[j]=k;
                   if(count>max)
                      max=count;
                   if(count<min)
                      min=count;
                   if(count==0)
                   {
                       flag=1;
                       break;
                   }
                  
              }
              if(flag==1)
                  break;
               res=res+max-min;
              i=index[0];
         }
         for(i=1;i<n;i++)
         {
             if(arr[i][index[i]]!='\0')
             {
                 flag=1;
                 break;
             }
         }
         cout<<"Case #"<<ii<<": ";
         if(flag==1)
            cout<<"Fegla Won\n";
         else
            cout<<res<<"\n";
      }
 }
         
