#include<iostream>
#include<string>
using namespace std;

int main()
{
	long long t,n,i,ans,T,z,w,u,x,g,o,r,f,se,a,b,c,d,ni;
	string s;
	cin>>t;
	for(T=1;T<=t;T++)
	{
		z=0,w=0,u=0,x=0,g=0,o=0,r=0,f=0,se=0,a=0,b=0,c=0,d=0,ni=0;
		cin>>s;
		n=s.length();
		for(i=0;i<n;i++)
		{
			if(s[i]=='Z')
				z++;
			else if(s[i]=='W')
				w++;
			else if(s[i]=='U')
				u++;
			else if(s[i]=='X')
				x++;
			else if(s[i]=='G')
				g++;
		}
		a=o=z+w+u;
		b=r=z+u;
		c=f=u;
		d=se=x;
		for(i=0;i<n;i++)
		{
			if(s[i]=='O'&&o>0)
			{
				o--;
				s[i]='a';
			}
			else if(s[i]=='R'&&r>0)
			{
				r--;
				s[i]='a';
			}
			else if(s[i]=='F'&&f>0)
			{
				f--;
				s[i]='a';
			}
			else if(s[i]=='S'&&se>0)
			{
				se--;
				s[i]='a';
			}
		}
		for(i=0;i<n;i++)
		{
			if(s[i]=='O')
				o++;
			else if(s[i]=='R')
				r++;
			else if(s[i]=='F')
				f++;
			else if(s[i]=='S')
				se++;
		}
	
		ni=n-z*4-o*3-w*3-r*5-u*4-f*4-x*3-se*5-g*5;
		ni/=4;
		
		cout<<"Case #"<<T<<": ";
		for(i=0;i<z;i++)
			cout<<"0";
		for(i=0;i<o;i++)
			cout<<"1";
		for(i=0;i<w;i++)
			cout<<"2";
		for(i=0;i<r;i++)
			cout<<"3";
		for(i=0;i<u;i++)
			cout<<"4";
		for(i=0;i<f;i++)
			cout<<"5";
		for(i=0;i<x;i++)
			cout<<"6";
		for(i=0;i<se;i++)
			cout<<"7";
		for(i=0;i<g;i++)
			cout<<"8";
		for(i=0;i<ni;i++)
			cout<<"9";
		cout<<endl;
	}
	return 0;
}