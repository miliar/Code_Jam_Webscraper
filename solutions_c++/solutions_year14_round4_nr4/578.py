#include<stdio.h>
#include<set>
struct string
{
	char a[100];
	string(char *t, int r)
	{
		for(int i=0; i<=r; i++)
			a[i] = t[i];
		a[r+1] = 0;
	}
public:
	char operator[](int x) const{ return a[x]; }
};
bool operator<(const string &A, const string &B)
{
	int i;
	for(i=0; A[i] && B[i]; i++)
	{
		if(A[i] != B[i]) return A[i]<B[i];
	}
	return A[i]<B[i];
}
std::set<string> set[5];
char dat[10][20];
int go[10], n, m, ans = 0, cnt = 0;
void solve()
{
	int i, j;
	for(i=1; i<=m; i++)
	{
		set[i].clear();
	}
	for(j=0; j<n; j++)
	{
		for(int k=0; dat[j][k]; k++)
		{
			set[go[j]].insert(string(dat[j], k));
		}
	}
	int sum = 0;
	for(i=1; i<=m; i++)
	{
		sum += set[i].size()+1;
		if(set[i].size() == 0) return;
	}
	if(ans < sum)
	{
		ans = sum;
		cnt = 1;
	}
	else if(ans == sum)
	{
		cnt++;
	}
}
void bt(int x)
{
	if(x == n)
	{
		solve();
		return;
	}
	for(int i=1; i<=m; i++)
	{
		go[x] = i;
		bt(x+1);
	}
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int TT, T;
	scanf("%d", &TT);
	for(T=1; T<=TT; T++)
	{
		int i, j;
		ans = cnt = 0;
		scanf("%d%d", &n, &m);
		for(i=0; i<n; i++)scanf("%s", dat[i]);
		bt(0);
		printf("Case #%d: %d %d\n", T, ans, cnt);
	}
	return 0;
}