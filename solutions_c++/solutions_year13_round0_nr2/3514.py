#include<iostream>
#include<sstream>
#include<cstdio>
#include<climits>
#include<cstring>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
#include<vector>
#include <algorithm> 
using namespace std;
int main()
{
int t,k;
cin>>t;
for(k=0;k<t;k++)
{      
    int i,j,m,n,arr[100][100]={0};
    int maxr[100]={0};
    int maxc[100]={0};
    bool flag=false;
    cin>>n>>m;
    for(i=0;i<n;i++)
     {   for(j=0;j<m;j++)
         {
            cin>>arr[i][j];
            if(arr[i][j]>maxr[i])
            maxr[i]=arr[i][j];
         }
     }
    for(i=0;i<n;i++)
     {   for(j=0;j<m;j++)
          if(arr[i][j]>maxc[j])
            maxc[j]=arr[i][j];
     }
   /* for(i=0;i<n;i++)
     {   for(j=0;j<m;j++)
          cout<<arr[i][j]<<" ";
          cout<<"\n";
     }*/
    for(i=0;i<n;i++)
     {   for(j=0;j<m;j++)
         { // cout<<arr[i][j]<<" r "<<maxr[i]<<" c "<<maxc[j];
            if((arr[i][j]>=maxr[i])||(arr[i][j]>=maxc[j]))
            flag=true;
            else { flag=false;break;
            }
         }
         if(flag==false)
         break;
     }
     if(flag==true)
     cout<<"Case #"<<k+1<<": YES\n";
     else  cout<<"Case #"<<k+1<<": NO\n";   
  }
  // system("pause");
}




