#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;
int main(){int e;
	ifstream input("input.txt");
	ofstream output("output.txt");
int t;int n;int ans;
input>>t;int arr[50][50];
for(int i=0;i<t;i++)
{input>>n;
vector<int>x;
	for(int k=0;k<((2*n)-1);k++)
	{
	for(int j=0;j<n;j++)
	input>>arr[k][j];
	}ans=0;
	for(int s=0;s<(2*n-1);s++)
	{
		for(int d=0;d<n;d++)
		{
			if(arr[s][d]!=-1)
			{e=arr[s][d];
	for(int m=0;m<((2*n)-1);m++)
	{
	for(int r=0;r<n;r++)
	{
	if(e==arr[m][r])
	{
	ans++;
	arr[m][r]=-1;
	}}
	}}
			if(ans%2!=0)
				x.push_back(e);
		ans=0;}}
	sort(x.begin(),x.end());
	output<<"case #"<<i+1<<": ";
	for(int l=0;l<n;l++)
	{
	output<<x[l]<<" ";
	}
	output<<endl;
}

}