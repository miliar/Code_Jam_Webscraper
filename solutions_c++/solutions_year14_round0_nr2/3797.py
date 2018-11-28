#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
    int test;
	double c,f,x,t,r,t1,t2;
	int i=0;
	cin>>test;
	while(test--)
	{
	    i++;
		cin>>c>>f>>x;
		r=2;
		t=0;
		while(true)
		{
		    t1=c/r+x/(r+f);
		    t2=x/r;
			if(t1<t2)
			{
				t=t+c/r;
				r=r+f;

			}
			else
			break;
		}
		t=t+x/r;
		printf("Case #%d: %.7f\n",i,t);
    }
}
