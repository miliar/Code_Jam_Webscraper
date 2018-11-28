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

string str;

void flip()
{
	int n = str.size(),i;
	fl(i,0,n)
	{
		if(str[i]=='-')
			str[i] = '+';
		else
			str[i] = '-';
	}
}

int main()
{
	int t,I;
	scan(t);
	fl(I,1,t+1)
	{
		string s;
		cin>>s;
		printf("Case #%d: ",I);
		ll n = s.size(),i,end=-1,beg,beg2;
		rev(i,n-1,0)
		{
			if(s[i]=='-')
			{
				end = i;
				break;
			}		
		}

		if(end==-1)
		{
			printf("0\n");
			continue;
		}

		ll ans=0;
		bool flag;

		while(1)
		{
			beg = n;
			//cout<<"h\n";
			str.clear();
			flag = 0;
			fl(i,0,n)
			{
				if(s[i]=='-')
				{
					beg = i-1;
					break;
				}
			}

			if(beg==n)
				break;

			if(beg!=-1)
				ans++;

			fl(i,beg+1,n)
			{
				if(s[i]=='+')
				{	
					beg = i-1;
					flag = 1;
					break;
				}
			}

			if(!flag)
			{	
				ans++;
				break;
			}
			
			str = s.substr(beg+1, end-beg);
			reverse(str.begin(), str.end());
			
			flip();
			ans++;
			s = str;
			n = s.size();
			if(!n)
				break;

			end = -1;
			rev(i,n-1,0)
			{
				if(s[i]=='-')
				{
					end = i;
					break;
				}		
			}

			if(end==-1)
				break;			
		}

		printll(ans);
	}
	return 0;
}
