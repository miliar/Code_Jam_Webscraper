#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
double c,f,x;
int T;

int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for (int t=0;t<T;t++){
		printf("Case #%d: ",t+1);
		cin>>c>>f>>x;
		double ans=x/2.0,tmp=0.0;
		for (int i=0;i<=100000;i++){
			//printf("%.10f\n",tmp+x/(i*f+2.0));
			if (ans>tmp+x/(i*f+2.0)) 
				ans=tmp+x/(i*f+2.0);
			tmp+=c/(i*f+2.0);	
		}
		printf("%.10f\n",ans);
	}
	return 0;
}