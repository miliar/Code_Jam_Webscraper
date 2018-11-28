//============================================================================
// Name        : pblm1_magician.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main()
{
	int n;
//	cout<<"Enter the total number of test cases:";
	cin>>n;
	int arr_ans[n];

for(int z=0;z<n;z++)
{
	int ans1,ans2,arr1[4][4],arr2[4][4];
//	cout<<"Enter the answer and first arrangement;";
	cin>>ans1;
	ans1--;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>arr1[i][j];
		}
	}
//	cout<<"Enter the next answer and first arrangement;";
	cin>>ans2;
	ans2--;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>arr2[i][j];
		}
	}
	int count=0,store=0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{

			if(arr1[ans1][i]==arr2[ans2][j])
			{
				//cout<<"equality found!!!"<<arr1[ans1-1][i]<<endl<<arr2[ans2-1][j]<<endl<<z;;
				count++;
				store=arr1[ans1][i];
			}
		}
	}
	if(count==1)
	{
		arr_ans[z]=store;
	}
	else if(count>1)
	{
		arr_ans[z]=-1;
	}
	else
	{
		arr_ans[z]=0;
	}
}
for(int z=0;z<n;z++)
{
	if(arr_ans[z]==0)
	{
		cout<<"Case #"<<z+1<<":"<<" Volunteer cheated!"<<endl;
	}
	else if(arr_ans[z]==-1)
	{
		cout<<"Case #"<<z+1<<":"<<" Bad magician!"<<endl;
	}
	else if(arr_ans[z]>0)
	{
		cout<<"Case #"<<z+1<<":"<<" "<<arr_ans[z]<<endl;
	}
}

	return 0;
}
