#include<cstdio>
#include<algorithm>
using namespace std;

#define N 101
int t,a,n;
int tab[N];
//bool vis[N];
int cnt()
{
	int min=0,max=n,tmp=0,count=0,now=0;
	while(count<n){
	//bool op=false;
	int i;
	for(i=count;i<n;i++)if(a>tab[i]){a+=tab[i];count++;}else break;
	tmp=n-count+min;
	if(tmp<max)max=tmp;
	min++;a=a<<1;a--;
	if(a==1||min>max)break;
	}
	return max;
}
int main()
{
	//FILE* fin=freopen("1.in","r",stdin);
	//FILE* fout=freopen("1.out","w",stdout);
	scanf("%d",&t);
	int cas;
	for(cas=1;cas<=t;cas++)
	{
		scanf("%d",&a);
		scanf("%d",&n);
		int i;
		for(i=0;i<n;i++)scanf("%d",tab+i);
		sort(tab,tab+n);
		//for(i=0;i<n;i++)vis[i]=false;
		int ret=cnt();
		printf("Case #%d: %d\n",cas,ret);
	}
	return 0;
}