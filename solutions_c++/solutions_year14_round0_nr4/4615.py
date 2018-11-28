#include<iostream>
#include<cstdlib>

using namespace std;
double naomi[1000],ken[1000],naomi1[1000],ken1[1000];
int size;
int justbig(double a,double* arr)
{
	int val=0;
	while(arr[val]<a&&val<size&&arr[val]>0)
	{
		val++;
	}
	for(int i=val+1;i<size;i++)
	{
		if(arr[i]>a&&arr[i]>0)
		{
			if(arr[val]>0)
			{
				if(arr[i]<arr[val])
				val=i;
			}
			else
			val =i;
		}
	}
	if(val==size)
	val--;
	return val;
}
int smallest(double* arr)
{
	int val=0;
	while(val<0&&val<size)
	val++;
	for(int i=val+1;i<size;i++)
	{
		if(arr[i]<arr[val]&&arr[i]>0)
		val=i;
	}
	if(val==size)
	val--;
	return val;
}
int greatest()
{
	int val=0;
	for(int i=val+1;i<size;i++)
	{
		if(ken1[i]>ken1[val])
		val=i;
	}
	return val;
}
void dwar()
{
	int cnt=0;
	for(int i=0;i<size;i++)
	{
		int j=greatest();
		int k=justbig(ken1[j],naomi1);
		if(naomi1[k]>ken1[j])
		{
			cnt++;
			naomi1[k]=ken1[j]=-1;
		}
		else
		{
			k=smallest(naomi1);
			naomi1[k]=ken1[j]=-1;
		}
	}
	cout<<cnt<<" ";
}
void war()
{
	int cnt=0;
	for(int i=0;i<size;i++)
	{
		int j=justbig(naomi[i],ken);
		if(ken[j]>naomi[i])
		{
			ken[j]=-1;
		}
		else
		{
			j=smallest(ken);
			cnt++;
			ken[j]=-1;
		}
	}
	cout<<cnt<<endl;
}
int main()
{
	int T;
	cin>>T;
	for(int p=0;p<T;p++)
	{
		cin>>size;
//		cout<<size<<endl;
		for(int i=0;i<size;i++)
		{
			cin>>naomi[i];
			naomi1[i]=naomi[i];
//			cout<<naomi[i]<<" ";
		}
//		cout<<endl;
		for(int i=0;i<size;i++)
		{
			cin>>ken[i];
			ken1[i]=ken[i];
//			cout<<ken[i]<<" ";
		}
//		cout<<endl;
		cout<<"Case #"<<p+1<<": ";
		dwar();
		war();
	}
}
