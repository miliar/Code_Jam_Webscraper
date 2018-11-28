#include<iostream>
using namespace std;

double r1,c1,r2,c2,V,X;
const double eps = 0.00000000001;
double check(double v1)
{
	double v2 = V-v1;
	return (v1*c1 + v2*c2)/V;
}


double b_search(double l,double r)
{
	double mid = (l+r)/2;
	double x = check(mid);
	if(fabs(check(mid)-X) < 0.000000000001) return mid;
	if(check(mid) < X) return b_search(mid,r);
	return b_search(l,mid);

}

void solve(int test)
{
	int N;
	scanf("%d%lf%lf",&N,&V,&X);
	scanf("%lf%lf",&r1,&c1);
	if(N == 1)
	{
		if(X == c1) printf("Case #%d: %.9lf\n",test, V/r1);
		else printf("Case #%d: IMPOSSIBLE\n", test);
		return;
	}



	scanf("%lf%lf",&r2,&c2);
	if(c2>c1)
	{
		swap(c1,c2);
		swap(r1,r2);
	}
	if(c1==c2)
	{
		if(c1==X)
		{
			double r = r1+r2;
			printf("Case #%d: %.9lf\n",test, V/r);
		}
		else printf("Case #%d: IMPOSSIBLE\n", test);
		return;
	}
	if(c1 == X)
	{
		printf("Case #%d: %.9lf\n",test, V/r1);
		return;
	}
	if(c2 == X)
	{
		printf("Case #%d: %.9lf\n",test, V/r2);
		return;
	}
	if(c1 < X || c2 > X)
	{
		printf("Case #%d: IMPOSSIBLE\n", test);
		return;
	}
	double v1 = b_search(0, V);
	
		double r = max(v1/r1,(V-v1)/r2);
		printf("Case #%d: %.9lf\n",test, r);
	//}
	//else printf("Case #%d: IMPOSSIBLE\n", test);
}



int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int TT;
	scanf("%d",&TT);
	for(int i =1; i <=TT; i++) solve(i);
	return 0;
}