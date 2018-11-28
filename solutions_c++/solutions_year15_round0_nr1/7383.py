#include<bits/stdc++.h>
#define fr(i,m,n) for(i=m;i<n;i++)
#define ifr(i,m,n) for(i=m;i>n;i--)
#define ll long long
#define sc scanf
#define pf printf
#define var(x) x i=0,j=0,k=0,tmp1=0,tmp2=0,tmp3=0,tmp=0,tmp4=0,tmp5=0,flag=0,T=0,N=0,Q=0
#define pb push_back
#define vi vector<int>
#define vii vector<pair<int,int> >
#define vl vector<ll>
#define vll vector<pair<ll,ll> >
using namespace std;

int main() {
	var(int);
	char ch;
	sc("%d",&T);
	fr(i,1,T+1) {
		sc("%d ",&tmp);
		vi vec,sum;
		fr(j,0,tmp+1) {
			sc("%c",&ch);
			vec.pb(ch-'0');
			if(j==0)
				sum.pb(vec[j]);
			else
				sum.pb(sum[j-1]+vec[j]);
		}
		tmp5=0;
		fr(j,0,tmp) {
			if((sum[j]+tmp5)<j+1 && vec[j+1]!=0) {
				tmp5+=(j+1-sum[j]-tmp5);

			}
		}
		pf("Case #%d: %d\n",i,tmp5);
	}
	return 0;
}
