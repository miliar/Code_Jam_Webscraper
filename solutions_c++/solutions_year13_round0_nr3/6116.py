#include <cstdio>
#include <set>

using namespace std;

int T,ans,A,B;
set <int> S;
int main()
{
	freopen("file.in","r",stdin);
	freopen("file.out","w",stdout);
	S.insert(1);
	S.insert(4);
	S.insert(9);
	S.insert(121);
	S.insert(484);
	S.insert(10201);
	S.insert(12321);
	S.insert(14641);
	S.insert(40804);
	S.insert(44944);
	S.insert(1002001);
	S.insert(1234321);
	S.insert(4008004);
	scanf("%d",&T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d%d",&A,&B);
		ans = 0;
		for(int i = A; i <= B; i++)
			if (S.find(i) != S.end())
				ans++;
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}