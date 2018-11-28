#include<iostream>
#include<cmath>
using namespace std;

int And(int a,int b)
{
	int result=0,n=0;
	while(a>0 || b>0)
	{
		result+= (a%2 && b%2 )*pow(2,n);
		n++;a=a/2;b=b/2;
	}
	return result;
}
int main()
{
	int t;cin>>t;
	for(int q=0;q<t;q++)
	{
		
	int n1,n2,k,count=0;
	cin>>n1>>n2>>k;
	for(int i=0;i<n1;i++)
	{
		for(int j=0;j<n2;j++)
		{
			if(And(i,j)<k) count++;
		}
	}
	cout<<"Case #"<<q+1<<": "<<count<<endl;
}
}
