#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
 int t,i,j;
 int a,b;
 int v1[4][4],v2[4][4];
 cin>>t;
for(int k=1;k<=t;k++)
 {
     cin>>a;
	 for(i=0;i<4;i++)
	 {
	   for(j=0;j<4;j++)
	   {
	     cin>>v1[i][j];
		
	   }
	   //std::sort(v[i].begin(),v[i].end);
	 }
	
	 
	 cin>>b;
	 int m;
	 
	 for(i=0;i<4;i++)
	 {
	   for(j=0;j<4;j++)
	   {
	       cin>>v2[i][j];
		  }
	   //std::sort(v2[i].begin(),v2[i].emd());
	 }
	 
	 int co=0,sol;
	 for(i=0;i<4;i++)
	 {
	   for(j=0;j<4;j++)
	   {
	     if(v1[a-1][i]==v2[b-1][j])
	      { co++; sol=v1[a-1][i];}
	   }  
	 }
	
	 switch(co)
	 {
	  case 0: cout<<"Case #"<<k<<": Volunteer cheated!\n";
	          break;
	  case 1: cout<<"Case #"<<k<<": "<<sol<<"\n";        break;
	   default: cout<<"Case #"<<k<<": Bad magician!\n";
	            break;
	 }
	 
 }
 
}