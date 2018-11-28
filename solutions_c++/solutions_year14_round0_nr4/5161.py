#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int main()
{
	float arr1[1000],arr2[1000];int opt[1000],des[1000];
	int t,n,l=0,temp;
	float mfile[100000];
	ifstream in;
	in.open("a16.txt");
	for(int i=0;i<100000;i++)
	{
		in>>mfile[i];	
	}
	t=mfile[l++];
	for(int j=0;j<t;j++)
	{
		opt[0]=0;temp=0;des[0]=0;
		n=mfile[l++];
		for(int i=0;i<n;i++)
		{
			arr1[i]=mfile[l++];
		}
		for(int i=0;i<n;i++)
		{
			arr2[i]=mfile[l++];
		}		
		sort(arr2,arr2+n);
		sort(arr1,arr1+n);
		for(int i=0;i<n;i++)
		{
			if(arr2[i]>arr1[temp])
			{
				++temp;
			}
		}
		des[j]=(n-temp);
	/*	for(int i=0;i<n;i++)
		{
			if(arr1[i]>arr2[i])
			{
				opt[j]+=1;
			}
		}*/
		temp=0;
		for(int i=0;i<n;i++)
		{
			if(arr1[i]>arr2[temp])
			{
				opt[j]+=1;
				temp++;
			}
		}
		cout<<"Case #"<<j+1<<": "<<opt[j]<<" "<<des[j]<<"\n";
	}
	return 0;
}
