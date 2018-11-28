#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
using namespace std;

#define ll long long
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define mod 1000000007

double c,f,x,v,ta,tb;
int t;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>t;
	for (int ca=1;ca<=t;ca++){
		cin>>c>>f>>x;
		v=2.00;
		double ans=0.00;
		while (1){
			ta=x/v;
			tb=(c/v)+(x/(v+f));
			if (ta>tb){
				ans+=(c/v);
				v+=f;
			}
			else{
				ans+=ta;
				break;
				}
		}
		printf("Case #%d: %.7lf\n",ca,ans); 
	}
}
