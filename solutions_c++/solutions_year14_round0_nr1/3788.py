#include <bits/stdc++.h>
#define fi "A.INP"
#define fo "A.OUT"
#define nmax
#define INF
using namespace std;
typedef map<int,int> MII;
//VARIABLES
int test,ans,res,a[2][10][10];
MII my_map;
//PROTOTYPES
void Process();

//MAIN
int main()
{
	int tc;
	freopen(fi,"r",stdin);
	freopen(fo,"w",stdout);
	scanf("%d",&tc);
	while (tc--) Process();
	return 0;
}

//FUNCTIONS
void Process()
{
	for (int k=0;k<=1;++k)
	{
		scanf("%d",&a[k][0][0]);
		for (int i=1;i<=4;++i)
		for (int j=1;j<=4;++j)
		scanf("%d",&a[k][i][j]);
	}
	my_map.clear();
	for (int j=1;j<=4;++j) ++my_map[a[0][a[0][0][0]][j]];
	for (int j=1;j<=4;++j) ++my_map[a[1][a[1][0][0]][j]];
	res=ans=0;
	for (MII::iterator it=my_map.begin();it!=my_map.end();++it)
	if (it->second==2)
	{
		++res;
		ans=it->first;
	}
	printf("Case #%d: ",++test);
	if (res==1) printf("%d\n",ans); else
	if (res==0) printf("Volunteer cheated!\n"); else
	printf("Bad magician!\n");
}
