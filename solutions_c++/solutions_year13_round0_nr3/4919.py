//Fair and square
#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
int pal(int a)
{
	int b=a,c=0;
	while(b>0)
	{
		c*=10;
		c+=b%10;
		b/=10;
	}
	if(c==a)return 1;
	else return 0;
}

		
int main()
{
			ifstream fin("C:\\Users\\sesir_000\\Documents\\C++ stuff\\A.in");
	ofstream fout("C:\\Users\\sesir_000\\Documents\\C++ stuff\\B.out");
	int ctr[1000],no=0,n,i,j,t=33,a,b;
	for(i=1;i<=t;i++)
	if(pal(i)&&pal(i*i))ctr[no++]=i*i;
	fin>>n;
	for(i=0;i<n;i++)
	{
		fin>>a>>b;
		fout<<"Case #"<<i+1<<": "<<upper_bound(ctr,ctr+no,b)-lower_bound(ctr,ctr+no,a)<<endl;
	}
	return 0;
}
	
		
	
