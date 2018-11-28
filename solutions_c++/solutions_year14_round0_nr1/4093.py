#include <iostream>
#include<cstring>
using namespace std;
 
int main() {
   int t,i,j,k,l,count=0,element;
   cin>>t;
   int arr[4][4],brr[4][4],vis[20];
 
   for(i=1;i<=t;i++)
   {
   	   memset(vis,0,sizeof(vis));
   	   cin>>l;
   	   for(j=0;j<4;j++)
   	   {
   	   	  for(k=0;k<4;k++)
   	   	   {
   	   	   	  cin>>arr[j][k];
   	   	   	  //cout<<arr[j][k]<<" ";
   	   	   	  if(j==l-1)
   	   	   	   vis[arr[j][k]]=1;
 
   	   	   }
   	   	  // cout<<endl;
   	   }
   	   cin>>l;
   	   count=0;
   	  // for(i=0;i<20;i++)
   	  // cout<<i<<" "<<vis[i]<<endl;
 
   	   for(j=0;j<4;j++)
   	   {
   	   	   for(k=0;k<4;k++)
   	   	    {
   	   	    	 cin>>brr[j][k];
   	   	    //	 cout<<brr[j][k]<<" ";
   	   	    	 if(j==l-1&&vis[brr[j][k]]==1)
   	   	    	 {
   	   	    	 	count++;
   	   	    	 	element=brr[j][k];
   	   	    	 }
 
   	   	    }
   	   	   // cout<<endl;
 
   	   }
   	   if(count==0)
   	   cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
   	   if(count==1)
   	   cout<<"Case #"<<i<<": "<<element<<endl;
   	   if(count>1)
   	   cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
   }
	return 0;
}