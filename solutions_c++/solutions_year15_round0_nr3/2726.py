#include <iostream>
#include <math.h>
#include <string>
#include <stdlib.h>

using namespace std;
#include <fstream>
using std::ifstream;
using std::ofstream;

int sign(int x)
{
	if(x<0)
		return -1;
	return 1;
}

struct point{
	int count;
	int index;
};

bool valid1(point l, point r, int n)
{
	if(l.count == r.count)
		if(l.index < (r.index-2))
			return true;
	if(l.count < (r.count - 1))
		return true;
	if(l.count == r.count-1)
		if(l.index < (n + r.index - 2))
			return true;
	return false;
}

bool valid2(point l, point r, int n)
{
	if(l.count == r.count)
		if(l.index < (r.index-3))
			return true;
	if(l.count < (r.count - 1))
		return true;
	if(l.count == r.count-1)
		if(l.index < (n + r.index - 3))
			return true;
	return false;
}

bool valid3(point l, point r, int n)
{
	if(l.count == r.count)
		if(l.index < (r.index-1))
			return true;
	if(l.count < (r.count - 1))
		return true;
	if(l.count == r.count-1)
		if(l.index < (n + r.index - 1))
			return true;
	return false;
}

int q[4][4] = {{1,2,3,4}, {2,-1,4,-3}, {3,-4,-1,2}, {4,3,-2,-1}};

int check(string s, point l, point r, int n)
{	
	if(l.index == n-1)
	{
		l.index = 0;
		l.count += 1;
	}
	else
		l.index += 1;

	if(r.index == 0)
	{
		r.index = n-1;
		r.count -= 1;
	}
	else
		r.index -= 1;

	int b = (int)(s[l.index]) - 103;
	if(l.count == r.count)
	{
		for(int y=l.index + 1; y<=r.index; y++)
		{
			int d = (int)(s[y]) - 103;
			int z = q[abs(b)-1][d-1];
			b = z*sign(b);
		}
		return b;
	}

	for(int y=l.index + 1; y<n; y++)
	{
		int d = (int)(s[y]) - 103;
		int z = q[abs(b)-1][d-1];
		b = z*sign(b);
	}

	int w = 1;
	for(int y=0; y<n; y++)
	{
		int d = (int)(s[y]) - 103;
		int z = q[abs(w)-1][d-1];
		w = z*sign(w);
	}

	for(int x=l.count+1; x<r.count; x++)
	{
		int z = q[abs(b)-1][abs(w)-1];
		b = z*sign(b)*sign(w);
	}

	for(int y=0; y<=r.index; y++)
	{
		int d = (int)(s[y]) - 103;
		int z = q[abs(b)-1][d-1];
		b = z*sign(b)*sign(d);
	}

	return b;
}

int main()
{
	ifstream in;
	in.open("C-small-attempt0.in");
	ofstream out;
	out.open("C-small-attempt0.out");
	int t;
	in>>t;

	for(int i=1; i<=t; i++)
	{
		int n, m;
		in>>n>>m;
		string s;
		in>>s;

		int p=n*m;

		if(p<3)
			out<<"Case #"<<i<<": NO\n";

		else if(p==3)
		{
			int g = 0;
			bool flag = true;
			for(int e=0; e<m && flag; e++)
			{
				for(int f=0; f<n && flag; f++)
				{
					int h = (int)(s[f]) - 105;
					if(g==h)
						g = g+1;
					else
						flag = false;
				}
			}
			if(flag)
				out<<"Case #"<<i<<": YES\n";
			else
				out<<"Case #"<<i<<": NO\n";
		}

		else
		{
			bool flag = true;
			bool change = true;
			point l, r;
			l.count = 1;
			r.count = m;
			l.index = 0;
			r.index = n-1;
			int a, b, c;
			a = (int)(s[l.index]) - 103;
			c = (int)(s[r.index]) - 103;
			
			while(flag && change)
			{
				//out<<a<<" "<<c<<"\n";
				change = false;
				if(a==2 && c==4)
				{
					//out<<"1    "<<a<<" "<<c<<"\n";
					if(valid3(l, r, n))
					{
						b = check(s, l, r, n);
						if(b==3)
							flag = false;
					}
				}
				else if(a!=2 && c==4)
				{
					//out<<"2    "<<a<<" "<<c<<"\n";
					if(valid1(l, r, n))
					{
						change = true;
						if(l.index == n-1)
						{
							l.index = 0;
							l.count += 1;
						}
						else
							l.index += 1;

						int d = (int)(s[l.index]) - 103;
						int z = q[abs(a)-1][d-1];
						a = z*sign(a);
					}
				}
				else if(a==2 && c!=4)
				{
					//out<<"3    "<<a<<" "<<c<<"\n";
					if(valid1(l, r, n))
					{
						change = true;
						if(r.index == 0)
						{
							r.index = n-1;
							r.count -= 1;
						}
						else
							r.index -= 1;

						int d = (int)(s[r.index]) - 103;
						int z = q[d-1][abs(c)-1];
						c = z*sign(c);
					}
				}
				else if(a!=2 && c!=4)
				{
					//out<<"4    "<<a<<" "<<c<<"\n";
					if(valid2(l, r, n))
					{
						change = true;
						if(l.index == (n-1))
						{
							l.index = 0;
							l.count += 1;
						}
						else
							l.index += 1;

						if(r.index == 0)
						{
							r.index = n-1;
							r.count -= 1;
						}
						else
							r.index -= 1;

						int d = (int)(s[l.index]) - 103;
						int z = q[abs(a)-1][d-1];
						a = z*sign(a);
						//out<<d<<"\n";
						d = (int)(s[r.index]) - 103;
						z = q[d-1][abs(c)-1];
						c = z*sign(c);
					}
				}
			}
			if(!flag)
				out<<"Case #"<<i<<": YES\n";
			else
				out<<"Case #"<<i<<": NO\n";
		}
	}

	in.close();
	out.close();
}
