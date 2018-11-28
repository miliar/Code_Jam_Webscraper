#include <iostream>
#include <cstdio>

using namespace std;

int a[1002];
void qsort(int l,int r)
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
}

int max(int a, int b)
{
	if (a>b) return a;
	return b;
}

int main ()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("t1.out","w",stdout);
	
	int t,tt,d,i;
	
	cin >> t;
	for (tt=1; tt<=t; tt++)
	{
		cin >> d;
		for (int i=1; i<=d; i++) 
		{
			cin >> a[i];
		}
		qsort(1,d);
		int min=0;
		while (1) {
			int c=max(a[1]/2,a[2]);
			
		}
	} 
	
	return 0;
}
