#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
typedef long long ll;
const ll MOD = 1000000007;

int dp[2000];
int t,i,j,tc,vv;
double c,f,x,ans,val[100010],speed,time,time1,time2;

int main()
{
	
	freopen("D:\\input.txt","r",stdin);
	freopen("D:\\output.txt","w",stdout);
	cin>>tc;
	for(t=1;t<=tc;t++){
		vv=0;
		speed=2.0;
		time=0.0;
		cin>>c>>f>>x;
		for(i=1;i<=100001;i++){
			val[vv]=(time+x/speed)/1.0000000;
			time+=c/speed;
			speed+=f;
			vv++;
		}
		sort(val,val+100001);
		cout<<"Case #"<<t<<": ";
		printf("%.7llf\n",val[0]);
	}
	return 0;
}
