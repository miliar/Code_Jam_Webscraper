#include<iostream>
#include<iomanip>
using namespace std;

double ans;
double cost, extra, target;

void solve(double prefix, double rate)
{
	if(prefix >= ans)
		return;
	ans = min(ans, prefix + target/rate);
	solve(prefix+cost/rate, rate+extra);
}

int main()
{
	freopen("d:\\2.txt", "r", stdin);
	freopen("d:\\2-out.txt", "w", stdout);
	
	int T;
	cin>>T;
	for(int kase = 1; kase <= T; ++kase)
	{
		cin>>cost>>extra>>target;
		ans = target/2;
		solve(0, 2);
		cout<<"Case #"<<kase<<": ";
		cout<<fixed<<setprecision(7)<<ans<<endl;
	}
}
