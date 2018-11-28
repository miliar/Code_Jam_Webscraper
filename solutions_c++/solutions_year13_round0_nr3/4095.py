/*
 Anton Gulikov
*/
#pragma comment(linker,"/STACK:300000000")
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <list>
#include <math.h>
#include <string>
#include <stdlib.h>

#define gcd(a,b) __gcd((a),(b))
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define foru(i,n) for (int i=0;i<(n);i++)
#define ford(i,n) for (int i=(n)-1;i>=0;i--)
#define forab(i,l,r) for (int i=(l);i<=(r);i++)
#define forabd(i,r,l) for (int i=(r);i>=(l);i--)
#define fillchar(a,b) memset((a),(b),sizeof((a)))
#define pb push_back
#define F first
#define S second
#define all(x) x.begin,x.end
#define pw2(x) (1ull<<(x))
#define mp make_pair

const long double eps=1e-20;
const long double pi=acos(-1.0);
const long long inf=1000*1000*1000*1000*1000*1000;
const long long base=1000*1000*1000+7;

using namespace std;

long long a[50];
int t;
long long le,ri,ans;

int main(){
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	scanf("%d",&t);
	a[0]=1;    
a[1]=4;
a[2]=9;
a[3]=121;
a[4]=484;
a[5]=10201;
a[6]=12321;
a[7]=14641;
a[8]=40804;
a[9]=44944;
a[10]=1002001;
a[11]=1234321;
a[12]=4008004;
a[13]=100020001;
a[14]=102030201;
a[15]=104060401;
a[16]=121242121;
a[17]=123454321;
a[18]=125686521;
a[19]=400080004;
a[20]=404090404;
a[21]=(long long)10000200001ll;
a[22]=(long long)10221412201ll;
a[23]=(long long)12102420121ll;
a[24]=(long long)12345654321ll;
a[25]=(long long)40000800004ll;
a[26]=(long long)1000002000001ll;
a[27]=(long long)1002003002001ll;
a[28]=(long long)1004006004001ll;
a[29]=(long long)1020304030201ll;
a[30]=(long long)1022325232201ll;
a[31]=(long long)1024348434201ll;
a[32]=(long long)1210024200121ll;
a[33]=(long long)1212225222121ll;
a[34]=(long long)1214428244121ll;
a[35]=(long long)1232346432321ll;
a[36]=(long long)1234567654321ll;
a[37]=(long long)4000008000004ll;
a[38]=(long long)4004009004004ll;
	forab(tt,1,t){
		printf("Case #%d: ",tt);
		ans=0;
		cin>>le>>ri;
		foru(i,39) if (a[i]>=le && a[i]<=ri) ans++;
		cout<<ans<<endl;
	}
	return 0;
}