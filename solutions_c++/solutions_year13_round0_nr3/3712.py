#include<iostream>
using namespace std;
bool check(int x)
{
	int t1=x,t2=0;
	while (t1>0)
	{
		t2=t2*10+t1%10;
		t1=t1/10;
	}
	return (x==t2);
}
int calcu(int R)
{
	int i,ans=0;
	for (i=0;i<=R;i++)
		if (check(i)&&check(i*i)) ++ans;
	return ans;
}
int main()
{
	int T,i,L,R;
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	cin>>T;
	for (i=0;i<T;i++)
	{
		cin>>L>>R;
		cout<<"Case #"<<i+1<<": "<<calcu(sqrt(R))-calcu(sqrt(L-1))<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}