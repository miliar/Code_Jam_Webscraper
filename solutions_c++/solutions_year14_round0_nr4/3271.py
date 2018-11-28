#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<set>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<cstring>
#include<stack>
using namespace std;

 
int main()
{
	freopen("inp.txt","r",stdin);
freopen("out2.txt","w",stdout);
  int t,co=1;
  cin>>t;
   while(t--)
   {
   	 double A[1009],B[1009];
   	  int n;
   	  cin>>n;
   	   for(int i=0;i<n;i++)
   	   cin>>A[i];
   	   for(int i=0;i<n;i++)
   	   cin>>B[i];
   	   sort(A,A+n);
   	   sort(B,B+n);
   	   int i=0,j=0,k1=0,k2=0;
   	   while(i<n&&j<n)
   	   {
   	   	if(A[i]<B[j])
   	   	{
   	   	  k1++;
   	   		i++;
   	   		j++;
   	   	}
   	   else
   	   	j++;
   	   	
   	   }
   	   cout<<"Case #"<<co<<": ";
   	   i=0;j=n-1;int k=0;
   	  
   	  vector<int>F(n,0);
   	  for(int i=0;i<n;i++)
   	  {
   	  	if(k<=j&&A[i]>B[k])
   	  	 {
   	  	 	k2++;
   	  	 	k++;
   	  	 }
   	  	 else if(k<=j&&A[i]<=B[k])
   	  	 {
   	  	 	j--;
   	  	 }
   	  	 
   	  }
   	  
   	  
   	   cout<<k2<<" "<<n-k1<<endl;
   	   co++;
   }
  return 0;
}
