#include <cstdio>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstring>
#define int64 long long

using namespace std;

const int Maxn=50000;

int64 list[Maxn];
int tot,Test;

int Convert(int i)
{
	stringstream ss;
	ss << i;
	string s;
	ss >> s;
	string t=s;
	reverse(t.begin(),t.end());
	s=s+t;
	stringstream ss1;
	ss1 << s;
	int res;
	ss1 >> res;
	return res;
}

bool Check(int64 num)
{
	int a[30];
	int len=0;
	for (;num;num/=10) a[len++]=num % 10;
	for (int i=0,j=num-1;i<j;++i,--j)
		if (a[i]!=a[j]) return false;
	return true;
}

void Prepare()
{
	tot=0;
	list[++tot]=1;list[++tot]=4;list[++tot]=9;
	for (int i=1;;++i)
	{
		int64 j=Convert(i);
		if (j*j>100000000000000LL) break;
		int64 t=j*j;
		if (Check(t)) 
			list[++tot]=t;
	}
}

int Calc(int64 lim)
{
	if (lim<list[1]) return 0;
	int l=1,r=tot;
	for (;l<r;)
	{
		int mid=(l+r)/2+1;
		if (list[mid]<=lim) l=mid;
		else r=mid-1;
	}
	return l;
}

int main()
{
	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);
	
	Prepare();

	scanf("%d",&Test);
	for (int ii=1;ii<=Test;++ii)
	{
		int64 L,R;
		scanf("%I64d%I64d",&L,&R);
		
		printf("Case #%d: %d\n",ii,Calc(R)-Calc(L-1));
	}

	return 0;
}
