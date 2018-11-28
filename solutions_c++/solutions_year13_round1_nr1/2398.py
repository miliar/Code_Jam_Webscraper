#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<deque>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;
long long compute(double r,double t)
{
	long long ans=(long long)((sqrt(4*r*r-4*r+8*t+1)-(2*r-1))/4);
	while(ans*ans*2+(2*r-1)*ans>t)
		ans--;
	return ans;
}
int main()
{
	FILE *fp1,*fp2;
	freopen_s(&fp1,"data.in","r",stdin);
	freopen_s(&fp2,"data.out","w",stdout);
	int T;
	double r,t;
	cin>>T;
	for(int time=1;time<=T;time++){
		scanf("%lf%lf",&r,&t);
		printf("Case #%d: %lld\n",time,compute(r,t));
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}