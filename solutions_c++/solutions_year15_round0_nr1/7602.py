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

int main()
{
	int t,cas=1;
	scan(t);
	fl(cas,1,t+1)
	{
		int smax,i;
		scan(smax);
		string s;
		cin>>s;
		int standing=0,ans=0;
		fl(i,0,smax+1)
		{
			if(i==0)
				standing = s[i]-'0';
			else
			{	
				int num = s[i]-'0';
				if(num>0)
				{
					if(standing>=i)
						standing+=num;
					else
					{
						ans+=(i-standing);
						standing = i+num;
					}
				}
			}
		}
		printf("Case #%d: ",cas);
		print(ans);
	}
	return 0;
}
