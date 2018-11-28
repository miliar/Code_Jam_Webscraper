#include<bits/stdc++.h>
using  namespace std;
int main()
{
	int t,d,p[2000],pmax,i,j;
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		pmax=-1;
		cin>>d;
		for(i=0;i<d;i++)
		{
			cin>>p[i];
			if(p[i]>pmax) pmax=p[i];
		}
		int mins=pmax;
		for(i=pmax-1;i>=1;i--)
		{
			int addition=0;
			for(j=0;j<d;j++)
			{
				if(p[j]>i) addition+=((p[j]-1)/i);
			}
			if((i+addition)<mins) mins=i+addition;
		}
		cout<<"Case #"<<tc<<": "<<mins<<endl;
	}
}
