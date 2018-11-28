#include<stdio.h>
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{

	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int t;
	cin>>t;
	for (int p=0;p<t;p++)
	{
		int r;
		cin>>r;
		vector<int> arr1(4);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				int inp;
				cin>>inp;
				if (i==r-1)	
					arr1[j]=inp;
			}
		}

		cin>>r;
		vector<int> arr2(4);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				int inp;
				cin>>inp;
				if (i==r-1)	
					arr2[j]=inp;
			}
		}

		sort(arr1.begin(),arr1.end());
		sort(arr2.begin(),arr2.end());
		int found=0;
		int index=-1;
		for (int q=0;q<4;q++)
		{
			if (binary_search(arr2.begin(),arr2.end(),arr1[q]))
			{
				index=q;
				found++;
			}
		}

		if (found==0)
			cout<<"Case #"<<p+1<<": Volunteer cheated!"<<endl;
		else if (found==1)
			cout<<"Case #"<<p+1<<": "<<arr1[index]<<endl;
		else
			cout<<"Case #"<<p+1<<": Bad magician!"<<endl;

	}

	return 0;
}
