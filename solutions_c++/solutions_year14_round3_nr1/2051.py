//Rupinder :D

#include<iostream>
#include<sstream>
#include<cstring>
#include<stack>
#include<cmath>
#include<map>
#include<set>
#include<string.h>
#include<stdio.h>
#include<vector>
#include<math.h>
#include<string>
#include<algorithm>
#include<iterator>
#include<iomanip>
#include<limits.h>
#include<numeric>
using namespace std;

#define Pi 3.14159265358979323846264338327950288419716939937510582
typedef long long int lld;
typedef vector<int> vi;
typedef pair<int,int> pii;
#define sz size()
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define pf push_front
#define ppb pop_back
#define ff first
#define ss second
#define rep(i,n) for(i=0;i<n;i++)
#define all(a) a.begin(),a.end()
lld modpow(lld a,lld n,lld temp){lld res=1,y=a;while(n>0){if(n&1)res=(res*y)%temp;y=(y*y)%temp;n/=2;}return res%temp;}
lld gcd(lld a,lld b){if(a==0)return(b);else return(gcd(b%a,a));}
int split(double p)
{
	if(fabs(p)<.000001 || fabs(p-1)<.000001)
		return 0;
	if(p>0.5)
		return 1;
	else
		return 1 + max(split(2*p),split(0));
}
bool check(double p,int lev)
{
	if(fabs(p)<.000001 || fabs(p-1)<.000001)
		return true;
	if(lev>40)
		return false;
	if(p>.5)
		return check(1,lev+1)&&check(2*p-1,lev+1);
	else
		return check(0,lev+1)&&check(2*p,lev+1);
}
int main()
{
	double t,p,q;
	cin>>t;
	int te=t;
	while(t--)
	{
		scanf("%lf/%lf",&p,&q);
		printf("Case #%.0lf: ",te-t);
		if(check(p/q,0))
			printf("%d\n",split(p/q));
		else
			printf("impossible\n");
	}
	return 0;
}
