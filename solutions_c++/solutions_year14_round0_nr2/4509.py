#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<vector>
#include<map>
#include<list>
#include<string.h>
using namespace std;
int main()
{
	int t,kp;
	cin>>kp;
	for(int t=1;t<=kp;t++){
		double c,f,x;
		cin>>c>>f>>x;
		int k=0;
		while( x/(2.0+f*k) >   c/(2.0+f*k)  +  x/(2.0+f*(k+1)) )
			k++;
			//cout<<"k is "<<k<<endl;
		double ans=0.0;
		ans=x/(2.0+f*k);
		for(int i=0;i<k;i++)
			ans+=c/(2.0+f*i);
		printf("Case #%d: %.9f\n",t,ans);
	}
	
	
	
	return 0;
}

