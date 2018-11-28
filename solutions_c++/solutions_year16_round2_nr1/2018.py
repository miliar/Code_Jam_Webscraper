/*
._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._
	ABHINANDAN AGARWAL
	MNNIT ALLAHABAD
	CSE
._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._._
*/
#include<bits/stdc++.h>
using namespace std;
#define pc putchar_unlocked
#define gc getchar_unlocked
typedef long long ll;
typedef unsigned long long llu;
#define mp make_pair
#define pb push_back
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define scstr(x) scanf("%s",x)
#define pd(x) printf("%d",x)
#define pstr(x) printf("%s",x)
#define newl() printf("\n")
#define fl(i,n) for (i=0;i<n;i++)
#define fle(i,n) for (i=1;i<=n;i++)
#define fla(i,a,n) for (i=a;i<n;i++)
#define mem(a,i) memset(a,i,sizeof(a))
#define fi first
#define se second
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > piii ;
#define wl(n) while (n--)
#define MOD 1000000007
//-------------
char s[100][100]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int main()
{
	int t;
	sc(t);
	int ass=1;
	wl(t)
	{
		int hs[26]={0};
		int i,j,l;
		char x[2010];
		int num[10]={0};
		scanf("%s",x);l=strlen(x);
		for (i=0;i<l;i++)
		{
			hs[x[i]-'A']++;
		}
		num[0]+=hs['Z'-'A'];
		int al=hs['Z'-'A'];
		for (i=0;i<strlen(s[0]);i++)
		{
			hs[s[0][i]-'A']-=al;
		}
		num[2]+=hs['W'-'A'];
		al=hs['W'-'A'];
		for (i=0;i<strlen(s[2]);i++)
		{
			hs[s[2][i]-'A']-=al;
		}
		
		

		num[6]+=hs['X'-'A'];
		al=hs['X'-'A'];
		for (i=0;i<strlen(s[6]);i++)
		{
			hs[s[6][i]-'A']-=al;
		}

		num[8]+=hs['G'-'A'];
		al=hs['G'-'A'];
		for (i=0;i<strlen(s[8]);i++)
		{
			hs[s[8][i]-'A']-=al;
		}
		num[4]+=hs['U'-'A'];
		al=hs['U'-'A'];
		for (i=0;i<strlen(s[4]);i++)
		{
			hs[s[4][i]-'A']-=al;
		}
		num[1]+=hs['O'-'A'];
		al=hs['O'-'A'];
		for (i=0;i<strlen(s[1]);i++)
		{
			hs[s[1][i]-'A']-=al;
		}
		num[3]+=hs['R'-'A'];
		al=hs['R'-'A'];
		for (i=0;i<strlen(s[3]);i++)
		{
			hs[s[3][i]-'A']-=al;
		}
		num[5]+=hs['F'-'A'];
		al=hs['F'-'A'];
		for (i=0;i<strlen(s[5]);i++)
		{
			hs[s[5][i]-'A']-=al;
		}
		num[7]+=hs['S'-'A'];
		al=hs['S'-'A'];
		for (i=0;i<strlen(s[7]);i++)
		{
			hs[s[7][i]-'A']-=al;
		}
		num[9]=hs['I'-'A'];
		printf("Case #%d: ",ass);
		for (i=0;i<10;i++)
		{
			if (num[i]>0)
			{
				for (j=0;j<num[i];j++)
					printf("%d",i);
			}
		}
		/*for (i=0;i<26;i++)
			printf("%c:%d ",i+'A',num[i]);*/
		printf("\n");
		ass++;

	}		

	return 0;

}