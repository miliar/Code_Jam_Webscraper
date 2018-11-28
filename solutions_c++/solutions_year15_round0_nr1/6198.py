#include <iostream>
#include<cstdio>
using namespace std;
int a[6];
int main() {
	int n,p,x=0,j;
	cin>>n;
	while(n--)
	{  int total=0,friends=0,b;
	    x++;
		cin>>p;
		string s;
		cin>>s;
		for(int i=0;i<=p;i++)
		{
		a[i]=s[i]-'0';
		//cout<<a[i];
		}
		for(int i=0;i<=p;i++)
		{
			if(total<i)
			{friends+=i-total;
			total=i;
			}
		total+=a[i];
		}
		cout<<"Case #"<<x<<": "<<friends<<endl;
	}
	return 0;
}