#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{   std::ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int ti=0;ti<t;ti++)
	{	int d;
		cin>>d;
		int* arr=new int[1001];
		for(int i=0;i<1001;i++)
		{	arr[i]=0;
		}
		for(int i=0;i<d;i++)
		{	int p;
			cin>>p;
			arr[p]++;
		}
		int minans=1000;
		for(int i=1;i<=1000;i++)
		{	int count=0;
			for(int j=i+1;j<=1000;j++)
			{	if(j%i==0)count+=arr[j]*((j/i)-1);
				else count+=arr[j]*(j/i);
			}
			minans=min(minans,count+i);
		}
		cout<<"Case #"<<(ti+1)<<": "<<minans<<endl;
	}
}
