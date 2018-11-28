#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;
inline int mini(int a,int b)
{
	return a>=b?b:a;
}
int main ()
{
	int t,x,r,c;
	bool done;
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small.out","w",stdout);
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		cin>>x>>r>>c;
		done=false;
//		check if x is a factor of r*c or not
		if(!((r*c)%x))
		{
//		check if min(r,c)>x-2 or not
			if(min(r,c)>(x-2))
			{
				done=true;
			}
		}
		if(done)
		{
			printf("Case #%d: GABRIEL\n",z);
		}
		else
		{
			printf("Case #%d: RICHARD\n",z);
		}
	}
	return 0;
}
