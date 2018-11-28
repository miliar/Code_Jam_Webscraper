#include<stdio.h>
#include<iostream>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<map>
#include<utility>
#define PB push_back
#define MP make_pair
#define LL long long int
#define sc(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
using namespace std;
int main()
{
	int k,t,i,j,n;
	double temp,c,f,x,time,ans,min;
	sc(t);
	for(k=1;k<=t;k++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		time = 0;
		i = 0;
		min = 10000000;
		while(1)
		{
			ans = time + ((x*1.0)/(2 + (float)(i*f)));
			if(ans < min)
			{
				min = ans;
				
			}
			
			temp = ((c*1.0)/(2 + (i*f)));
			time += temp;
			if(time > min)
			{
				break;
			}
			i++;
		}
		cout<<"Case #"<<k<<": ";
		//cout<<min<<endl;
		printf("%.6f\n",min);
	}	
	return 0;
}

