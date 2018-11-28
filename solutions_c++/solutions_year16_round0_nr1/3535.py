#include <bits/stdc++.h>
using namespace std;
int main() {
	unsigned long long int t,i,j,n,d,a[10]={0},b,c=0,e;
	cin>>t;
	for(j=1;j<=t;j++)
	{c=0;
		cin>>n;
		for(i=1;c!=10;i++)
{	d=i*n;
e=d; 
	while(d!=0&&n!=0)
	{
		b=d%10;
		if(a[b]==0) {
			a[b]++; c++;
		}
		d=d/10;
	}
	if(c==10||n==0) { c=10;
	cout<<"Case #"<<j<<": ";
	if(n!=0) 	cout<<e<<"\n";
	else cout<<"INSOMNIA"<<"\n";
		}
		}
		for(int i=0;i<10;i++) a[i]=0;
	}
	return 0;
}