#include<iostream>
#include<algorithm>
#include<fstream>
#include<cstring>
using namespace std;

int main()
{
	int T,n,t=1,prv,i,arr[10001],diff;
	long long int ans1,ans2;
	fstream fin,fout;
	
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);

	fin>>T;
	cout<<T;
	
	while(t<=T)
	{
		fin>>n;
		i=0;
		ans1 = 0;
		ans2 = 0;
		fin>>arr[0];
		diff = 0;
		for(i=1;i<n;i++)
		{
			fin>>arr[i];
			if(arr[i-1]-arr[i]>diff)
				diff = arr[i-1]-arr[i];
		}


		prv = arr[0];
		for(i=1;i<n;i++)
		{
			prv-arr[i]>0?ans1 = ans1 = ans1+prv-arr[i]:ans1=ans1;
			if(prv<=diff)
				ans2+=prv;
			else
				ans2+=diff;
			prv = arr[i];
		}
		/*
		if(prv == arr[n-1])
		{
			if(prv<=diff)
				ans2-=prv;
			else
				ans2-=diff;
		}
		*/
		fout<<"Case #"<<t<<": "<<ans1<<" "<<ans2<<"\n";
			
		t++;
	}
	
}
