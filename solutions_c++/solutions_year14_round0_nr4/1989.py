#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin>>T;
	int n;
	for(int i=0; i<T; i++)
	{
		cin>>n;
		vector<double> na(n),ke(n);
		for(int j=0; j<n; j++)
		{
			cin>>na[j];
		}
		for(int j=0; j<n; j++)
			cin>>ke[j];
		int suml=0, sumt=0;
		sort(na.begin(), na.end());
		sort(ke.begin(), ke.end());
		int k=n-1;
		for(int j=n-1; j>=0; j--)
		{
			if(ke[j]>na[k]) suml++;
			else k--;
		}
		k=n-1;
		for(int j=n-1; j>=0; j--)
		{
			if(na[j]>ke[k]) sumt++;
			else k--;
		}
		cout<<"Case #"<<i+1<<": "<<n-suml<<" "<<sumt<<endl;
	}
	//system("pause");
	return 0;
}