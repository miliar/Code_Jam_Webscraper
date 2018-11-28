#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int n,t,i,j,flag,count,k,a,b;
	scanf("%d",&n);
	for(t=1;t<=n;t++)
	{
		scanf("%d %d %d",&a,&b,&k);
		count=0;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if((i&j)<k)
					count++;
			}
		}
		cout<<"Case #"<<t<<": ";
		cout<<count<<endl;
	}
	return 0;
}