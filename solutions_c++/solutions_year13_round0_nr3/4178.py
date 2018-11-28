#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
using namespace std;
typedef long long ll;

ll makep(ll a);
ll atoll(char *s);

ll atoll(char *s)
{
	ll a=0;
	int l=strlen(s);
	for (int i=0; i<l; i++) {
		a *= 10LL;
		a += (ll)(s[i]-'0');
	}
	return a;
}

ll makep(ll a)
{
	ll len;
	char s[16];
	sprintf(s, "%lld", a);
	len = (ll)strlen(s);
	for (int i=0; i<=(len-1)/2; i++) {
		s[len-1-i] = s[i];
	}
	if (a != atoll(s)) {
		return atoll(s);
	}

	a += pow(10, len/2);
	sprintf(s, "%lld", a);
	len = (ll)strlen(s);

	for (int i=0; i<=(len-1)/2; i++) {
		s[len-1-i] = s[i];
	}
	a = atoll(s);
	return a;
}

int main()
{
	ll T,t,l,idx=0LL,d[123]={0LL};
	bool flag=0;
	char s[5]="";
	scanf("%lld",&T);
	t=T;
	for(ll i=1LL; i*i<=100000000000000LL; i=makep(i)){	// square
		sprintf(s,"%lld",i*i);
		l=(ll)strlen(s);
		flag=1;
		for(int j=0; 2*j<l; j++){
			if (s[j] != s[l-1-j]) {
				flag=0;
				break;
			}
		}
		if(flag){
			d[idx++]=i*i;
		}
	}

	while(T--){
		int cnt=0;
		ll a,b;
		scanf("%lld%lld",&a,&b);
		for(int i=0;i<idx;i++){
			if(a <= d[i] && d[i] <= b){
				cnt++;
			}
			else if (d[i] > b) {
				break;
			}
		}
		printf("Case #%lld: %d\n",t-T,cnt);
	}
	return 0;
}
