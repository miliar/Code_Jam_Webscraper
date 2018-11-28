#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	long long int m;
	m=0;
	while(t>0)
	{
		t--;
		m++;
	
	long long int n;
	int a[10];
	for(int i=0;i<=9;i++)
	{
		a[i]=0;
	}
	cin>>n;
	if(n==0)
	cout<<"Case #"<<m<<": INSOMNIA"<<endl;
	else
	{
	long long int i=1;
	long long int p,q,c=0,ans;
	while(1)
{
	c=0;
	p=n*i;
	i++;
	ans=p;
	while(p!=0)
	{
		q=p%10;
		a[q]=1;
		p=p/10;
	}
		for(int l=0;l<=9;l++)
	{
		if(a[l]==1)
	{	c++;}
	}
	if(c==10)
	break;
	
}
cout<<"Case #"<<m<<": "<<ans<<endl;;
	}
	}
	return 0;
}