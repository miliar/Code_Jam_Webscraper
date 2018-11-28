#include <iostream>
#include <cstdio>

using namespace std;

int a[1002];
/*void qsort(int l,int r)
{
	int tl,tr,mid,t;
	tl=l;
	tr=r;
	mid=a[(tl+tr)/2];
	do 
	{
		while (a[tl]>mid) tl++;
		while (a[tr]<mid) tr--;
		if (tl<=tr)
		{
			t=a[tl];
			a[tl]=a[tr];
			a[tr]=t;
			tl++;
			tr--;
		}
	} while (tl<=tr);
	if (tl<r) qsort(tl,r);
	if (l<tr) qsort(l,tr);
}*/

int max(int a, int b)
{
	if (a>b) return a;
	return b;
}

int main ()
{
	freopen("B-large.in","r",stdin);
	freopen("t1.out","w",stdout);
	//freopen("B.in","r",stdin);
	int t,tt,d,i,maxx;
	
	cin >> t;
	for (tt=1; tt<=t; tt++)
	{
		cin >> d;
		maxx=0;
		for (int i=1; i<=d; i++) 
		{
			cin >> a[i];
			maxx=max(a[i],maxx);
		}
		//qsort(1,d);
		int min=10000000,ans=0;
		for (int i=1; i<=maxx; i++)
		{
			ans=0;
			for (int j=1; j<=d; j++) ans+=(a[j]+i-1)/i-1;
			if (ans+i<min) min=ans+i;
		}
		cout << "Case #" << tt << ": ";
		cout << min << endl;
	} 
	
	return 0;
}
