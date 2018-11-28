#include<iostream>
#include<string>
#include<math.h>
#include<cmath>
using namespace std;
int num=1;
void Gao()
{
	printf("Case #%d: ",num++);
	unsigned long long k,c,s;
	cin>>k>>c>>s;
	if(k>s)
	{
		cout<<"IMPOSSIBLE"<<endl;
		return ;
	}
	if (s==1)
	{
		cout<<1<<endl;
		return ;
	}
	unsigned long long ans=1LL,delta=1LL;
//	ans=pow(k,(c));
	for (int i=0;i<(int)c;i++)
		ans*=k;
	delta=(ans-1)/(k-1);
	unsigned long long tem=1;
	for (int i=0;i<(int)s;i++)
	{
		if (i)
			cout<<" ";
		cout<<tem;
		tem+=delta;	
	}
	cout<<endl;
}
int main()
{	
	int T;
	freopen("D-small-attempt1.in","r",stdin);
	freopen("D.out","w",stdout);
	cin>>T;
	while (T--)
		Gao();
	return 0;
}  
