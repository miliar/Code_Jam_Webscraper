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
long long A,B;

long long sq(long long n)
{
	long long num= sqrt(long double(n));
	if (num*num != n)
		return -1;
	else return num;
}

bool good(long long n, long long d)
{
	long long a,b,c,e,f,g,h,i,j,k,l,m,r,o,p;
	if(d==15)
	{
		a= n/100000000000000;
		b=(n%100000000000000)/10000000000000;
		c=(n%10000000000000)/1000000000000;
		e=(n%1000000000000)/100000000000;
		f=(n%100000000000)/10000000000;
		g=(n%10000000000)/1000000000;
		h=(n%1000000000)/100000000;
	//	i=(n%100000000)/10000000;
		j=(n%10000000)/1000000;
		k=(n%1000000)/100000;
		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( a==p && b==o && c==r && e==m && f==l && g==k && h==j)
			return true;
		else return false;
	}else if(d==14)
	{
		b= n/10000000000000;
		c=(n%10000000000000)/1000000000000;
		e=(n%1000000000000)/100000000000;
		f=(n%100000000000)/10000000000;
		g=(n%10000000000)/1000000000;
		h=(n%1000000000)/100000000;
		i=(n%100000000)/10000000;
		j=(n%10000000)/1000000;
		k=(n%1000000)/100000;
		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( b==p && c==o && e==r && f==m && g==l && h==k && i==j)
			return true;
		else return false;
	}else if(d==13)
	{
		c= n/1000000000000;
		e=(n%1000000000000)/100000000000;
		f=(n%100000000000)/10000000000;
		g=(n%10000000000)/1000000000;
		h=(n%1000000000)/100000000;
		i=(n%100000000)/10000000;
	//	j=(n%10000000)/1000000;
		k=(n%1000000)/100000;
		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( c==p && e==o && f==r && g==m && h==l && i==k)
			return true;
		else return false;
	}else if(d==12)
	{
		e= n/100000000000;
		f=(n%100000000000)/10000000000;
		g=(n%10000000000)/1000000000;
		h=(n%1000000000)/100000000;
		i=(n%100000000)/10000000;
		j=(n%10000000)/1000000;
		k=(n%1000000)/100000;
		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( e==p && f==o && g==r && h==m && i==l && j==k)
			return true;
		else return false;
	}else if(d==11)
	{
		f= n/10000000000;
		g=(n%10000000000)/1000000000;
		h=(n%1000000000)/100000000;
		i=(n%100000000)/10000000;
		j=(n%10000000)/1000000;
	//	k=(n%1000000)/100000;
		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if(f==p && g==o && h==r && i==m && j==l)
			return true;
		else return false;
	}else if(d==10)
	{
		g= n/1000000000;
		h=(n%1000000000)/100000000;
		i=(n%100000000)/10000000;
		j=(n%10000000)/1000000;
		k=(n%1000000)/100000;
		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( g==p && h==o && i==r && j==m && k==l)
			return true;
		else return false;
	}else if(d==9)
	{
		h= n/100000000;
		i=(n%100000000)/10000000;
		j=(n%10000000)/1000000;
		k=(n%1000000)/100000;
//		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( h==p && i==o && j==r && k==m)
			return true;
		else return false;
	}else if(d==8)
	{
		i= n/10000000;
		j=(n%10000000)/1000000;
		k=(n%1000000)/100000;
		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( i==p && j==o && k==r && l==m)
			return true;
		else return false;
	}else if(d==7)
	{
		j= n/1000000;
		k=(n%1000000)/100000;
		l=(n%100000)/10000;
	//	m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( j==p && k==o && l==r)
			return true;
		else return false;
	}else if(d==6)
	{
		k= n/100000;
		l=(n%100000)/10000;
		m=(n%10000)/1000;
		r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if(	k==p && l==o && m==r)
			return true;
		else return false;
	}else if(d==5)
	{
		l=(n%100000)/10000;
		m=(n%10000)/1000;
	//	r=(n%1000)/100;
		o=(n%100)/10;
		p= n%10;
		if( l==p && m==o)
			return true;
		else return false;
	}else if(d==4)
	{
		a= n/1000;
		b=(n%1000)/100;
		c=(n%100)/10;
		e=n%10;
		if(	a==e && b==c)
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

int digit(long long n)
{
	if (n/100000000000000>0)
		return 15;
	else if (n/10000000000000>0)
		return 14;
	else if (n/1000000000000>0)
		return 13;
	else if (n/100000000000>0)
		return 12;
	else if (n/10000000000>0)
		return 11;
	else if (n/1000000000>0)
		return 10;
	else if (n/100000000>0)
		return 9;
	else if (n/10000000>0)
		return 8;
	else if (n/1000000>0)
		return 7;
	else if (n/100000>0)
		return 6;
	else if (n/10000>0)
		return 5;
	else if(n/1000>0)
		return 4;
	else if(n/100>0)
		return 3;
	else if(n/10>0)
		return 2;
	else return 1;
}

int first(long long n, int dig)
{
	if (dig==15)
		return n/100000000000000;
	else if (dig==14)
		return n/10000000000000;
	else if (dig==13)
		return n/1000000000000;
	else if (dig==12)
		return n/100000000000;
	else if (dig==11)
		return n/10000000000;
	else if (dig==10)
		return n/1000000000;
	else if (dig==9)
		return n/100000000;
	else if (dig==8)
		return n/10000000;
	else if (dig==7)
		return n/1000000;
	else if (dig==6)
		return n/100000;
	else if (dig==5)
		return n/10000;
	else if(dig==4)
		return n/1000;
	else if(dig==3)
		return n/100;
	else if(dig==2)
		return n/10;
	else return n;
}

int second(long long n, int dig)
{
	if (dig==15)
		return (n%100000000000000)/10000000000000;
	else if (dig==14)
		return (n%10000000000000)/1000000000000;
	else if (dig==13)
		return (n%1000000000000)/100000000000;
	else if (dig==12)
		return (n%100000000000)/10000000000;
	else if (dig==11)
		return (n%10000000000)/1000000000;
	else if (dig==10)
		return (n%1000000000)/100000000;
	else if (dig==9)
		return (n%100000000)/10000000;
	else if (dig==8)
		return (n%10000000)/1000000;
	else if (dig==7)
		return (n%1000000)/100000;
	else if (dig==6)
		return (n%100000)/10000;
	else if (dig==5)
		return (n%10000)/1000;
	else if(dig==4)
		return (n%1000)/100;
	else if(dig==3)
		return (n%100)/10;
	else if(dig==2)
		return n%10;
}

int main()
{

	ofstream out;
//	out.open("output.txt");

	long long T,n,ans,dig;
	int f;
	char c;
	string s;

	cin>>T;
	for(long long t=1;t<=T;t++)
	{
		cin>>A>>B;
		ans=0;
		for(long long i= long long (ceil((sqrt(long double(A)))) ) ;i<=long long (floor((sqrt(long double(B)))) );i++)
		{
			dig=digit(i);
			f=first(i,dig);
			if(dig>1 && f>2)
			{
				i=1;
				for(int j=0;j<dig;j++)
					i=i*10;
				i--;
				continue;
			}
			if(dig>1 && second(i,dig)>2)
			{
				i=f+1;
				for(int j=1;j<dig;j++)
					i=i*10;
				i--;
				continue;
			}
			

				if(good(i, dig) && good(i*i,digit(i*i)))
				{
					ans++;
				}
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	//	out<<"Case #"<<t<<": "<<ans<<"\n";
	}

//	out.close();

	return(0);
}