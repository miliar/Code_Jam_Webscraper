#include <iostream>
#include <string.h>
#include <fstream.h>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main ()
{
ifstream file1;
ofstream file2;
file1.open("inp.txt",ios::in);
file2.open("out.txt");
int t;
file1>>t;
int cnt=1;
while (t--)
	{
long long int a,n;
file1>>a>>n;
long long int arr[n];
for (int i=0;i<n;++i)
{
	file1>>arr[i];
}


sort (arr,arr+n);
int arrop[n+1];
for (int i=0;i<=n;++i)
    {
arrop[i]=n-i;
}
int op=0;
for (int i=0;i<n;++i)
{
	if (arr[i]<a)
	{
     	a=arr[i]+a;
		arrop[i+1]+=op;
    }
	else {
		a=a+a-1;
		op++;
		if( (a+a-1) > a) 
        {
        i--;
        }
        else {
        arrop[i+1]+=op;
        }
	}
}
sort(arrop,arrop+n+1);


file2<<"Case #"<<cnt++<<": "<<arrop[0]<<endl;
}

file2.close();
file1.close();
	return 0;
} 
