#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

	int a[9];
	long long int n,m;
	int get_do();
	int chk_it();
	void reset_a();

int main() 
{
	int i,j,k,total;
	
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w+",stdout);
	
	cin>>total;
	for(k=1;k<=total;k++)	
	{
		cin>>m;
		n=m;
		j=2;
		
		if(m==0)
		{
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;	
			continue;
		}
		while(chk_it() == 0)
		{
			get_do();
			n=m*j;
			j++;
		}
	
		//cout<<"Done in "<<(j-3)<<"steps. N is "<<(n-m)<<"\n\n";
		//for(i=0;i<10;i++)
		//cout<<a[i]<<endl;

		cout<<"Case #"<<k<<": "<<(n-m)<<endl;	
		reset_a();
	}
	
}

int get_do()
{
	//cout<<endl;
	long long int x=n;
	while(x > 0)
	{
		int y = x%10;
		x/=10;
		a[y]++;
		//cout<<"Found"<<y<<endl;
	}	
}

int chk_it()
{
	int x=1,i=0;
	for(i=0;i<10;i++)
	if(a[i] == 0)
	x=0;
	return x;	
}

void reset_a()
{
	int i=0;
	for(i=0;i<10;i++)
	a[i]=0;
}