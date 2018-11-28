#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int test,tests,n,s,c,t,t1,num;
	bool used[10];
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>tests;
	for (int test=1;test<=tests;test++)
	{
	cin>>n;
	printf("Case #%d: ",test);
	if (n==0) cout<<"INSOMNIA"<<endl;
	else
	{
		s=0;c=0;t=0;
		for (int i=0;i<=9;i++) used[i]=false;
		while (c<100000)
		{
			t+=n;c++;t1=t;
			while (t1!=0)
			{
			  num=t1%10;
			  if (used[num]==false) {used[num]=true;s++;}
			  t1=t1/10;
			}
			if (s==10) break;
		}
		cout<<t<<endl;
	}
	}
	return 0;
}
			
			
