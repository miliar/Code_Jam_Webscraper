#include<iostream>
#include <iomanip> 
#include<cstdio>
using namespace std;
int main()
{
	int t;
	double x,c,f,time = 0.0,cr = 0;
	double t1,t2,t3;
	cin>>t;
	int count = 0;
	for(int i =0;i<t;i++)
	{
		time = 0;
		cin>>c;
		cin>>f;
		cin>>x;
		cr = 2;
		time = x/cr;
		count = 0;
		while((x/cr) > ((c/cr)+(x/(f+cr))))
		{
			if(count == 0)
				time = 0;
			time = time+(c/cr);
			cr = cr+f;
			count++;
		}
		if(count > 0)
			time = time+(x/cr);
		cout<<"Case #"<<i+1<<": ";
		printf("%.7lf\n",time);
	}
return 0;
}
