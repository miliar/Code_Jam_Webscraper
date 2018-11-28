#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>

using namespace std;
vector<long long> v;

bool f(long long t){
	long long  a= t;
	long long  b= 0 ;
	while(t){
		b *= 10;
		b += t%10;
		t/=10;
	}
	return a == b;
}
int main(){
	v.clear();
	for(int i=1;i<=1e7;i++){
		long long  t = (long long)i*i;
		if(f(i) && f(t))	v.push_back(t);
	}
	int c;
	scanf("%d",&c);
	for(int i=1;i<=c;i++){
		int a, b;scanf("%d %d",&a,&b);
		int l = lower_bound(v.begin(),v.end(),a) - v.begin();
		int r = lower_bound(v.begin(),v.end(),b) - v.begin();
		if(v[r] != b)	r --;
		int ans = r - l + 1;
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
