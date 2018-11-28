#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>
#include <deque>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);  
	for(int t=1; t<=T; t++)
	{		
		int N;
		double V,X;
		scanf("%d %lf %lf",&N,&V,&X);
		vector <double> R(N);
		vector <double> C(N);
		for(int i=0;i<N;i++){
			scanf("%lf  %lf",&R[i],&C[i]);
		}
		if(N==1 && X!=C[0]) printf("Case #%d: IMPOSSIBLE\n",t);
		else if(N==1) printf("Case #%d: %f\n",t,(V/(R[0])));
		else if(X<min(C[0],C[1]) || X>max(C[0],C[1])) printf("Case #%d: IMPOSSIBLE\n",t);
		else if(X==C[0] && X==C[1]) printf("Case #%d: %f\n",t,(V/(R[0]+R[1])));
		else{
			double det=C[0]-C[1];
			double V0=V*(X-C[1])/det;
			double V1=V*(C[0]-X)/det;
			double time=max(V0/R[0],V1/R[1]);
			printf("Case #%d: %f\n",t,time);
		}
	}
  return 0;
}
