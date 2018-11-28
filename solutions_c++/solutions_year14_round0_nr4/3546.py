#include<iostream>
#include<fstream>
using namespace std;
void sort(double arr[],int n);
int main()
{
	ifstream inp;
	ofstream out;
	inp.open("input.in");
	if(!inp)
		{
			return 100;
		}
	out.open("output.txt");
	if(!out)
		{
			return 100;
		}
	int cases;
	inp>>cases;
	int count;
	int r1,r2;
	int res;
	for(int z=1;z<=cases;z++)
	{
		inp>>count;
		res=0;
		double arr1[count];
		double arr2[count];
		for(int i=0;i<count;i++)
		{
			inp>>arr1[i];
		}
		for(int i=0;i<count;i++)
		{
			inp>>arr2[i];
		}
		sort(arr1,count);
		sort(arr2,count);
		r1=r2=0;
		int i1=0,i2=count-1,j=count-1;
		while(i1<=i2)
		{
			if(arr1[i2]<arr2[j])
			{
				i1++;
				j--;	
			}
			else
			{
				r1++;
				i2--;
				j--;
			}
		}
	
		j=0;
		for(int i=0;i<count && j<count;i++)
		{
			while(i<count && arr1[j]>arr2[i])
			{
				r2++;
				i++;
			}
			j++;
		}
		out<<"case #"<<z<<": "<<r1<<" "<<r2<<endl;
	}
	inp.close();
	out.close();
	return 0;
}
void sort(double arr[],int n)
{
	int min;
	for(int i=0;i<n;i++)
	{
		min=i;
		for(int j=i+1;j<n;j++)
		{
			if(arr[j]<arr[min])
			{
				min=j;
			}
		}
		double temp=arr[min];
		arr[min]=arr[i];
		arr[i]=temp;
	}
}
