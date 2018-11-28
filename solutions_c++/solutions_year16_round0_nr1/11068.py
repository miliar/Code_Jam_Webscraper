#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

int main()
{
long long int no,temp,n2;
int t;
ifstream fin;
fin.open("inp.txt");
ofstream fout;
fout.open("out.txt");
fin>>t;
int j=1;
while(t--)
{
	fin>>no;
	if(no==0)
	fout<<"Case #"<<j<<": "<<"INSOMNIA"<<"\n";
	else
	{	int count=0,i=1,rem;
		int arr[10];
		memset(arr,0,sizeof(arr));
		n2= no;
		while(count<10)
		{
		 n2=no*i;temp=n2;
		 while(temp>0)
		 { rem=temp%10;
		   if(arr[rem]==0)
			{arr[rem]=1;
			 count++;
			}
		   temp=temp/10;
		 }
		 i++;//fout<<n2<<"\n";
		}fout<<"Case #"<<j<<": "<<n2<<"\n";
	}
	j++;
}
return 0;
}