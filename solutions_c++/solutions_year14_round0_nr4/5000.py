#include <iostream>
#include <cstdio>
#include<algorithm>
using namespace std;

#define lld long long int
lld inpt()
{
	char c;
	lld n[5]={},p=0,i;
	for(c=getchar();c!='.';c=getchar());
	for(c=getchar(),i=0;c>='0'&&c<='9';c=getchar(),i++)
	n[i]= c-'0';
	for(i=0;i<5;i++)
	p=p*10+n[i];
	
	return(p);
}
double ar[11],br[11],aflg[11]={},bflg[11]={};
int main() 
{
	lld t,n,i,j,count,k,p,q,r;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cin>>n;
		count=0;
		for(i=0;i<n;i++)
		cin>>ar[i];
		for(j=0;j<n;j++)
		cin>>br[j];
		sort(ar,ar+n);
		sort(br,br+n);
		/*for(i=0;i<n;i++)
		cout<<ar[i]<<" ";
		cout<<endl;
		for(i=0;i<n;i++)
		cout<<br[i]<<" ";
		cout<<endl;*/
		p=0;
		q=0;
		r=0;
		for(i=0;i<n;i++)
		{
			if(ar[q]>br[r])
			{
				count++;
				q++;
				r++;
			}
			else
			q++;
		}
		cout<<"Case #"<<k<<": "<<count<<" ";
		count=0;
		q=n-1;
		r=n-1;
		while(q>=0)
		{
			if(ar[q]>br[r])
			{
				q--;
				count++;
			}
			else
			{
				q--;
				r--;
			}
		}
		cout<<count<<endl;
	}
	return 0;
}