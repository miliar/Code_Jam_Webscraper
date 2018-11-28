#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
   int t,p=0;
	cin>>t;
	while(t--)
	{   p++;
		int n,i;
		cin>>n;
		int m[n];
		for(i=0;i<n;i++)
		cin>>m[i];
		int y=0,z=0,q,max=0;
		for(int j=0;j<n-1;j++)
		{
			if(m[j]>m[j+1])
			{
				q=(m[j]-m[j+1]);
				y+=q;
				if(q>max)
				max=q;
			}
			
		}
		
		for(int k=0;k<n-1;k++)
		{
			if(m[k]<=max)
			z+=m[k];
			else
			z+=max;
		}
		cout<<"Case #"<<p<<": "<<y<<" "<<z<<"\n";
	}
	
    return 0;
}
