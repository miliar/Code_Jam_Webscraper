#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int main()
{
	int test,i,j,l;
	int a,b,k,count;
	cin>>test;
	for(i=0;i<test;i++)
	{
		cin>>a>>b>>k;
	 	count=0;
	 	cout<<"Case #"<<i+1<<": ";
//	 	cout<<endl<<a&b<<endl;
		for(j=0;j<a;j++)
		{
//			cout<<j;
			for(l=0;l<b;l++)
			{
//				 cout<<l;
				 int temp=j&l;
//				cout<<":"<<temp;
				if(temp<k)
					count++;
			}
//			cout<<endl;	
		}
		cout<<count<<endl;
	}

}