#include<iostream>
#include<cstdio>
using namespace std;

int main(void)
{
	int t,test;
	double c,f,x,ans,prev,newt;
	cin>>t;
	test=t;
	while(t--)
	{
		cin>>c>>f>>x;
		prev=x/2;
		newt=(c/2.0);
		int i=1;
		while(newt+(x/(2+i*f))<prev)
		{
			prev=newt+(x/(2+i*f));
			newt=newt+(c/(2+i*f));
			i++;
		}
		cout << "Case #"<<test-t<<": ";
		printf("%.7lf\n",prev);
		
		
		
	}
}