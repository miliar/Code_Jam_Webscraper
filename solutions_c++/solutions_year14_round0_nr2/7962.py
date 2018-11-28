#include<cstdio>
int z, i;
long double m, c, f, x, p, sum, time;
int main()
{
  scanf("%d", &z);
  
  for(i = 1; i <= z; i++)
  {
    scanf("%Lf%Lf%Lf", &c, &f, &x);
    sum = 0;
    p = 2;
    time = 0;
    m = x / p;
    while(sum < x)
    {
	time += c / p;
	p += f;
	if (time + (x - sum) / p < m) {m = time + (x - sum) / p;}
	else{break;}
    }
    printf("Case #%d: %.7Lf\n", i, m);
  }
  
return 0;
}