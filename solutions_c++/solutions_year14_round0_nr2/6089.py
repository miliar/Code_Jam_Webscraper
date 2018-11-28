#include <iostream>
#include <fstream>
using namespace std;

long double C,F,X;

int upBound(){
	int n = 0;
	long double ng = X/2,cur = 0;
	int up = 2*ng/C;
	while(cur<ng&&n<up){
		cur += C/(2+n*F);
		n++;
	}
	return n;
}

long double cal(int k){
	long double ret = 0;
	for(int i=0;i<k;i++)ret += C/(2+i*F);
	ret += X/(2+k*F);
	return ret;
}

int main(){
	ifstream cin("B-large (1).in");
	freopen("out","w",stdout);
	//ofstream cout("out");
	int nCase;
	cin>>nCase;
	for(int nc=1;nc<=nCase;nc++){
		cin>>C>>F>>X;
		int l = 0,m1,m2,r;
		r = upBound();
		long double lv = cal(l),rv = cal(r),v1,v2;
		while(r-l>2){
			m1 = (l*2+r)/3;
			m2 = (l+r*2)/3;
			v1 = cal(m1),v2 = cal(m2);
			if(v1<v2){
				r = m2;
				rv = v2;
			}else{
				l = m1;
				lv = v1;
			}
		}
		long double ans = min(min(lv,rv),cal(l+1));
		printf("Case #%d: %0.7f\n",nc,ans);
	}
	return 0;
}

