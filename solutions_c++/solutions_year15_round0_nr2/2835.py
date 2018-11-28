#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int solution();

bool can(int data[],int d,int change,int eat);

bool text(int data[],int mid,int d);

int main()
{
	int line=0;
	cin>>line;
	int cases[line];

	for(int i=0;i<line;++i)
	{
		cases[i]=solution();
	}

	for(int j=0;j<line;++j)
	{
		cout<<"Case #"<<j+1<<": "<<cases[j]<<endl;
	}


}

bool text(int data[],int mid,int d)
{
	for(int i=0;i<mid;++i)
	{
		if(can(data,d,i,(mid-i)))
			return true; 
	}
	return false;
}

bool can(int data[],int d,int change,int eat)
{
	int tmp;
	int sum = 0;
	for(int i=0;i<d;++i)
	{
		if(data[i]>eat)
		{
			tmp=data[i]/eat - 1;
			if(data[i] % eat != 0)
				tmp++;
			sum += tmp;
		}
	}
	if(sum<=change)
		return true;
	else
		return false;
}

int solution()
{
	int d=0;
	cin>>d;
	int data[d];
	for(int i=0;i<d;++i)
		cin>>data[i];
	int l=0,r=1005;
	int mid;
	while((r-l)>1)
	{
		mid=(l+r)/2;
		if(text(data,mid,d))
			r=mid;
		else
			l=mid;
	}
	return r;
}