#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	int t,n;
	double a[1000],b[1000],*ap,*bp;
	int i,j,k;
	int lb,rb;
	int ans1,ans2;
	ofstream f2("output4.txt");
	ifstream f1("D-large.in");
	f1>>t;
	for (i = 0; i < t; i++)
	{
		f1>>n;
		for (j = 0; j < n; j++)
			f1>>a[j];
		for (j = 0; j < n; j++)
			f1>>b[j];
		ap = a;
		bp = b;
		sort(ap,ap+n);
		sort(bp,bp+n);
		lb = 0;
		rb = n-1;
		ans1 = 0; ans2 = 0;
		for (j = 0; j < n; j++)
		{
			if (a[j]<b[lb])
			{
				rb--;
			}
			else
			{
				lb++;
				ans1++;
			}
		}
		rb = n-1; lb = 0;
		for (j = n-1; j >=0; j--)
		{
			if (a[j]>b[rb])
			{
				lb++;
				ans2++;
			}
			else
			{
				rb--;
			}
		}
		
		f2<<"Case #"<<i+1<<": "<<ans1<<" "<<ans2<<endl;
		
	}
	
	
}
