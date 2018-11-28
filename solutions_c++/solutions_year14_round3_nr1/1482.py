#include <iostream>
#include<cstdio>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
long long int a=0;
long long int rec(long long int p, long long int q)
{
//	printf("p= %lld\n q= %lld\n a is %lld\n",p,q,a);;
	if(a>40)return 0;
	int i;
	for(i=0;i<=40;i++)	
	{
		if(p==q)
		{
			if(a<=40)
			{
//				printf("return %d\n",i);
				return i;
			}
			else
			{
				return 0;
			}
		}
		else if(p>q)
		{
			long long int temp= a ;
			//a=0;
			//printf("a was %lld\n",a);
			long long int  xe= rec(p-q,q);
			//printf("xe = %lld\n",xe);
			if(xe!=0)return i;
			else
				return 0;
		} 
		else
		{
//			printf("Mul p by 2....\n");
			p*=2;
			a++;
			if(a>40)
			{
				return 0;
			}
		}
	}
}
int main() {
	// your code goes here
	int n,i,j,i1;
	cin>>n;
	for(i1=0;i1<n;i1++)
	{
		char x[50];
		cin>>x;
		a=0;
		int len=strlen(x);
		long long int ct=0,p,q;
		for(i=0;i<len;i++)
		{
			if((x[i]=='/'))break;
			ct+=(int) x[i]-48;
			if(x[i+1]!='/')
			{
				ct*=10;
			}
		}
		p=ct;
		ct=0;
		for(i++;i<len;i++)
		{
		//	if((x[i]=='/'))break;
			ct+=(int) x[i]-48;
			if(i!=len-1)
			{
				ct*=10;
			}
		}
		q=ct;
		//printf("%lld %lld\n",p,q);
		printf("Case #%d: ",i1+1);
		if(q%2!=0)
		{
			printf("impossible\n");
		}
		else if(p==q)
		{
			printf("0\n");
		}
	else
	{
		long long int ans=rec(p,q);
		if(ans<40 && ans!=0)
		{
			printf("%lld\n",ans);
		}
		else
		{
			printf("impossible\n");
		}
	}
	}
	return 0;
}