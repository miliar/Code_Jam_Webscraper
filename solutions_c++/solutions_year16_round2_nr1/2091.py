#include <bits/stdc++.h>
using namespace std;

const int MAXL=2005,SIGMA=26;
const char bet[10][10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

char s[MAXL];
int cnt[10],cnt2[SIGMA];

inline void cl(int k)
{
	int l=strlen(bet[k]);
	for (int i=0;i<l;i++) cnt2[bet[k][i]-'A']-=cnt[k];
}

inline void solve()
{
	scanf("%s",s);
	memset(cnt,0,sizeof(cnt));
	memset(cnt2,0,sizeof(cnt2));
	int l=strlen(s);
	for (int i=0;i<l;i++) cnt2[s[i]-'A']++;
	cnt[0]=cnt2['Z'-'A'];
	cl(0);
	cnt[2]=cnt2['T'-'A']-cnt2['H'-'A'];
	cl(2);
	cnt[8]=cnt2['G'-'A'];
	cl(8);
	cnt[3]=cnt2['T'-'A'];
	cl(3);
	cnt[4]=cnt2['R'-'A'];
	cl(4);
	cnt[1]=cnt2['O'-'A'];
	cl(1);
	cnt[6]=cnt2['X'-'A'];
	cl(6);
	cnt[5]=cnt2['F'-'A'];
	cl(5);
	cnt[7]=cnt2['S'-'A'];
	cl(7);
	cnt[9]=cnt2['E'-'A'];
	for (int i=0;i<=9;i++) while (cnt[i]--) printf("%d",i);
	puts("");
}

int main()
{
	freopen("read.txt","r",stdin);
	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
