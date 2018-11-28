#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include <stdlib.h>
#include <stack>
using namespace std;


int main()
{

	int t,one ,two,a[4][4],b[4][4],var=0;
		cin>>t;

	while(t--)
	{
	cin>>one;
	for(int i=0;i<4;i++)
	{
		   for(int j=0;j<4;j++)
		{
			cin>>a[i][j];
		}
	}
	  cin>>two;
		for(int i=0;i<4;i++)
		{
			   for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}
		int count=0,ans;
	    for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			  {

  		     	if(a[one-1][i]==b[two-1][j])
  		     	{
				   ans=a[one-1][i];
				   count++;
  		     	}
			  }
		}
		if(count==1)
		cout<<"Case #"<<++var<<":"<<" "<<ans<<endl;
		else if(count==0)
		cout<<"Case #"<<++var<<":"<<" "<<"Volunteer cheated!"<<endl;

	else 	cout<<"Case #"<<++var<<":"<<" "<<"Bad magician!"<<endl;
	}
}
