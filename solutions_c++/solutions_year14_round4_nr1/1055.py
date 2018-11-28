#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> v;
int main()
{
int N;
scanf("%d",&N);
for(int T=1;T<=N;T++)
{
	int n,m;
	scanf("%d%d",&n,&m);
	v.clear();
	for(int a=0;a<n;a++){ int t; scanf("%d",&t); v.push_back(t); }
	sort(v.begin(),v.end());
//for(int a=0;a<n;a++) printf("%d ",v[a]);
//printf("\n");
	int p=n;
	for(int a=0;a<p;a++)
	{
		while( p-a-1>=0 && v[a]+v[p-a-1]>m ) p--;
	}
	if( p%2==1 ) p--;
	printf("Case #%d: ",T);
	printf("%d",n-p+p/2);
done:;
	printf("\n");
}
	return 0;
}
