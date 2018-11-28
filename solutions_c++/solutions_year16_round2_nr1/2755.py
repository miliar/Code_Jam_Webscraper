#include <iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstring>
//#include<bits/stdc++.h>

#define pb push_back
#define ll long long int
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
  	freopen("output.txt","w",stdout);
	ll t,n,i,ans,T,z,w,u,x,g,o,r,f,se,a,b,c,d,ni;
	char s[2003];
	scanf("%lld",&t);
	for(T=1;T<=t;T++)
	{
		z=0,w=0,u=0,x=0,g=0,o=0,r=0,f=0,se=0,a=0,b=0,c=0,d=0,ni=0;
		scanf("%s",s);
		n=strlen(s);
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
		//printf("s=%s\n",s);
		ni=n-z*4-o*3-w*3-r*5-u*4-f*4-x*3-se*5-g*5;
		ni/=4;
		printf("Case #%lld: ",T);
		for(i=0;i<z;i++)
			printf("0");
		for(i=0;i<o;i++)
			printf("1");
		for(i=0;i<w;i++)
			printf("2");
		for(i=0;i<r;i++)
			printf("3");
		for(i=0;i<u;i++)
			printf("4");
		for(i=0;i<f;i++)
			printf("5");
		for(i=0;i<x;i++)
			printf("6");
		for(i=0;i<se;i++)
			printf("7");
		for(i=0;i<g;i++)
			printf("8");
		for(i=0;i<ni;i++)
			printf("9");
		printf("\n");
	}
	return 0;
}

