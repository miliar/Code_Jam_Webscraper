#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void findDigits(int a,int *arr,int lastnum)
{
	while(a)
	{
		int tmp = a%10;
		if(arr[tmp]==1)
			arr[tmp] = 0;
		a/=10;
		
	}
	
}
bool dkdung(int *arr)
{
	for(int i=0;i<10;i++)
		if(arr[i]==1)
			return false;
	return true;
}
int mycount(int a)
{
	int indx = 1;
	int lastnum = 0;
	int arr[10] = {1,1,1,1,1,1,1,1,1,1};
	while(dkdung(arr)==false && a!=0)
	{
		//a = a*indx;
		findDigits(a*indx,arr,lastnum);
		lastnum = a*indx;
		indx++;
	}
	return lastnum;
}
void main()
{
	int n;
	int a[100];
	int b[100];
	fstream f;
	f.open("A-large.in",ios::in);
	f >> n;
	
	for(int i=0;i<n;i++)
	{
		f >> a[i];
	}
	f.close();
	for(int i=0;i<n;i++)
	{
		if(a[i]!=0) 
			b[i] = mycount(a[i]);
		else
			b[i] = 0;
	}

	fstream f2("A-large.out",ios::out);

	for(int i=0;i<n;i++)
	{
		if(b[i]==0)
			f2 << "Case #"<<i+1<<": INSOMNIA"<<endl;
		else
		f2 << "Case #"<<i+1<<": "<<b[i]<<endl;
	}
	f2.close();



}
