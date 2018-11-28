#include <iostream>
#include<cstdio>
double buy[100010];
double rate[100100];
double C,F,X;
using namespace std;
int test(double r)
{
	//cout << r << endl;
	for(int i=0;i<=100000;i++)
	{
		if(buy[i]>r) break;
		//cout << buy[i]+X/rate[i] << endl;
		if(buy[i]+X/rate[i] <= r+1.0e-8) return 1;
	}
	return 0;
}
void solve(int t)
{
	double ans=-1.0;
	buy[0]=0.0;
	rate[0]=2.0;
	double p=0.0,q=50000.0,r;
	cin >> C >> F >> X;
	//cout << C <<F << X << endl;
	for(int i=1;i<=100000;i++)
	{
		rate[i]=rate[i-1]+F;
		buy[i]=buy[i-1]+C/rate[i-1];
	}
	//cout << buy[0] << " " << X << " " << rate[0] << endl;
	//for(int i=0;i<10;i++) cout << buy[i]+X/rate[i] << endl;
	//for(;;);
	//cout << buy[0] << " " << buy[1] << " " << buy[2] <<  endl;
	//for(;;);	//cout << "A" << endl;
	ans=50000.0;
	for(int i=0;i<=100000;i++)
	{
		ans=min(ans,buy[i]+X/rate[i]);
	}
	/*while(p<=q-1e-8)
	{
		r=(p+q)/2;
		if(test(r)==1)
		{
			ans=r;
			q=r;
		}
		else
		{
			p=r;
		}
	}*/
	cout << "Case #" << t << ": ";
	printf("%.8lf\n",ans);
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B.txt","w",stdout);
	int t;
	cin >> t;
	for(int i=0;i<t;i++) solve(i+1);
}