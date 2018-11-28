#include<iostream>
#include<cstdio>
#include<iomanip>
using namespace std;
int main()

{
	double c,fo,need2,f,x,temp,f1,f2,f3,time,time1,time2,have,need;
	int t,cou,count,ans,l,m,n,ch;
	scanf("%d",&t);
	cou=0;
	while(t--)
	{	
	cou++;
	fo=2;temp=0;count=1;f2=0;time=0;
	//scanf("%f%f%f",&c,&f,&x);
	cin>>c>>f>>x;ch=1;
	if(c>x)
{
	time=x/fo;

}
	else
	{
		time=c/fo;
		while(ch)
		{
			f2=fo+f;
			time1=x/f2;
			time2=(x-c)/fo;
			if(time1<time2)
			{
				fo+=f;
				time+=(c/fo);
				//printf("inside");
			}
			else
			{
				time+=(x-c)/fo;
				ch=0;break;
			}
		}
	}
	cout<<"Case #"<<cou<<": " <<fixed<<setprecision(7)<<time<<endl;
	}
	return 0;
}
