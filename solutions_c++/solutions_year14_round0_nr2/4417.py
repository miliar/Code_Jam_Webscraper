#include <stdio.h>

void solve()
{
	double c, f, x, min, speed, pass, need;
	
	scanf("%lf %lf %lf", &c, &f, &x);
	//printf("%f %f %f\n", c, f, x);
	speed = 2;
	pass = 0;
	while (1)
	{
		need = x / speed;
		if (pass + need < min) min = pass + need;
		pass += c / speed;
		speed += f;
		if (pass > min) break;
	}
	printf("%.7lf\n", min);
}

int main()
{
	int t, i;
	
	scanf("%d", &t);
	for (i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	
	return 0;
}