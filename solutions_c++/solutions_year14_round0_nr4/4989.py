#include<iostream>
#include<algorithm>
#include<stdio.h>
using namespace std;

int deciteful(float *x, float *y, int N)
{
	if(N==1)
	{
		if(y[0]>x[0])
		{
			return 0;
		}
		else
		{
			return 1;
		}
	}
	else
	{
		if (*max_element(&x[0],&x[0]+N)<*max_element(&y[0], &y[0]+N))
		{
			return deciteful(x+1,y,N-1);
		}
		else
		{
			return 1+deciteful(x,y,N-1);
		}
	}
}

int war(float *x, float *y, int N)
{
	return N - deciteful(y,x,N);
}

int main()
{
	int T;
	cin>>T;
	int N,ans1,ans2;
	float x[1002], y[1002];
	int t=1;
	while(t<=T)
	{
		cin>>N;
		ans1=ans2=0;
		for(int i=0; i<N; i++)
		{
			cin>>x[i];
		}
		sort(&x[0], &x[0]+N);
		for(int i=0; i<N; i++)
		{
			cin>>y[i];
		}
		sort(&y[0], &y[0]+N);
		ans1 = deciteful(x,y,N);
		ans2 = war(x,y,N);
		printf("Case #%d: %d %d\n",t,ans1,ans2);
		t++;
	}
	return 0;
	
}
