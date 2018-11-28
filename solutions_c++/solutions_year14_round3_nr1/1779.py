#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test,t,i,j,k,p,q;
	cin>>test;
	for(t=1;t<=test;t++)
	{
		scanf("%d/%d",&p,&q);
		if(q%p==0)
		{
			q=q/p;
			p=1;
		}
		k=q;i=0;
		while(k>p&&k%2==0)
		{
			k=k/2;
			i++;
		}
		while(k%2==0)
		{
			k=k/2;
		}
		if(k!=1)
		{
			cout<<"Case #"<<t<<": impossible"<<endl;
		}
		else
		{
			cout<<"Case #"<<t<<": "<<i<<endl;
		}

	}
    return 0;
}
