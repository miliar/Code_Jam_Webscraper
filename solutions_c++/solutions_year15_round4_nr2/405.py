#include <bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define MP make_pair
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
const double eps=1e-9;

int N;
double V,X;
double R1,C1,R2,C2;

int main()
{
	int NumberOfTestcases;
	scanf("%d",&NumberOfTestcases);
	for(int CaseNumber=1;CaseNumber<=NumberOfTestcases;CaseNumber++)
	{
		scanf("%d%lf%lf",&N,&V,&X);
		if(N==1)
		{
			scanf("%lf%lf",&R1,&C1);
			printf("Case #%d: ",CaseNumber);
			if(abs(X-C1)<eps)
				printf("%.9f\n",V/R1);
			else
				puts("IMPOSSIBLE");
		}
		else
		{
			scanf("%lf%lf%lf%lf",&R1,&C1,&R2,&C2);
			printf("Case #%d: ",CaseNumber);
			if(abs(C1-C2)<eps)
			{
				if(abs(X-C1)<eps)
					printf("%.9f\n",V/(R1+R2));
				else
					puts("IMPOSSIBLE");
			}
			else
			{
				if(abs(X-C1)<eps)
					printf("%.9f\n",V/R1);
				else if(abs(X-C2)<eps)
					printf("%.9f\n",V/R2);
				else if((C1<X+eps && C2<X+eps)||(C1>X-eps && C2>X-eps))
					puts("IMPOSSIBLE");
				else
				{
					if(C1>C2)
					{
						swap(C1,C2);
						swap(R1,R2);
					}
					double a,b;
					b=(V*(X-C1))/(C2-C1);
					a=V-b;
					printf("%.9f\n",max(a/R1,b/R2));
				}
			}
		}
	}
	return 0;
}
