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
typedef vector<pll> vpll;
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

pll get_state(ll no,ll k)
{
	 pll x;
	 if(no%k)
	 	x.f=no/k+1;
	 else
	 	x.f=no/k;
	 x.s=k-1;
	 return x;
}

int main()
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	ll t=rl(),d,i,j,l,temp,sum,ans,caseno=0;
	ll overhead[1011];
	vpll lstates;
	pll state,state2;
	while(t--)
	{
		ans=99999999;
		lstates.resize(0);
		caseno++;
		vl a;
		d=rl();
		loop(i,0,d)
			a.pb(rl());
		sort(a.begin(),a.end());
		loop(i,0,d)
		{
			// generates all active states.
			ll profit=1,k=1,temp_time=99999;
			loop(j,0,1009)
				overhead[j]=-1;
			while(profit)
			{
				state = get_state(a[i],k);
				//cout<<"state gen="<<state.f<<","<<state.s<<endl;	
				if(temp_time>=state.f+state.s) // check if the new state's time is good
				{
					temp_time=state.f+state.s;
					k++;
					if(k>a[i])
						profit=0;
				}
				else
					profit=0;
				if(!lstates.size())
					if(overhead[state.f]==-1)
						overhead[state.f]=state.s;
					else
						if(overhead[state.f]>state.s)
							overhead[state.f]=state.s;
				loop(j,0,lstates.size())
				{
					state2.f=max(state.f,lstates.at(j).f); // get max of highest of both
					state2.s=state.s+lstates.at(j).s;  // add overhead of both
					if(overhead[state2.f]==-1)
						overhead[state2.f]=state2.s;
					else
						if(overhead[state2.f]>state2.s)
							overhead[state2.f]=state2.s;
				}
			}
			lstates.resize(0);
			loop(j,0,1001)
				if(overhead[j]!=-1)
					lstates.pb(mp(j,overhead[j]));
		}
		loop(i,0,lstates.size())
		{
			//cout<<"counting,lstateat i="<<i<<"is "<<lstates.at(i).f<<","<<lstates.at(i).s<<endl;	
			if(ans>(lstates.at(i).f+lstates.at(i).s))
				ans=(lstates.at(i).f+lstates.at(i).s);
		}
		cout<<"Case #"<<caseno<<": "<<ans<<endl;
	}
	return 0;
}