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

string s;
vector<string> v;

void foo(int x)
{
	if(x==15)
	{
		s+='1';
		v.PB(s);
		s.pop_back();
		return;
	}

	s+='0';
	foo(x+1);
	s.pop_back();

	s+='1';
	foo(x+1);
	s.pop_back();	
}

ll prime(ll x)
{
	ll i;
	for(i=2;i*i<=x;i++)
	{
		if(x%i==0)
			return i;
	}

	return 0;
}

int main()
{
	s="1";
	foo(1);
	//cout<<v.size()<<endl;

	
	ll i,b,num,j,chk,cnt=0;
	bool flag;

	vector<string> ans;
	vector<ll> res[500];
	vector<ll> divs;
	//cout<<prime(150)<<" "<<prime(101)<<endl;
	
	fl(i,0,v.size())
	{
		if(v[i][0])
		num = 0;
		flag = 0;
		divs.clear();
		fl(b,2,11)
		{
			num = 0;
			fl(j,0,v[i].size())
			{
				if(v[i][j]=='0')
					num = num*b;
				else
					num = num*b + 1;
			}

			chk = prime(num);

			if(!chk)
			{
				flag = 1;
				break;
			}
			else
				divs.PB(chk);
		}

		if(!flag)
		{	
			ans.PB(v[i]);
			//cout<<v[i]<<endl;
			res[cnt++] = divs;
		}

		if(ans.size() == 500)
			break;
	}

	//cout<<"Done\n";

	
	ll n,t;
	
	printf("Case #1:\n");

	fl(i,0,500)
	{
		cout<<ans[i]<<ans[i]<<" ";
		fl(b,0,9)
			cout<<res[i][b]<<" ";
		nline;
	}
	

	return 0;
}
