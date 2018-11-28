#include<iostream>
#include<cmath>
using namespace std;


int cek[10]={0};

int cekinsom(int n)
{
	int i=1;
	if (n==0) return 1;
	for (int i=1;i<10;i++)
	{
		if (n==pow(10,i)) return 1;
	}
	return 0;
}

int fdigit(int n)
{
	int x=0;
	if (n==0) return x;
	else while (n>0)
	{
		x++;
		n/=10;
	}
	return x;
}

void fcek(int d, int n)
{
	for (int i=d-1;i>=0;i--)
	{
		cek[n%10]=1;
		n/=10;
	}
}



int main()
{
	int sum;
	int digit;
	int N;
	int j;
	int t;
	cin>>t;
	
	int n[t];
	for (int i=0;i<t;i++)
	cin>>n[i];
	
	for (int i=0;i<t;i++)
	{
		for (int z=0;z<10;z++)
		cek[z]=0;
		j=0;
		sum=0;
		
		if (n[i]==0)
		{
			cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		}
		else 
		{
			while (sum<10)
			{
				sum=0;
				j++;
				N=n[i]*j;
					
				fcek(fdigit(N),N);
					
				for (int z=0;z<10;z++)
				sum+=cek[z];
			}
			cout<<"Case #"<<i+1<<": "<<N<<endl;
		}
	}
}
