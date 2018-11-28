#include <iostream>
#include <cmath>

using namespace std;
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
const long long m=10000001;
const int y=10;
long long arr[m],a,b,a2,b2;
int cases,d[y];
bool palindrome(long long num)
{
	long long temp;
	int counter;
	temp=num;
	for(counter=1;;counter++)
	{
		d[counter]=temp%10;
		temp=temp/10;
		if(temp==0)break;
	}
	for(int i=1;i<=counter/2;i++)
	{
		if(d[i]!=d[counter-i+1])
		{
			return false;
		}
	}
	return true;
}
int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	arr[0]=1;
	for(int i=1;i<=m;i++)
	{
		if(palindrome(i) && palindrome(i*i))
		{
			arr[i]=arr[i-1]+1;
		}
		else
		{
			arr[i]=arr[i-1];
		}
	}
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>a>>b;
		a2=sqrtl(a);
		if(a2*a2!=a)a2++;
		b2=sqrtl(b);
		cout<<"Case #"<<kase<<": ";
		if(a2>b2)
		{
			cout<<"0\n";
		}
		else
		{
			cout<<arr[b2]-arr[a2-1]<<"\n";
		}
	}
	return 0;
}