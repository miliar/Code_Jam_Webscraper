#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>

#define SZ 1000000
#define pb push_back
using namespace std;


typedef long long Long;

vector<Long> Mask(Long no)
{
	vector<Long> ret;
	do{
		ret.pb(no%2);
		no /= 2;
	}while(no);
	return ret;
}

Long NumberInBase(vector<Long> & b2 ,Long b)
{
	Long p = 1;
	Long ret = 0;
	for(Long i=0;i<b2.size();i++) {
		ret += b2[i]*p;
		p = p*b;
	}
	return ret;
}

Long NotPrime(Long no)
{
	for(Long i=2;i*i<=no;i++) {
		if(no%i==0) return i;
	}
	return 0;
}

Long JamValidate(Long no) {
	if(no<3) return 0;
	if(no%2==0) return 0;
	vector<Long> b2 = Mask(no);
	vector<Long> divi;
	for(Long i=2;i<=10;i++) {
		int value = NotPrime( NumberInBase (b2,i) ) ; 
		if( value) {
			divi.pb(value);
		}
		else return 0;
	}
	for(Long i=b2.size()-1;i>=0;i--) printf("%lld",b2[i]);
	for(int i=0;i<divi.size();i++) printf(" %lld",divi[i]);
	printf("\n");
	
	return 1;
}

void Init(int n, int limit)
{
	int cnt = 0;
	for(Long i=(1<<(n-1));i<(1<<n);i++) {
		if(JamValidate(i)) {
			cnt++;
			if(cnt>=limit) break;
		}
	}
}



int main()
{	
	freopen("C.txt","rt",stdin);
	freopen("Cout.txt","wt",stdout);
	int tst,cas,n,l;
	scanf("%d",&tst);
	for(cas=1;cas<=tst;cas++)
	{
		scanf("%d%d",&n,&l);
		printf("Case #%d:\n",cas);
		Init(n,l);
	}
	return 0;
}