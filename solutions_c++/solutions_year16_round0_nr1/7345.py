#include <iostream>
#include<fstream>

using namespace std;
int main()
{
	ifstream f;
	f.open("C:\\a.in");
	ofstream fo;
	fo.open("C:\\Users\\Zonoid\\Desktop\\output.txt");
	long long int test;
	f>>test;
	for(long long int z=0;z<test;z++)
		{
			long long int n;
		f>>n;
		int d[]={0,0,0,0,0,0,0,0,0,0};		
		if(n==0)
		fo<<"Case #"<<(z+1)<<": INSOMNIA"<<endl;
		else
		{
		long long int j=2;
	for(long long int a=n;;j++){
	long long int no=a;
	while(no>0)
	{
		d[no%10]++;
	no/=10;
	}
	int flag=1;
	for(int i=0;i<10;i++)
	if(d[i]==0)
	{
		a=n*j;
			
		flag=0;
		break;
	}
	if(flag)
	{
	fo<<"Case #"<<(z+1)<<": "<<a<<endl ;
	break;}
	}
	}
		}
		fo.close();
    return 0;
}
