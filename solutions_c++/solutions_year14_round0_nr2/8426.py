#include <iostream>
#include<cstdio>
using namespace std;

int main()
{
	int t,r=1;
	scanf("%d",&t);
	while(r<=t)
	{
	float c,f,s,cnt=0.0000000,g=2.0000000;
	scanf("%f%f%f",&c,&f,&s);
	while((((c/g)+(s/(g+f)))<(s/g))&&(c/g)>=0.0000001)
	{
		cnt=cnt+(c/g);
		g=g+f;
	}
	cnt=cnt+(s/g);
	printf("Case #%d: %.7f\n",r,cnt);
	r++;
	}
	return 0;
}
