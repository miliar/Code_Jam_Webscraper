#include<iostream>
using namespace std;
int main()
{
	int tot=0,i,j,t,a,b,k,count;
	cin>>t;
	while(t-->0)
	{
		tot++;
		count=0;
		cin>>a>>b>>k;
		for(i=0;i<a;++i)
		for(j=0;j<b;++j)
		{
			if((i&j)<k)
			count++;
		}
		cout<<"case #"<<tot<<": "<<count<<"\n";
		
	}
	return 0;
}
