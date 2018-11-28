#include<iostream>
using namespace std;

int main()
{
	freopen("E:/A.in","r",stdin);
    freopen("E:/out.in","w",stdout);
	long long int a,b,t;
	scanf("%lld",&t);
	int cc = 0;
	while(t--)
	{
		scanf("%lld/%lld",&a,&b);
		cc++;
		long long int xx = b;
		cout<<"Case #"<<cc<<": ";
		bool fl = true;
		int cnt = 0;
		while(b>2*a)
		{
			if(b%2!=0){fl=false;break;}
			b/=2;
			cnt++;
		}
		int bb = (xx&(xx-1));
		if(fl==false || !(bb==0))
			cout<<"impossible"<<endl;
		else
			cout<<cnt+1<<endl;
	}
}