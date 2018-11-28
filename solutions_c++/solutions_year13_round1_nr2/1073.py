#include <iostream>
using namespace std;

int minofh(int e,int r,int t,int a[10],int p,int emax)
{
	if(p>=t)
	return 0;
	
	int mi=0;
	for(int i=e;i>=0;i--)
	{
		if(e-i>=0){
	    int ei;
	    if(emax<e-i+r)
	    ei=emax;
	    else ei=e-i+r;
		int curent=minofh(ei,r,t,a,p+1,emax)+i*a[p];
		if(curent>mi)
		mi=curent;
	    }
	}
		
	return mi;
	
}

int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		int e,r,t,a[10];
		cin>>e>>r>>t;
		for(int j=0;j<t;j++)
		cin>>a[j];
		cout<<"Case #"<<i<<": "<<minofh(e,r,t,a,0,e)<<endl;
	}
}
