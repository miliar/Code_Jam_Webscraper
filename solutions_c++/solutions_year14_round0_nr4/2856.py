#include<iostream>
#include<fstream>
#include<iomanip>
#include<math.h>
using namespace std;
float partsort(float a[],int low,int high)
{
float temporary_para=a[low];
while (low<high)
	{
	while(low<high &&a[high]>=temporary_para)
	high--;
	a[low]=a[high];
	while(low<high &&a[low]<=temporary_para)
	low++;
	a[high]=a[low];
	}
a[low]=temporary_para;
return low;
}
void qsort(float a[],int low,int high)
{
float mid;
if (low<high)
	{
	mid=partsort(a,low,high);
	qsort(a,low,mid-1);
	qsort(a,mid+1,high);
	}
}
void quicksort(float a[],int n)
{
qsort(a,0,n-1);
}

int normal(float a[],float b[],int n)
{
bool fo[n];
int num=0;
for (int i=0;i<n;i++)
	fo[i]=true;	
for (int i=0;i<n;i++)
	{
		for (int j=0;j<n;j++)
		if ((b[j]>a[i])&&(fo[j]))		
		{
		fo[j]=false;
		num=num+1;			
		break;	
		}
	}
return n-num;
}
int enormal(float a[],float b[],int n)
{
bool fo[n];
int num=0;
for (int i=0;i<n;i++)
	fo[i]=true;
int i=n-1,j=n-1;
while ((i>-1)&&(j>-1))
	{
	if (a[i]>b[j]) {num=num+1;i--;j--;}
	else {j--;}
	}
return num;
}
int main()
{
ifstream in("D-large.in");
ofstream out;
out.open("3.txt",ios::trunc);
int t;
in>>t;
for (int i=0;i<t;i++)
	{
	int n;
	in>>n;
	float *a=new float[n];
	float *b=new float[n];
	for (int j=0;j<n;j++)
		in>>a[j];
		quicksort(a,n);
	for (int j=0;j<n;j++)
		in>>b[j];
		quicksort(b,n);
		int w1=normal(a,b,n);
		int w2=enormal(a,b,n);	
	out<<"Case #"<<i+1<<": "<<w2<<" "<<w1<<endl;
	delete a;
	delete b;
	}
return 0;
}
