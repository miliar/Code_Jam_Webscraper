#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<vector>
#include<map>
#include<cmath>
#include<iomanip>
//#pragma GCC optimize("O2") 
#define pb push_back
#define mp make_pair
#define IOS ios_base::sync_with_stdio(false)
using namespace std;
int n; 
const long double eps=1e-14;
void read(int &x)
{
	char ch=getchar();x=0;
	for(;ch<'0'||ch>'9';ch=getchar());
	for(;ch>='0' && ch<='9';ch=getchar())x=x*10+ch-'0';
}
struct node{
	 long double c,r;
}a[110];
long double v,x;
double l,r,mid;
bool cmp(node a,node b){
	return a.c>b.c;
}
bool judge(long double mid)
{
	long double s=0,s1=0,s2=0,p;
	for(int i=1;i<=n;i++){
		if(s+a[i].r*mid+eps<v){
			s+=a[i].r*mid;
			s1+=a[i].r*mid*a[i].c;
		}
		else{
			s1+=(v-s)*a[i].c;
			s=v+1;
			break;
		}
	}
	if(s+eps<v)return false;
	s=0;
	for(int i=n;i>=1;i--){
		if(s+a[i].r*mid+eps<v){
			s+=a[i].r*mid;
			s2+=a[i].r*mid*a[i].c;
		}
		else{
			s2+=(v-s)*a[i].c;
			s=v+1;
			
			break;
		}
	}
	if(s2<v*x+eps  && v*x<s1+eps) return true;
	else return false;
}
void task()
{
	cin>>n>>v>>x;
	for(int i=1;i<=n;i++){
		cin>>a[i].r>>a[i].c;
		a[i].r+=eps;
	}
	sort(a+1,a+n+1,cmp);
	l=0;r=1000010;
	while(abs(r-l)>1e-9){
		mid=(l+r)/2;
		if(judge(mid)) r=mid;
		else l=mid;
	}
	if(r<1000010)printf("%.9f\n",r);
	else puts("IMPOSSIBLE");

}
	
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
		for(int i=1;i<=T;i++){
		printf("Case #%d: ",i);
		task();
	}
}

