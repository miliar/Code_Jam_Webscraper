#include"../std_lib_facilities.h"

int main()
{
	ifstream ifs("input.in");
	ofstream ofs("output.out");
	int solve,count=0;
	ifs>>solve;
	while (solve>count)
	{
		++count;
		ofs<<"Case #"<<count<<": ";
		int n;
		double a[1000],b[1000];
		ifs>>n;
		for (int i=0; i<n; ++i)
			ifs>>a[i];
		for (int i=0; i<n; ++i)
			ifs>>b[i];
		int s1=0,s2=0;
		sort(a,a+n);
		sort(b,b+n);
		int x=0,y=n-1;
		for (int i=0; i<n; ++i)
			if (a[i]>b[x])
			{
				++s1; ++x;
			}
			else
			{
				--y;
			}
		x=0; y=n-1;
		for (int i=n-1; i>=0; --i)
		{
			if (a[i]>b[y])
			{
				++s2; ++x;
			}
			else
			{
				--y;
			}
		}
		ofs<<s1<<" "<<s2<<endl;
	}
	ifs.close(); ofs.close();
	return 0;
}