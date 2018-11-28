#include<iostream>
#include<cmath>
#include <cstdlib>
#include<fstream>
#include <cstring>
#include<string>
#include<algorithm>
#define size 10000
using namespace std;
using std::ifstream;
using std::ofstream;

char a[size]={'.'};
int A,B;

bool sq(int n)
{
	int num= sqrt(double(n));
	if (num*num != n)
		return false;
	else return true;
}

bool good(int n, int d)
{
	int a,b,c,e;
	if(d==4)
	{
		a=n/1000;
		b=(n%1000)/100;
		c=(n%100)/10;
		e=n%10;
		if(a==e && b==c)
			return true;
		else return false;
	}else if(d==3)
	{
		a=n/100;
		c=(n%10);
		if(a==c)
			return true;
		else return false;
	}
	else if(d==2)
	{
		if(n/10 == n%10)
			return true;
		else return false;
	}
	else if(d==1)
		return true;
	return false;

}

int digit(int n)
{
	if(n%1000!=n)
		return 4;
	else if(n%100!=n)
		return 3;
	else if(n%10!=n)
		return 2;
	else return 1;
}

int main()
{

	ofstream out;
	out.open("output.txt");

	int T,n,ans;
	char c;
	string s;

	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>A>>B;
		ans=0;
		for(int i=A;i<=B;i++)
		{
			if(sq(i) && good(i,digit(i)) && good(int(sqrt(double(i))), digit(int(sqrt(double(i))))))
			{
				ans++;
				//cout<<i<<" ";
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	//	out<<"Case #"<<t<<": "<<ans<<"\n";
	}

	out.close();
		
	return(0);
}