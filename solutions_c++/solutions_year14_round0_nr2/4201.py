#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
#include<cstdio>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	int count = 0;
	while (T--)
	{
		if (count != 0)
			cout << endl;
		count++;
		cout << "Case #" << count << ": ";
		double C, F, X,R=0,production=2;
		scanf("%lf %lf %lf",&C,&F, &X);
		while (1)
		{
			double wait = X / production;
			double buildfarm = (C / production) + (X / (production + F));
			if (wait <= buildfarm)
			{
				R += wait;
				break;
			}
			R += C / production;
			production += F;
		}
		printf("%.7lf", R);
	}
	return 0;
}