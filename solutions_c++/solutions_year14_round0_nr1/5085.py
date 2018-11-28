#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	int T,po,a,b,mat[4][4],i,j,k,num1[4],pos1[4],pos2[4],num2[4];
	int count=0,res,hash[17],noc=0;
	cin>>T;
	for(noc=1;noc<=T;noc++)
	{
		cin>>po;
		for(i=0;i<4;i++)
		{
			num1[i]=0;
			num2[i]=0;
		}
		for(i=0;i<17;i++)
		{
			hash[i]=0;
		}
		for(i=0;i<4;i++)
		 for(j=0;j<4;j++)
		 {
		 	cin>>mat[i][j];
		 }
		 i=po-1;
		 for(j=0;j<4;j++)
		 {
		 	num1[j]=mat[i][j];
		 	pos1[j]=i;
		 	hash[num1[j]]=hash[num1[j]]+1;
		 }
		 cin>>po;
		 for(i=0;i<4;i++)
		 	for(j=0;j<4;j++)
		 	{
			 	cin>>mat[i][j];
			}
		 i=po-1;
		 for(j=0;j<4;j++)
		  {
		  	num2[j]=mat[i][j];
		  	hash[num2[j]]=hash[num2[j]]+1;
		  }
		  count=0;
		  res=0;
		 for(i=0;i<4;i++)
		 {
		 	if(hash[num2[i]]>1)
		 	 {
		 	 	count++;
		 	 	res=num2[i];
		 	 }
		 }
		 //////////////////////////
		 /*for(i=1;i<17;i++)
		 {
		 	cout<<hash[i]<<" ";
		 }
		 cout<<endl;*/
		 /////////////////////////
		 	 if(count>1)
		 	 {
		 	 	cout<<"Case #"<<noc<<":"<<" "<<"Bad magician!"<<endl;
		 	 }
		 	 else if(count==0)
		 	 {
		 	 	cout<<"Case #"<<noc<<":"<<" "<<"Volunteer cheated!"<<endl;
		 	 }
		 	 else if(count==1)
		 	 {
		 	 	cout<<"Case #"<<noc<<":"<<" "<<res<<endl;
		 	 }
		 }
		
	return 0;
}