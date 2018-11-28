#include <iostream>
#include<cstdio>
#define gc getchar
using namespace std;
void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("cj_1.txt","w",stdout);
	int t,n;
	scanint(t);
	for(int z=0;z<t;z++)
	{
	    scanint(n);
	    int a[n],meth1=0,meth2=0,maxdiff,diff;
	    maxdiff=0;
	    for(int i=0;i<n;i++)
                scanint(a[i]);
     for(int i=0;i<n-1;i++)
     {
	        diff=a[i]-a[i+1];
	        if(maxdiff<diff)
	            maxdiff=diff;
	        if(diff>0)
	            meth1=meth1+diff;
	    }
	    for(int i=0;i<n-1;i++)
	    {
	        if(maxdiff>=a[i])
	        {
	            meth2=meth2+a[i];
	        }
	        else
	        {
	            meth2=meth2+maxdiff;
	        }
	           
	    }
	    cout<<"Case #"<<z+1<<": "<<meth1<<" "<<meth2<<endl;
	}
	return 0;
}
