#include<iostream>
#include<climits>
#include<cstdio>
#include<set>
#include<cstring>
#include<map>
#include<cmath>
#include<vector>
using namespace std;

int main()
{
int t,k,i,j,n,s;
double arr1[1001],arr2[1001];
int y,z;
cin>>t;
for(k=1;k<=t;k++)
{    
     y=0;z=0;
     cin>>n;
     for(i=0;i<n;i++)
     cin>>arr1[i];
     for(i=0;i<n;i++)
     cin>>arr2[i];
     sort(arr1,arr1+n);
     sort(arr2,arr2+n);
     
   /*  for(i=0;i<n;i++)
     cout<<arr1[i]<<"  ";
     cout<<"\n";
     for(i=0;i<n;i++)
     cout<<arr2[i]<<"  ";
     cout<<"\n";
  */
     j=n-1;
     for(i=n-1;i>=0;i--)
     {
     	if(arr1[i]>arr2[j])
     	{ z++;}
     	else {
     		j--;
     	}
     }

     i=0;j=n-1;
     s=0;
     for(i=0;i<n;i++)
     {  
       // cout<<i<<" "<<j<<" "<<arr1[i]<<" "<<arr2[j]<<"\n";
     	if(arr1[i]<arr2[j] && arr1[i]<arr2[s])
     	{ j--;
		}
		else if(arr1[i]<arr2[j] && arr1[i]>arr2[s])
        {s++;
         y++;
        }
        else y++;
     }
    // printf("Case #%d: %.7f\n",k,ftime);
 //   Case #1: 0 0
     cout<<"Case #"<<k<<": "<<y<<" "<<z<<"\n";
}
}

