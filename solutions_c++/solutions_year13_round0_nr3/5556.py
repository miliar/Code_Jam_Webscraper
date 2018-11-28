#include<iostream.h>
#include<math.h>
#include<stdio.h>

void main()
{       int n,i,j,N,k,temp1,count=0;
	double l,temp,a,b;
	freopen("s1.in","r",stdin);
	freopen("gad.out","w",stdout);
	cin>>n;
	for(i=1;i<=n;i++)
	{	cin>>a>>b;
		for(j=a;j<=b;j++)
		{	l=sqrt(j);
			k=fabs(l);
			if(k==l)
			{      	temp=0;N=0;
				while(k>0)
				{ 	temp1=k%10;
					k=k/10;
					temp=temp*10+temp1;
				}
				if(temp==sqrt(j))
				{       //cout<<temp;
					N++;
				}
				temp=0;
				k=j;
				while(k>0)
				{	temp1=k%10;
					k=k/10;
					temp=temp*10+temp1;
				}
				if(temp==j)
					N++;
				if(N==2)
				       count++;
			}
		}
		cout<<"Case #"<<i<<": "<<count<<"\n";
		count=0;
	}
}