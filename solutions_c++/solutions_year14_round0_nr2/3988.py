//Bismillaahir Rahmaanir Raheem.

#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double sum1 = 0, sum2, C, F, X, ans, T;
	int n, i, j;
	freopen("E:\\Special Applications\\MS Visual C++ 6.0\\MSDev98\\MyProjects\\Google Codejam 2014\\Input and Output\\B-large.in", "r", stdin);
	freopen("E:\\Special Applications\\MS Visual C++ 6.0\\MSDev98\\MyProjects\\Google Codejam 2014\\Input and Output\\LargeOutputProbB.txt", "w", stdout);
	cin>>T;
	for(j = 1; j <= T; j++)
	{
		cin>>C>>F>>X;
		for(n = 1;n <= X;n++)
		{
			sum2 = 0;
			for(i = 1; i <= n; i++)
			{
				sum2 += C/(2+(i-1)*F);
			}
			sum2 += X/(2 + n*F);
			if(sum2 > sum1 && n > 1)
			{
				break;
			}
			sum1 = sum2;
		}
		if(sum1 < X/2)
			ans = sum1;
		else
			ans = X/2;
		cout<<"Case #"<<j<<": ";
		printf("%7lf\n", ans);
	}
	
	return 0;
}