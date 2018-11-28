#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
	int n;
	double t1,t2,produce,final;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		produce=2;
		final=0;

			double C,F,X;
			cin>>C>>F>>X;
			if(C>X)
				final=X/produce;
			else
			{
				while(1)
				{
					t1=C/produce+X/(produce+F);
				    t2=X/produce;
				    if(t2<=t1) { final+=t2; break; }
				    else 
				    {
				    	final+=C/produce;
				    	produce+=F;
				    }
				}
			}

		printf("Case #%d: %.7f\n",i+1,final);
	}
}