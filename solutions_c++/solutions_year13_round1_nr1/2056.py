#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#define fr(i,a,b) for(int i=a;i<b;i++)
#define rep(i,b) fr(i,0,b)
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
double eps= 1e-7;

//double sum(ll q){ return double(q)*(q+1)*(q*2.0+1)/6.0; }

double r, t;
double tot(ll q){
	double t = (2.0*(q-1) + 1.0)*q;
	return (2.0*(q)*r + t);
}

int main(){
	int cas;
	scanf("%d",&cas);
	rep(u,cas){
		scanf("%lf %lf",&r,&t);
		ll l1=0,l2=1LL;
		while(tot(l2) < t+eps) l2*=2;
		double area = 0.0, rr=r;
		fr(i,1,4){
			area += ((rr+1)*(rr+1)-rr*rr);
			//printf(">>>%.3lf\n",area);
			rr+=2.0;
		}
		//printf(" %.6lf\n",tot(1));
		//printf(" %.6lf\n",tot(2));
		//printf(" %.6lf\n",tot(3));
		while(l1<l2-10){
			ll w= (l1+l2)/2LL;
			if(tot(w)<t+eps) l1 = w;
			else l2 = w; 
		}
		for(ll i=l2;i>=l1;i--){
			if(tot(i)<t+eps){
				printf("Case #%d: %lld\n",u+1,i);
				break;
			}
		}
	}	
	return 0;
}

