#include<bits/stdc++.h>
using namespace std;

long long int m,n,k,cnt,i,l,j,t;

int main()
{
	ifstream iff("B-small-attempt0.in");
	ofstream off("lol.txt");
	iff >> t;
	while(t--)
	{
		cnt=0;
		l++;
	   iff >> m >> n >> k;
	
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			 int z = i&j;
			if(z<k)
			{
				cnt++;
			}
			
			
			
		}
	}
	
	off <<"Case #"<<l<<": "<<cnt<<endl;	
	}
	
	
	return 0;
}
