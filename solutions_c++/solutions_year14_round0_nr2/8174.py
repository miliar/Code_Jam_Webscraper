#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	double C,F,X,Min,Counter,Time;
	cin>>T;
	for(int CASE=1 ; CASE<=T ; CASE++)
	{
		Time=2;
		Counter=0;
		cin>>C>>F>>X;
		Min=X/Time;
		while (true)
		{
			Counter+=(C/Time);
			Time+=F;
			if(Counter+(X/Time) <= Min)
			{
				Min=Counter+(X/Time);
			}
			else
				break;
		}
		printf("Case #%d: %.7f\n",CASE,Min);
	}
}