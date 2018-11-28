#include <iostream>  
#include <algorithm>  
#include <cmath>  
#include <vector>  
#include <string>
#include <set>
using namespace std;  

int n,m,i,j,k,q,s,w,v,a,b;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>w;
	for(v=1;v<=w;v++)
	{
		cin>>a>>b>>k;
		q=0;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
				{
					q++;
				}
			}
		}
		cout<<"Case #"<<v<<": "<<q<<endl;
	}
	return 0;
}

				






