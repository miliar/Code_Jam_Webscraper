#include<cstdio>
#include<algorithm>
#include<iostream>
#define gc getchar_unlocked
using namespace std;
void inline scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
int main()
{
	int t,a,b,k,count=0,caseno=1;
	scanint(t);
	while(t--)
	{
		scanint(a);
		scanint(b);
		scanint(k);
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				int zero=i&j;
				if(zero<k||zero==0)
				count++;
			}
		}
		cout<<"Case #"<<caseno<<": "<<count<<"\n";
		count=0;
		caseno++;
		}
	return 0;
	
}

