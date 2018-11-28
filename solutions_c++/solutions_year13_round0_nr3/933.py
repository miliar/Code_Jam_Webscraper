#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long ll;
ll s[110];
void init(){
s[1] = 1LL;
s[2] = 4LL;
s[3] = 9LL;
s[4] = 121LL;
s[5] = 484LL;
s[6] = 10201LL;
s[7] = 12321LL;
s[8] = 14641LL;
s[9] = 40804LL;
s[10] = 44944LL;
s[11] = 1002001LL;
s[12] = 1234321LL;
s[13] = 4008004LL;
s[14] = 100020001LL;
s[15] = 102030201LL;
s[16] = 104060401LL;
s[17] = 121242121LL;
s[18] = 123454321LL;
s[19] = 125686521LL;
s[20] = 400080004LL;
s[21] = 404090404LL;
s[22] = 10000200001LL;
s[23] = 10221412201LL;
s[24] = 12102420121LL;
s[25] = 12345654321LL;
s[26] = 40000800004LL;
s[27] = 1000002000001LL;
s[28] = 1002003002001LL;
s[29] = 1004006004001LL;
s[30] = 1020304030201LL;
s[31] = 1022325232201LL;
s[32] = 1024348434201LL;
s[33] = 1210024200121LL;
s[34] = 1212225222121LL;
s[35] = 1214428244121LL;
s[36] = 1232346432321LL;
s[37] = 1234567654321LL;
s[38] = 4000008000004LL;
s[39] = 4004009004004LL;
s[40] = 100000020000001LL;
}
int main(){
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	init();
	for(int cas=1;cas<=T;cas++){
		ll a,b;
		scanf("%lld%lld",&a,&b);
		int  x=lower_bound(s+1,s+1+40,a)-s;
		int  y=lower_bound(s+1,s+1+40,b)-s;
		if(s[y]>b)y--;
		printf("Case #%d: %d\n",cas,y-x+1);
	}
	return 0;
}

