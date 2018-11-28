//Problem B. Cookie Clicker Alpha CODEJAM2014
#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    
    int test,caseno=0;
    scanf("%d", &test);
    while(test--)
    {
    	caseno++;
    	double c,f,x,t=0.0,n=2.0;
    	scanf("%lf %lf %lf", &c, &f, &x);
    	
    	double cookies=x;
    	while( cookies>0 )
    	{
    		if((cookies-c)/n > cookies/(n+f))
			{
    			t += c/n;
    			n += f;
    		}
    		else
			{
    			t += cookies/n;
				break;
    		}
    	}
    	printf("Case #%d: %lf\n", caseno, t);
    }
}
