#include <iostream>
#include <cmath>
using namespace std;

int main() {
	// your code goes here
	int t,ans,counter=0,i,temp;
	char num[10];
	int p,q,hi,a,b;
	cin>>t;
	while(counter++!=t)
	{
		i=0;
		cin>>num;
		p=q=temp=0;
		while(num[i++]!='/')
		{
			p*=10;
			p+=num[i-1]-48;
		}
		while(num[i++]!='\0')
		{
			q*=10;
			q+=num[i-1]-48;
		}
		a=p;
		b=q;
		cout<<"Case #"<<counter<<": ";
		while(true)
		{
			if(a>b)
			a=a-b;
			else if(b>a)
			b=b-a;
			else
			break;
		}
		if(a!=1)
		{
			p/=a;
			q/=a;
		}
		while(pow(2,++temp)<q);
		if(pow(2,temp)==q)
		{
			temp=0;
			hi=q/p;
			while(pow(2,++temp)<hi);
			cout<<temp<<endl;
		}
		else
		{
			cout<<"impossible"<<endl;
		}
	}
	return 0;
}