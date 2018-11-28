#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<fstream>
using namespace std;


int d(float *x, float *y, int N)
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
			return d(x+1,y,N-1);
		}
		else
		{
			return 1+d(x,y,N-1);
		}
	}
}

int main()
{
	ofstream cout("o2.txt");
	ifstream cin("D-large.in");
	int T;
	cin>>T;
	int N,a1,a2;
	float a[1002], b[1002];
	int t=1;
	while(t<=T)
	{
		cin>>N;
		a1=a2=0;
		for(int i=0; i<N; i++)
		{
			cin>>a[i];
		}
		sort(&a[0], &a[0]+N);
		for(int i=0; i<N; i++)
		{
			cin>>b[i];
		}
		sort(&b[0], &b[0]+N);
		a1 = d(a,b,N);
		a2 = N - d(b,a,N);
		cout<<"Case #"<<t<<": "<<a1<<" "<<a2<<"\n";
		t++;
	}
	return 0;
	
}
