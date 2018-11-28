#include <fstream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <string>
#include <set>
using namespace std;


int mult(int a,int b)
{
	int g=1;
	if (a<0)
	{
		g*=-1;
		a*=-1;
	}
	if (b<0)
	{
		g*=-1;
		b*=-1;
	}

	if (a==1)
	{
		return g*b;
	}
	if (b==1)
		return g*a;
	if (a==2)
	{
		if (b==2)
			return g*(-1);
		if (b==3)
			return g*4;
		if (b==4)
			return g*(-3);
	}
	if (a==3)
	{
		if (b==2)
			return g*(-4);
		if (b==3)
			return g*(-1);
		if (b==4)
			return g*2;
	}
	if (a==4)
	{
		if (b==2)
			return g*3;
		if (b==3)
			return g*(-2);
		if (b==4)
			return g*(-1);
	}
}


int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int q;
	cin>>q;
	for (int qq=0;qq<q;qq++)
	{
		cout<<"Case #"<<qq+1<<": ";
		long long l,x;
		cin>>l>>x;
		string h;
		cin>>h;
		string w="";
		for (int i=0;i<x;i++)
		{
			w+=h;
		}
		l*=x;
		vector <int> a(l);
		for (int i=0;i<l;i++)
		{
			if (w[i]=='i')
				a[i]=2;
			if (w[i]=='j')
				a[i]=3;
			if (w[i]=='k')
				a[i]=4;
		}
		int ff=1;
		for (int i=0;i<l;i++)
			ff=mult(ff,a[i]);
		if (ff!=mult(mult(2,3),4))
		{
			cout<<"NO"<<endl;
		}
		else
		{
			long long mn=2e17;
			int w=1;
			for (int i=0;i<l;i++)
			{
				w=mult(w,a[i]);
				if (w==2)
					mn=min(mn,i+0ll);
			}
			w=1;
			long long mx=-1;
			for (int i=l-1;i>0;i--)
			{
				w=mult(a[i],w);
				if (w==4)
				{
					mx=max(mx,i+0ll);
				}
			}
			if (mx-mn>1)
				cout<<"YES"<<endl;
			else
				cout<<"NO"<<endl;
		}


		
		
	}
	return 0;
}
