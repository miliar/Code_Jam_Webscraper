/*
Problem :Cookie Clicker Alpha
contest : Google code jam
author : saurabh jain
date :12/4/2014
*/

#include<iostream>
#include<stdio.h>
#include<string.h>
#include<iterator>
#include<stdlib.h>
#include<map>
#include<vector>
#include<algorithm>
#define MOD 1000000007
#define max(x,y)((x>y)?x:y)
#define min(x,y)((x<y)>x:y)
#define FEP(i,a,b) for(int i=a;i<b;i++)
#define PI 3.14
using namespace std;
unsigned long long mod_pow(unsigned long long num, unsigned long long pow, unsigned long long mod)
{
    unsigned long long test;
    unsigned long long n = num;
    for(test = 1; pow; pow >>= 1)
    {
        if (pow & 1)
            test = ((test % mod) * (n % mod)) % mod;
        n = ((n % mod) * (n % mod)) % mod;
    }
    return test; /* note this is potentially lossy */
}
int main(int argc, char* argv[])
{	int t;
	scanf("%d",&t);
	double C,F,X;
	for(int k=1;k<=t;k++)
	{	cin>>C>>F>>X;
		//scanf("%f %f %f",&C,&F,&X);
		double div =2.0;
		double ans1 = X/2.0;
		double ans2;
		double temp = C/div;
		div +=F;
		ans2 = temp+X/div;
		//cout<<ans1<<" "<<ans2<<endl;
		while(ans1>ans2)
		{
			ans1= ans2;
			temp +=C/div;
			div+=F;
			ans2 = temp+X/div;
		}
		if(ans1<ans2)
		{	printf("Case #%d: %.7f\n",k,ans1);
		}
		else
		{	printf("Case #%d: %.7f\n",k,ans2);
		}
	}	
}
