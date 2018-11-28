#include <iostream>
#include<cstdio>
using namespace std;

int main() {
 	int j,n;
	cin>>n;
	long long int i;
	double x,y,c,f,w,ans,t;
	for(j=1;j<=n;j++)
	{
	cin>>c>>f>>w;
	ans=w/2;
	i=0;
	x=y=0.0;
	while(1)
	{
		x=x+(c/(2+(f*i)));
		y=w/(2+(f*(i+1)));
		t=x+y;
		if(t>ans)
			break;
		else
			ans=t;
		i++;
		}
		
		printf("Case #%d: %.7f\n",j,ans);
	}
	return 0;
}
