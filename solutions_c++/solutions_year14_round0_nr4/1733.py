#include "iostream"
#include "fstream"
#include "iomanip"
#include<conio.h>
#include<stdlib.h>
using namespace std;
int compare (const void * a, const void * b)
{
  if ( *(double*)a <  *(double*)b ) return -1;
  if ( *(double*)a == *(double*)b ) return 0;
  if ( *(double*)a >  *(double*)b ) return 1;
}
int main()
{
	int t,i,j,k,a,b,n,n1,n2,score,ptr;
    ifstream fin("a.in");
    ofstream fout("a.out");
    fin>>t;
    double arr1[1000],arr2[1000];
    
    for(i=0;i<t;i++)
    {
    	fin>>n;
    	for(j=0;j<n;j++)
    		fin>>arr1[j];
    	for(j=0;j<n;j++)
    		fin>>arr2[j];
    	qsort (arr1, n, sizeof(double), compare);
    	qsort (arr2, n, sizeof(double), compare);
    	ptr=0;
    	for(j=0;j<n;j++)
    		if(arr1[j]>arr2[ptr])
    			ptr++;
    	fout<<"Case #"<<i+1<<": "<<ptr<<" ";
    	ptr=0;
    	for(j=0;j<n;j++)
    	{
    		for(;ptr<n;ptr++)
    			if(arr2[ptr]>arr1[j])
    				break;
    		if(ptr==n)
    			break;
    		ptr++;
    	}	
    	fout<<n-j<<endl;
    }
    cout<<"ok";
    getch();
    
}
