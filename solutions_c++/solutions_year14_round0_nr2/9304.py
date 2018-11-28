#include<bits/stdc++.h>

using namespace std;

int main(void)
{
	int t;
	cin >> t;
	for(int T=1;T<=t;T++)
	{
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		double ini = 2.0f;
		double time = 0;
		bool flag = false;
		while(flag == false)
		{
			if(x/ini <= (c/ini + (x/(ini+f))))
			{
				flag = true;
				time+=(x/ini);
			}
			else
			{
				time+=(c/ini);
				ini+=f;
			}
		}
	
		cout << "Case #" << T << ": "; 
		printf("%.7lf\n",time);
	}
}
