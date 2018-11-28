#include<bits/stdc++.h>
using namespace std;
int b[32];
int main()
{
	int count=0,valid=0,i,j,k,l,m,n,v,c,x,z,t;
	scanf("%d",&t);
	for(int m=1;m<=t;m++)
	{
		b[0]=b[31]=1;
		scanf("%d%d",&n,&j);
		cout<<"Case #"<<m<<": ";
		cout<<endl;
		count++;
		for(int k=0;k<32;k++)
		cout<<b[k];
		cout<<" ";
		for(l=2;l<=10;l++)
		cout<<l+1<<" ";
		cout<<endl;
		for(i=1;i<=29;i=i+2)
		{
			b[i]=1;
		for(v=31-i;v>=2;v=v-2)
		{
			b[v]=1;
			count++;
			for(int k=0;k<32;k++)
			cout<<b[k];
			cout<<" ";
			for(int l=2;l<=10;l++)
			cout<<l+1<<" ";
			b[v]=0;
			cout<<endl;
		}
		b[i]=0;
		}
		for(int i=1;i<=29;i=i+2)
		{
			b[i]=b[31-i]=1;
			for(v=i+2;v<=29;v=v+2)
			{
				b[v]=1;
			for(c=31-v;c>=2;c=c-2)
			{
				b[c]=1;	
				if(count==500)
				{
					valid=1;
					break;
				}
				count++;
				for(int k=0;k<32;k++)
			     cout<<b[k];
			     cout<<" ";
			    for(int l=2;l<=10;l++)
			    cout<<l+1<<" ";
			    b[c]=0;
			    cout<<endl;
			}
			if(valid==1)
			break;
			b[v]=0;		
			}
			if(valid==1)
			break;
			b[i]=b[31-i]=0;
		}
}
return 0;
}
