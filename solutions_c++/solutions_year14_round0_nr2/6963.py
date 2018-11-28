#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;t++){
		double c,f,x,cas=0,pro=2;
		cin>>c>>f>>x;
		double vys=x/2;
		while(1){
			vys=min(vys,cas+x/pro);
			if(cas+x/pro-0.000002>vys) break;
			cas+=c/pro;
			pro+=f;
		}
		printf("Case #%d: %.8f\n",t+1,vys);



	}
	return 0;
}
