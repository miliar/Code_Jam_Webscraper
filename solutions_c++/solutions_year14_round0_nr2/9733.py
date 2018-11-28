#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	int n;
	double C,F,X,t,k,s;
	//freopen("d://1.txt","r",stdin);
	cin>>n;
	for(int i=0;i<n;i++)
	{
		k=2;
		cin>>C>>F>>X;
		t=C/2;
		if(X>C)
		{
			X=X-C;
			while(X>0)
			{
				if(X/k>(X+C)/(F+k))
				{
				   k=F+k;
				   //X=X+C;
				   t+=C/k;
			    }
			    else
			    {
			    	t+=X/k;
			    	break;
			    }
			}		   	
		}
		else
		{
			t=X/2;
		}
		printf("Case #%d: %.7lf\n",i+1,t);
		
	}
	return 0;
}
