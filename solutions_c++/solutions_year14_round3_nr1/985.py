#include <iostream>
using namespace std;
#define lld long long int 
lld ar[50];
lld input()
{
	char c;
	lld n=0;
	for(c=getchar();!(c>='0'&&c<='9');c=getchar());
	for(;(c>='0'&&c<='9');c=getchar())
	{
		n=n*10+c-'0';
	}
	return(n);
}
	
int main() 
{
	lld t,i,j,p,q,ex,k,count;
	ar[0]=1;
	for(i=1;i<41;i++)
	ar[i]=ar[i-1]*2;
	cin>>t;
	for(k=1;k<=t;k++)
	{
		cout<<"Case #"<<k<<": ";
		p=input();//cout<<p;
		q=input();//cout<<q;
		for(i=40;i>=0;i--)
		{
			if(ar[i]<=q&&q%ar[i]==0)
			{
				ex=q/ar[i];
				break;
			}
		}
		if(p%ex!=0)
		cout<<"impossible\n";
		else if(p>q)
		cout<<"impossible\n";
		else
		{
			p=p/ex;
			q=q/ex;
			count=1;
			while(2*p<q)
			{
				q/=2;
				count++;
			}
			cout<<count<<endl;
		}
		
	}
	return 0;
}