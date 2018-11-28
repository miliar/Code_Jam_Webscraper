#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int I=1;I<=T;I++)
	{
		int n;
		cin >> n;
		double c,t;
		cin >> c >> t;
		printf("Case #%d: ",I);
		//cout << "Case #" << I << ": ";
		if(n==1)
		{
			double c1,t1;
			cin >> c1 >> t1;
			if(t1!=t)
				//cout << "IMPOSSIBLE" << endl;
				printf("IMPOSSIBLE\n");
			else
				//cout << c/c1 << endl;
				printf("%.7f\n",c/c1);
		}
		else if(n==2)
		{
			double c1,t1,c2,t2;
			cin >> c1 >> t1 >> c2 >> t2;
			if(t1==t && t2==t)
				printf("%.7f\n",c/(c1+c2));
			else if(t1==t)
				printf("%.7f\n",c/(c1));
			else if(t2==t)
				printf("%.7f\n",c/(c2));
			else if((t1<t && t2<t) || (t<t1 && t<t2))
				//cout << "IMPOSSIBLE" << endl;
				printf("IMPOSSIBLE\n");
			else
			{
				double time1,time2;
				time2 = c*(t-t1)/(c2*(t2-t1));
				time1 = (c-c2*time2)/c1;
				//cout << max(time1,time2) << endl;
				printf("%.7f\n",max(time1,time2));
			}
		}
	}
}
