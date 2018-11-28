#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
using namespace std;

int vis[11];
unsigned long long n;
unsigned long long maxx;
bool imposs = false;
bool e = false;
void f(int pos, unsigned long long num)
{
	if (imposs || e)return;
	if (pos == 10000)
	{
		imposs = true;
		return;
	}

	string s = to_string(pos*n);
	unsigned long long nextnum = num;
	for (int i = 0; i < s.size(); i++)
	{
		if (!vis[s[i] - '0'] && s[i]>='0' && s[i] <= '9')
		{
			nextnum++;
			vis[s[i] - '0']++;
		}
	}

	if (nextnum == 10)
	{
		maxx = pos*n;
		e = true;
		return;
	}

	f(pos + 1, nextnum);
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++)
	{
		scanf("%llu", &n);
		imposs = false;
		e = false;
		maxx = 0;
		memset(vis, 0, sizeof(vis));
		f(1, 0);
		printf("Case #%d: ", T);
		if (imposs) printf("INSOMNIA\n");
		else printf("%llu\n", maxx);
	}

}