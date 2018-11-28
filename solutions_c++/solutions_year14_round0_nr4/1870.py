#include<iostream>
#include<algorithm>
#define rep(i,n) for (int i=0;i<n;i++)
#define For(i,a,b) for (int i=a;i<=b;i++)
using namespace std;
const int maxn=10000;
double a[maxn],b[maxn];
int T,n;
int ans1,ans2,caseNum;
int used[maxn];
void Analyse1()
{
	ans1=n;
	int k=0;
	rep(i,n)
	{
		while(k<n && a[i]>b[k]) k++;
		if (a[i]<b[k] && k<n) --ans1,++k;
	}
}
void Analyse2()
{
	ans2=0;
	int k=n-1;
	for(int i=n-1;i>=0;i--)
	{
		while (k>=0 && b[k]>a[i]) k--;
		if (a[i]>b[k] && k>=0) ++ans2,k--;
	}

}
int main(){
	//freopen("input.txt","r",stdin);
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		rep(i,n) scanf("%lf",&a[i]);
		rep(i,n) scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
//		rep(i,n) printf("%lf ",a[i]);printf("\n");
//		rep(i,n) printf("%lf ",b[i]);printf("\n");
		Analyse1();
		Analyse2();
		++caseNum;
		printf("Case #%d: %d %d\n",caseNum,ans2,ans1);
	}

	return 0;
}
