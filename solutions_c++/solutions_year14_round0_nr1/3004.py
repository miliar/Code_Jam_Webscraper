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
int t,k,i,j;
cin>>t;
int arr1[4][4],arr2[4][4],r1,r2;
int hash[17];
for(k=1;k<=t;k++)
{   cin>>r1;
    for(i=0;i<17;i++)
    hash[i]=0;
    
	for(i=0;i<4;i++)
	{  for(j=0;j<4;j++)
	   {  
	     cin>>arr1[i][j];
         if(i==r1-1)
         hash[arr1[i][j]]=1;
	   }
	}
	
	cin>>r2;
	for(i=0;i<4;i++)
	{  for(j=0;j<4;j++)
	   cin>>arr2[i][j];
	}
	if(hash[arr2[r2-1][0]]==0 && hash[arr2[r2-1][1]]==0 && hash[arr2[r2-1][2]]==0 && hash[arr2[r2-1][3]]==0)
	{
	  cout<<"Case #"<<k<<": Volunteer cheated!\n";
    }
    else if(hash[arr2[r2-1][0]]==1 && hash[arr2[r2-1][1]]==0 && hash[arr2[r2-1][2]]==0 && hash[arr2[r2-1][3]]==0)
     cout<<"Case #"<<k<<": "<<arr2[r2-1][0]<<"\n";
    else if(hash[arr2[r2-1][0]]==0 && hash[arr2[r2-1][1]]==1 && hash[arr2[r2-1][2]]==0 && hash[arr2[r2-1][3]]==0)
     cout<<"Case #"<<k<<": "<<arr2[r2-1][1]<<"\n";
    else if(hash[arr2[r2-1][0]]==0 && hash[arr2[r2-1][1]]==0 && hash[arr2[r2-1][2]]==1 && hash[arr2[r2-1][3]]==0)
     cout<<"Case #"<<k<<": "<<arr2[r2-1][2]<<"\n";
    else if(hash[arr2[r2-1][0]]==0 && hash[arr2[r2-1][1]]==0 && hash[arr2[r2-1][2]]==0 && hash[arr2[r2-1][3]]==1)
     cout<<"Case #"<<k<<": "<<arr2[r2-1][3]<<"\n";
     else
     cout<<"Case #"<<k<<": Bad magician!\n";
}

}

