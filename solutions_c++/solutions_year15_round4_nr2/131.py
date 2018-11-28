#include <cassert>
#include <cstdio>
#include <cmath>
#include <vector>


int toInt(double x)
{
	x *= 100000.0;
	return (int)(x + 0.1);
}

int signT(double t)
{
	if(toInt(t) > 0)
		return 2;
	if(toInt(t) < 0)
		return 0;
	return 1;
}

double solve(const double vol, const double temp, const std::vector<double> vols, std::vector<double> temps)
{
	const int n = (int)vols.size();
	for(int i = 0; i < n; i++)
		temps[i] -= temp;
	
	{
		bool fl[3] = {false, false, false};
		for(int i = 0; i < n; i++)
			fl[signT(temps[i])] = true;

		if(!fl[1] && !(fl[0] && fl[2]))
			return -1;
	}

		
	std::vector<bool> active(n, true);
	double rate = 0.0, tx = 0.0;
	for(int i = 0; i < n; i++)
	{
		rate += vols[i];
		tx += vols[i] * temps[i];
	}
	
	//for(int i = 0; i < n; i++)
	//	printf("%lf ", vols[i]);
	//printf("\n");
	//for(int i = 0; i < n; i++)
	//	printf("%lf ", temps[i]);
	//printf("\n");
	
	//printf("%lf %lf\n", rate, tx);
	while(fabs(tx) > 1e-8)
	{
		int sign = (tx < 0) ? 0 : 2;
		
		int ti = -1;
		for(int i = 0; i < n; i++)
			if(signT(temps[i]) == sign && active[i])
			{
				if(ti < 0 || fabs(temps[i]) > fabs(temps[ti]))
					ti = i;
			}
			
		if(ti < 0)
			break;
		active[ti] = false;
		
		double alpha = tx / (temps[ti] * vols[ti]);
		rate -= std::min(alpha, 1.0) * vols[ti];
		tx -= std::min(alpha, 1.0) * vols[ti] * temps[ti];
		
		//printf("%lf %lf\n", rate, tx);
		
		if(alpha <= 1.0)
			break;
	}
	
	return vol / rate;
}

int main()
{
	freopen("input.txt", "r", stdin);
	
	int tn;
	scanf("%i\n", &tn);
	for(int t = 1; t <= tn; t++)
	{
		int n;
		double v, x;
		scanf("%i %lf %lf\n", &n, &v, &x);
		
		std::vector<double> vol, temp;
		for(int i = 0; i < n; i++)
		{
			double vi, xi;
			scanf("%lf %lf\n", &vi, &xi);
			vol.push_back(vi);
			temp.push_back(xi);
		}
		
		double res = solve(v, x, vol, temp);
		printf("Case #%i: ", t);
		if(res < 0)
			printf("IMPOSSIBLE\n");
		else
			printf("%.10lf\n", res);
	}
	
	return 0;
}

