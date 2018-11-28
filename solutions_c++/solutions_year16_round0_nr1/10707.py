#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<iomanip>
#include<fstream>
#define x64 long long
using namespace std;
#if !defined(test)
#define for_(i,t)	\
	x64 t ;		\
	cin >> t;	\
	for( x64 i=0 ; i < t ; i++ )
#define for_2(i,t)	\
	for( x64 i=0 ; i < t ; i++ )
#define mod 1000000007
#endif
/*
using namespace std;
struct matrix
{
	x64 a[2][2];
	matrix operator*(matrix m)
	{
		matrix x;
		x.a[0][0]=(((a[0][0]*m.a[0][0])%mod)+((a[0][1]*m.a[1][0])%mod))%mod;
		x.a[0][1]=(((a[0][0]*m.a[0][1])%mod)+((a[0][1]*m.a[1][1])%mod))%mod;
		x.a[1][1]=(((a[1][0]*m.a[0][1])%mod)+((a[1][1]*m.a[1][1])%mod))%mod;
		x.a[0][1]=(((a[0][0]*m.a[0][1])%mod)+((a[0][1]*m.a[1][1])%mod))%mod;
	}
};

matrix fast(matrix e,x64 x)
{
	matrix base=e,side;
	side.a[0][0]=side.a[0][0]=1,side.a[0][1]=side.a[1][0]=0;
	while(x)
	{
		if(x&1)
		{
			side=side*base;
		}
		x>>=2;
		if(x)
		base=base*base;
	}
	base=base*side;
	return base;
}*/
bool call_me(x64 t,bool *a)
{
	while(t)
	{
		a[t%10]=true;
		t/=10;
	}
	for(int i=0;i<10;i++)
	{
		if(a[i]==false)
			return true;
	}
	return false;
}
int main()
{
	for_(i,t)
	{		
		cout << "Case #"<<i+1<<": ";
		x64 x,x0;
		cin >> x ;
		x0=x;
		if(x==0)
		{
			cout << "INSOMNIA" << endl ;
			continue;		
		}
			bool a[10] = {{false}} ;
		while(call_me(x,a))
			x+=x0;
		cout << x << endl ; 
	}
	return 0;
}