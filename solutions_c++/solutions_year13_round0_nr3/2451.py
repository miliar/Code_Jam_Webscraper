#include<cstdio>
#include<string>
#include<algorithm>
using namespace std;

int tot;

void calc(int v,int reduce){
	int tmp=v;
	if(reduce)tmp/=10;
	while(tmp){
		v=v*10+tmp%10;
		tmp/=10;
	}
	long long tt=1LL*v*v,mul=tt;
	string s="",vs="";
	for(;tt;tt/=10){
		int dig=tt%10;
		s+=dig+'0';
		vs=char(dig+'0')+vs;
	}
	if(s==vs){
		printf("%I64dLL,",mul);
		tot++;
	}
}

long long v[48]={1LL,121LL,4LL,484LL,9LL,10201LL,1002001LL,12321LL,1234321LL,14641LL,40804LL,4008004LL,44944LL,100020001LL,10000200001LL,102030201LL,10221412201LL,104060401LL,121242121LL,12102420121LL,123454321LL,12345654321LL,125686521LL,400080004LL,40000800004LL,404090404LL,1000002000001LL,100000020000001LL,1002003002001LL,100220141022001LL,1004006004001LL,1020304030201LL,102012040210201LL,1022325232201LL,102234363432201LL,1024348434201LL,1210024200121LL,121000242000121LL,1212225222121LL,121242363242121LL,1214428244121LL,1232346432321LL,123212464212321LL,1234567654321LL,123456787654321LL,4000008000004LL,400000080000004LL,4004009004004LL,};

int T;
long long a,b;

int main(){
	/*tot=0;
	for(int i=1;i<9999;i++){
		calc(i,1);
		calc(i,0);
	}
	printf("\n%d\n",tot);*/
	sort(v,v+48);
	scanf("%d",&T);
	for(int _=1;_<=T;_++){
		scanf("%I64d%I64d",&a,&b);
		int ans=0;
		for(int i=0;i<48;i++)
			if(v[i]>=a&&v[i]<=b)
				ans++;
		printf("Case #%d: %d\n",_,ans);
	}

	return 0;
}