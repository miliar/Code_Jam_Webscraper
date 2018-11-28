#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int t,n,x,i,j,k,cn=0;
	int sp[10001];
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cn=0;
		cin>>n>>x;
		for(j=0;j<n;j++)
			cin>>sp[j];
		sort(sp,sp+n);
		j=0;k=n-1;
		while(j<k)
		{
			if(sp[j]+sp[k]<=x)
				{j++;k--;cn++;}
			else 
				{k--;cn++;}
			
		}
		if(j==k)
			cn++;
		cout<<"Case #"<<i<<": "<<cn<<endl;
	}
}