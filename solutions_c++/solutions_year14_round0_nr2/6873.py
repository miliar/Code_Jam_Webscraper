#include <cstdio>

int main()
{
				int nbTests;
				scanf("%d", &nbTests);
				for(int testCase = 0; testCase < nbTests; ++testCase)
				{
								double c,f,x;
								scanf("%lf %lf %lf", &c, &f, &x);
								//printf("$$ %lf -- %lf -- %lf\n", c, f, x);
								//int n = (f*x-2) / (c * f);
								//n--;
								//if(n < 0)
								//				n = 0;
								//printf("$$ %d\n", n);
								double sum = c / 2.;
								int n = 1;
								double output1 = c / 2. + x / (f + 2.);
								double output2 = x / 2.;
								while(output2 > output1)
								{
												output2 = output1;
												sum += c / (n*f + 2.);
												n++;
												output1 = sum + x / (n*f + 2);
												//printf("$$ %lf", output);
								}
								printf("Case #%d: %0.7lf\n", testCase + 1, output2);

				}
				return 0;
}
