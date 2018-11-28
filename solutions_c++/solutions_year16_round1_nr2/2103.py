#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	freopen("C://Users//Abhishek//Desktop//Algorithm Coursera//A-small-attempt0.in","r",stdin);
	freopen("C://Users//Abhishek//Desktop//Algorithm Coursera//abhishek.txt","w",stdout);
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int n,y;
		cin>>n;
		int a[2501]={0};
		for(int i=0;i<n*(n*2-1);i++)
		{
			cin>>y;
			a[y]++;
		}
		cout<<"Case #"<<k<<": ";
		for(int i=1;i<=2500;i++)
		{
			if(a[i]%2==1)
				cout<<i<<" ";
		}
		cout<<endl;
	}
}
