    //ALL HAIL MEGATRON

using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)
#define scan(n) scanf("%d", &n)
#define scans(s) scanf("%s", s)
#define scanc(c) scanf("%c", &c)
#define scanp(f) scanf("%f", &f)
#define scanll(l) scanf("%lld", &l)
#define scanllu(u) scanf("%llu", &u)
#define print(n) printf("%d\n", n)
#define prints(s) printf("%s\n", s)
#define printc(c) printf("%c\n", c)
#define printp(f) printf("%f\n", f)
#define printll(l) printf("%lld\n", l)
#define printllu(u) printf("%llu\n", u)
#define nline printf("\n")
#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int
#define PB push_back

int has[26], cnt[10];

int main()
{
	int t,T;
	scan(t);
	fl(T,0,t)
	{
		string s;
		cin>>s;
		memset(has,0,sizeof(has));
		memset(cnt,0,sizeof(cnt));
		int n = s.size(), i;

		fl(i,0,n)
			has[s[i]-'A']++;

		while(has[25])
		{
			has[25]--;	has['E'-'A']--;
			has['R'-'A']--;	has['O'-'A']--;
			cnt[0]++;
		}
		while(has['W'-'A'])
		{
			has['W'-'A']--;	has['T'-'A']--;	has['O'-'A']--;
			cnt[2]++;
		}
		while(has['X'-'A'])
		{
			has['S'-'A']--;	has['I'-'A']--;	has['X'-'A']--;
			cnt[6]++;
		}
		while(has['U'-'A'])
		{
			has['F'-'A']--;	has['O'-'A']--;	has['U'-'A']--;	has['R'-'A']--;
			cnt[4]++;

		}
		while(has['F'-'A'])
		{
			has['F'-'A']--;	has['I'-'A']--;	has['V'-'A']--;	has['E'-'A']--;
			cnt[5]++;
		}
		while(has['V'-'A'])
		{
			has['S'-'A']--;	has['E'-'A']--;	has['V'-'A']--;	has['E'-'A']--;	has['N'-'A']--;
			cnt[7]++;
		}
		while(has['G'-'A'])
		{
			has['E'-'A']--;	has['I'-'A']--;	has['G'-'A']--;	has['H'-'A']--;	has['T'-'A']--;
			cnt[8]++;
		}
		while(has['I'-'A'])
		{
			has['N'-'A']--;	has['I'-'A']--;	has['N'-'A']--;	has['E'-'A']--;
			cnt[9]++;
		}
		while(has['O'-'A'])
		{
			has['O'-'A']--;	has['N'-'A']--;	has['E'-'A']--;
			cnt[1]++;
		}
		while(has['T'-'A'])
		{
			has['T'-'A']--;	has['H'-'A']--;	has['R'-'A']--;	has['E'-'A']--;	has['E'-'A']--;
			cnt[3]++;
		}

		printf("Case #%d: ",T+1);

		fl(i,0,10)
		{
			while(cnt[i])
			{
				cout<<i;
				cnt[i]--;
			}
		}
		nline;
	}
	return 0;
}