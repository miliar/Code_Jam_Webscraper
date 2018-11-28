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
#define tr(container,it) \
 
int main()
{
  int t,co=1;
  freopen("inp.txt","r",stdin);
  freopen("out.txt","w",stdout);
  cin>>t;
   while(t--)
   {
   	 int a,b;
   	 int A[4][4],B[4][4];
   	  cin>>a;
   	   for(int i=0;i<4;i++)
   	   {
   	   	for(int j=0;j<4;j++)
   	   	 cin>>A[i][j];
   	   }
   	   cin>>b;
   	   for(int i=0;i<4;i++)
   	   {
   	   	for(int j=0;j<4;j++)
   	   	 cin>>B[i][j];
   	   }
   	  int k=0,l;
   	  for(int i=0;i<4;i++)
   	  {
   	  	 for(int j=0;j<4;j++)
   	  	  if(B[b-1][j]==A[a-1][i])
   	  	  {
   	  	   k++;
   	  	 l=B[b-1][j]   ;
   	    }
   	  }
   	  if(k==1)
   	  {
   	  	cout<<"Case #"<<co<<": "<<l<<endl;
   	  }
   	  else if(k==0)
   	  {
   	  	cout<<"Case #"<<co<<": "<<"Volunteer cheated!"<<endl;
   	  }
   	  else
   	     	cout<<"Case #"<<co<<": "<<"Bad magician!"<<endl;
   	     	co=co+1;
   }
  return 0;
}
