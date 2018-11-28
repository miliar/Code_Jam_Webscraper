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

int main()
{
	int t,i,j;
	double c,f,x;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		double res=INT_MAX,btime=0,ctime=0,rate=2;
		for(i=0;i<=x;i++) {
			if(btime+x/rate<=res)
				res=btime+x/rate;
			else
				break;
			btime+=c/rate;
			rate+=f;
		}
		printf("Case #%d: %.7lf\n",j,res);
	}
	return 0;
}
