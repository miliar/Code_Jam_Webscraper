#include <cstdio>
#include <algorithm>
#include <vector>
#include<iostream>
#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;
typedef double D; 
const int MAXN = 100005;
void solve()
{
	int n;
	vector<D>A,B;
	scanf("%d",&n);
	A.resize(n),B.resize(n);
	fru(i,n)scanf("%lf",&A[i]);
	fru(i,n)scanf("%lf",&B[i]);
	sort(A.begin(),A.end());
	sort(B.begin(),B.end());
	int pb=0;
	int wyn=0;
	fru(i,n)
		if(A[i]>B[pb]){wyn++;pb++;}
	printf("%d ",wyn);
	wyn=0;
	pb=0;
	fru(i,n)
	{
		while(pb<n && B[pb]<A[i])pb++;
		if(pb==n)break;
		wyn++;pb++;
	}
	printf("%d\n",n-wyn);
}
int main()
{
	int t;
	scanf("%d",&t);
	fru(i,t){printf("Case #%d: ",i+1);solve();}
    return 0;
}
