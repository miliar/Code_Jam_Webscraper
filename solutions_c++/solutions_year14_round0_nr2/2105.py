#pragma warning(disable:4996)
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
#define LL long long
#define mod 1000000007

int main(){
	//freopen("in.in","r",stdin);
	//freopen("out","w",stdout);
	int t,cas = 0;
	cin>>t;
	while(t--){
		double c,f,x;
		cin>>c>>f>>x;
		cout<<"Case #"<<++cas<<": ";
		double ans = x/2.0;
		if(c < x){
			double a,b,tmp;
			b = 0;
			for (int i = 1; ; i++)
			{
				a = x/(f*i + 2.0);
				b += c/(f*(i-1)+2.0);
				tmp = a+b;
				if(tmp < ans)ans = tmp;
				else break;
			}
		}
		printf("%.7lf\n",ans);
	}
	return 0;
}