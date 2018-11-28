#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;
typedef vector<string> vs;
typedef unsigned long long llu;
#define loop(i,a,b) for(i=a;i<b;i++)
#define iter(j,a) for(vector<int>::iterator j = a.begin();j!=a.end();j++)
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define gc getchar   

int ri() {
  char c = gc();
  while(c<'0' || c>'9') c = gc();
  int ret = 0;
  while(c>='0' && c<='9') {
	ret = 10 * ret + c - 48;
	c = gc();
  }
  return ret;
}

ll rl()
{
	char c = gc();
	while(c<'0' || c>'9') c = gc();
	ll ret = 0;
	while(c>='0' && c<='9') {
		ret = 10 * ret + c - 48;
		c = gc();
	}
	return ret;		
}

string rs()
{
	char c = gc();
	while(c=='\n' || c==' ') c=gc();
	string ret="";
	while(c!=10 && c!=' ')
	{
		ret+=c;
		c=gc();
	}
	return ret;
}

char rc()
{
	char c = gc();
	while(c=='\n' || c==' ') c=gc();
	return c;
}


int main()
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	ll t=rl(),i,j,n,m,caseno=0,ans,y,z,rate;
	ll a[1009];
	while(t--)
	{
		y=0;z=0;rate=-999999;
		caseno++;
		n=rl();
		loop(i,0,n)
		{
			a[i]=rl();
		}
		// for y
		m = a[0];
		loop(i,1,n)
		{
			if(m<=a[i])
				{;}
			else
				y+=m-a[i];
			//cout<<"yati"<<i<<"="<<y<<"m="<<m<<"a[i]="<<a[i]<<endl;
			j = a[i-1]-a[i];
			if(j>=0)
				if(rate<j)
					rate = j;
			m=a[i];
		}
		//cout<<"rate="<<rate<<endl;
		if (rate>0)
		{
			loop(i,1,n)
			{
				if(a[i-1]>rate)
					z+=rate;
				else
					z+=a[i-1];
				//cout<<"z="<<z<<endl;
			}
		}
		cout<<"Case #"<<caseno<<": "<<y<<" "<<z<<endl;
	}
	return 0;
}