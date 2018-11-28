#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <map>
#include <ctime>
#include <cmath>
using namespace std;
typedef long long LL;
LL fq[] ={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,
121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,
12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,
1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,
1232346432321,1234567654321,4000008000004,4004009004004,100000020000001,100220141022001,
102012040210201,102234363432201,121000242000121,121242363242121,123212464212321,123456787654321,
400000080000004,10000000200000001,10002000300020001,10004000600040001,10020210401202001,10022212521222001,
10024214841242001,10201020402010201,10203040504030201,10205060806050201,10221432623412201,10223454745432201,
12100002420000121,12102202520220121,12104402820440121,12122232623222121,12124434743442121,12321024642012321,
12323244744232321,12343456865434321,12345678987654321,40000000800000004,40004000900040004,1000000002000000001,
1000220014100220001,1002003004003002001,1002223236323222001,1020100204020010201,1020322416142230201,1022123226223212201,
1022345658565432201,1210000024200000121,1210242036302420121,1212203226223022121,1212445458545442121,1232100246420012321,
1232344458544432321,1234323468643234321,4000000008000000004
};
/*
vector<LL> fq;
LL p[8];
LL bit[20];
int check(LL num)
{
	LL tmp = num*num;
	int cntb=0;
	while (tmp)
	{
		bit[cntb++] = tmp%10LL;
		tmp /= 10LL;
	}
	for (int i=0 ; i<cntb ; i++ )
	if (bit[i] != bit[cntb-i-1]) return 0;
	return 1;
}
LL rev(LL num)
{
	int cntb=0;
	LL tmp = num;
	while (tmp)
	{
		bit[cntb++] = tmp%10LL;
		tmp /= 10LL;
	}
	LL res=0;
	for (int i=0 ; i<cntb ; i++ ) res += p[cntb-1-i] * bit[i];
	return res;
}
void initfq()
{
	int i;
	LL j,k;
	for ( i=1,p[0]=1 ; i<=7 ; i++ ) p[i] = p[i-1] * 10LL;

	fq.push_back(1);
	fq.push_back(4);
	fq.push_back(9);

	for ( i=2 ; i<=14 ; i++ )
	{
		int len = i/2;
		if (i%2)
		{
			for ( j=0 ; j<=9 ;j++ )
			{
				for ( k=p[len-1] ; k<p[len] ; k++ )
				{
					LL num = k*p[len+1] + j*p[len] + rev(k);
					if (check(num))
					{
						fq.push_back(num*num);
					}
				}
			}
		}
		else
		{
			for ( k=p[len-1] ; k<p[len] ; k++ )
			{
				LL num = k*p[len] + rev(k);
				if (check(num))
				{
					fq.push_back(num*num);
				}
			}
		}
	}
	sort(fq.begin(),fq.end());
	for ( i=0 ; i<fq.size() ; i++ ) printf("%lld,",fq[i]);
	printf("\n");
}
*/
LL getAns(LL pos)
{
	int l=0,r=90,mid;
	while (l<r)
	{
		mid = (l+r)>>1;
		if (fq[mid] > pos) r=mid-1;
		else	l=mid;
		if (l+1 >= r)
		{
			if (fq[r] <= pos) return r;
			if (fq[l] <= pos) return l;
			return -1;
		}
	}
	return -1;
}
int main()
{
//	freopen("lst","w",stdout);
//	initfq();
	freopen("test","r",stdin);
	freopen("out.out","w",stdout);
	LL l,r,ansl,ansr;
	int cas,tt=0;
	scanf("%d",&cas);
	while (cas--)
	{
		printf("Case #%d: ",++tt);
		cin>>l>>r;
		ansl = getAns(l-1) + 1;
		ansr = getAns(r) + 1;
		cout<<ansr-ansl<<endl;
	}

	return 0;
}
