#include<iostream>
#include<cmath>
using namespace std;
bool pl(long long x){
	char a[20];
	int nc=0;
	while(x>0)
	{a[nc++]=x%10;
	x/=10;
	}
	bool yes=1;
	for(int i=0,c=nc-1;i<nc;++i,--c)
		if(a[i]!=a[c]){
			yes=0;
			break;
		}
	return yes;
}
int main(){
	int t;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	for(int c=1;c<=t;++c){
		long long l, r;
		scanf("%lld%lld",&l,&r);
		long long i=sqrt(l);
		while(i*i<l)++i;
		int tot=0;
		for(;i*i<=r;++i){
			if(pl(i) && pl(i*i))++tot;
		}
		printf("Case #%d: %d\n",c,tot);
	}
	//system("pause");
}