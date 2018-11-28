#include <iostream>
#include <stdlib.h>     /* qsort */
using namespace std;

struct senate
{
	char party;
	int num;
};

int cmp(const void *a,const void *b)
{
	int l=((const struct senate *)a)->num;
	int r=((const struct senate *)b)->num;
	return (r-l);
}	
	
int main() {
	int tc=1;
	int t;
	cin>>t;
	senate mem[26];
	
	int n;
	while(tc<=t)
	{
		for(int i=0;i<26;i++)
		{
			mem[i].party=char(65+i);
			mem[i].num=0;
		}
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>mem[i].num;
		}
		
		qsort(mem,n,sizeof(mem[0]),cmp);
		
		cout<<"Case #"<<tc<<":";
		for(int i=0;i<n-1;i++)
		{
			
			while(mem[i].num>mem[i+1].num)
			{
				for(int j=0;j<=i;j++)
				{
					cout<<" "<<mem[j].party;
					mem[j].num-=1;
				}
			}
		}
		if(n%2==0)
		{
			while(mem[n-1].num>0)
			{
				for(int i=0;i<n-1;i+=2)
				{
						cout<<" "<<mem[i].party<<mem[i+1].party;
					mem[i].num-=1;
					mem[i+1].num-=1;
				}
				
			}
		}
		else if(n%2==1)
		{
			while(mem[n-1].num>0)
			{
				for(int i=0;i<n-2;i+=3)
				{
					cout<<" "<<mem[i].party<<" "<<mem[i+1].party<<mem[i+2].party;
					mem[i].num-=1;
					mem[i+1].num-=1;
					mem[i+2].num-=1;
				}
				
			}
		}
		cout<<endl;
		tc++;
	}
	return 0;
}
