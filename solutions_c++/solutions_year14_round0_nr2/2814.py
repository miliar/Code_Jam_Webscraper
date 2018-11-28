#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
using namespace std;
void program(int xxxx)
{
	printf("Case #%d: ",xxxx);
	
	
	double  c,f,x;
	scanf("%lf %lf %lf",&c,&f,&x);
	double rate=2.0;
	
	/*double time[(int)ceil(x/f)];
	int i=0;
	double rati[(int)ceil(x/f)];
	
	time[i]=x/rate;
	rati[i]=c/rate;
	rate+=f;
	for(i=1;rate<=x;i++)
	{
		time[i]=rati[i-1]+(x/rate);
		rati[i]=rati[i-1]+(c/rate);
		rate+=f;
		printf("%lf\n",time[i]);
	}
	sort(time,time+i);
	
	printf("%.7lf\n",time[0]);*/
	
	double tempt=x/rate,tempr=c/rate;
	double t;
	rate+=f;
	while(true)
	{
		t=tempr+(x/rate);
		if(tempt<t) break;
		tempr+=c/rate;
		tempt=t;
		rate+=f;
	}
	printf("%.7lf\n",tempt);
}
int main()
{
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		program(i+1);
	}
	return 0;
}
