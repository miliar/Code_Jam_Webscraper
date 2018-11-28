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

ll iseq(double a, double b)
{
	ll ret = (fabs(a - b) < 0.00001); 
    return ret;
}


int main()
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	ll t=rl(),caseno=0,n,i,j,k,s,m;
	double v,x,ar,ax,br,bx,v1,v2,tim;
	while(t--)
	{
		caseno++;
		n=rl();
		//scanf("%lf %lf",&v,&x);
		cin>>v>>x;
		if(n==1)
		{
			cin>>ar>>ax;
			if( !iseq(x,ax) )
			{
				//cout<<"here"<<endl;
				tim=-1;
			}
			else
				tim = (v*1.0)/(ar*1.0);
		}
		else
		{
			cin>>ar>>ax>>br>>bx;
			if(!iseq(ax,bx))
			{
				if((ax-x)>0.00000 && (bx-x)>0.0000) // if both have greater temperature its impossible
					tim=-1;
				else
				{
					v2 = ( (v*(x-ax)*1.00000)/((bx-ax)*1.00000));
					v1 = v-v2;
					tim = ( (v2*1.000000)/ (br*1.00000));
					//cout<<setprecision(6)<<fixed<<"v2="<<v2<<"v1="<<v1<<"tim="<<tim<<endl;
					double t2 = ((v1*1.00000)/(ar*1.00000));
					if(t2 > tim)
						tim = t2;
					if(v1<0.00000 || v2 < 0.00000)
					    tim = -1;
				}
			}
			else
			{
				if(!iseq(ax,x))
					tim=-1;
				else
				{
					ar=ar+br; // as all temp are equal... add the rates
					tim = (v*1.0)/(ar*1.0);
				}
			}

		}

		if(tim==-1)
			cout<<"Case #"<<caseno<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<caseno<<": "<<setprecision(6)<<fixed<<tim<<endl;
	}
	return 0;
}