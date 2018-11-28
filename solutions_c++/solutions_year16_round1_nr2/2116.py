#include<bits/stdc++.h>
using namespace std;
int main(){
	long long int a,t,n,i,j,val,heights[2501],height[2501];
	 cin>>t;
	 val=0;
	 memset(heights,0,sizeof(heights));
	 memset(height,0,sizeof(height));
	 while(t--)
	 {
	 	val++;
	 	cin>>n;
	 	for(i=0;i<2*n-1;i++)
	 	{
	 		for(j=0;j<n;j++)
	 		{
	 			cin>>a;
	 			heights[a]+=1;
			 }
		 }
		 for(i=0;i<2501;i++)
		 {
		 	if(heights[i]%2!=0)
		 	{
		 		height[i]=1;
			 }
		 }
		 cout<<"Case #"<<val<<":";
		 for(i=0;i<2501;i++)
		 {
		 	if(height[i]==1)
		 	{
		 		cout<<" "<<i;
			 }
		 }
		 cout<<endl;
		 memset(heights,0,sizeof(heights));
		 memset(height,0,sizeof(height));
	 }
	 return 0;
}