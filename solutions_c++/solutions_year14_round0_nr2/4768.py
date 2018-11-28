#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <vector>

using namespace std;
int main(void)
{
	int n;
	scanf("%d",&n);
	float c,f,x,base=2;
	for(int i=1; i<=n; i++)
	{
		float cost=0.0, cur_min=0.0;
		scanf("%f%f%f",&c,&f,&x);
		cur_min = x/base;
		int j=0;
		if(x<=c)
		{
			cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<cur_min<<endl; 
		}	
		else
		{
			do
			{
				cost = 0.0;
				j++;
				for(int k=1; k<=j; k++)
					cost += c/(2+f*(k-1));
				cost += x/(2+j*f);
				if(cost<cur_min)
					cur_min = cost;
			}while(cost<=cur_min);
			cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<cur_min<<endl; 
		}
	}
	return 0;
}