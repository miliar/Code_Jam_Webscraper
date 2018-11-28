#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef vector<int> vi;
typedef vector<pair<int,int> >vpii;
typedef vector <LL> vl;
typedef vector <pair<LL,LL> > vpll;
typedef pair <int,int> pii;
typedef pair <LL,LL> pll;

#define forup(i,a,b) for(int i=(a); i<(b); ++i)
#define fordn(i,a,b) for(int i=(a); i>(b); --i)
#define rep(i,a) for(int i=0; i<(a); ++i)
#define gi(x) scanf("%d ",&x)
#define gll(x) scanf("%lld ",&x)
#define gd(x) scanf("%lf ",&x)
#define gs(x) scanf(" %s",x) 
#define fs first
#define sc second 
#define pb push_back
#define mp make_pair
void setup()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	cout.precision(15);
}

#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
            cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
            const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define endl '\n'
int cnt[10];
int alpha[27];
int main()
{
	//setup();
	int t;
	cin >> t;
	string s;
	for(int p=1;p<=t;p++)
	{
		memset(cnt,0,sizeof(cnt));
		memset(alpha,0,sizeof(alpha));
		cin >> s;
		for(int i=0;i<s.length();i++)
		{
			alpha[s[i]-'A']++;
		}
		//0
		cnt[0]=alpha['Z'-'A'];
		alpha['E'-'A']-=alpha['Z'-'A'];
		alpha['R'-'A']-=alpha['Z'-'A'];
		alpha['O'-'A']-=alpha['Z'-'A'];
		alpha['Z'-'A']=0;
		
		//2
		cnt[2]=alpha['W'-'A'];
		alpha['T'-'A']-=alpha['W'-'A'];
		alpha['O'-'A']-=alpha['W'-'A'];
		alpha['W'-'A']=0;

		//6
		cnt[6]=alpha['X'-'A'];
		alpha['S'-'A']-=alpha['X'-'A'];
		alpha['I'-'A']-=alpha['X'-'A'];
		alpha['X'-'A']=0;

		//8
		cnt[8]=alpha['G'-'A'];
		alpha['E'-'A']-=alpha['G'-'A'];
		alpha['I'-'A']-=alpha['G'-'A'];
		alpha['H'-'A']-=alpha['G'-'A'];
		alpha['T'-'A']-=alpha['G'-'A'];
		alpha['G'-'A']=0;

		//3
		cnt[3]=alpha['H'-'A'];
		alpha['T'-'A']-=alpha['H'-'A'];
		alpha['R'-'A']-=alpha['H'-'A'];
		alpha['E'-'A']-=alpha['H'-'A'];
		alpha['E'-'A']-=alpha['H'-'A'];
		alpha['H'-'A']=0;

		//4
		cnt[4]=alpha['R'-'A'];
		alpha['F'-'A']-=alpha['R'-'A'];
		alpha['O'-'A']-=alpha['R'-'A'];
		alpha['U'-'A']-=alpha['R'-'A'];
		alpha['R'-'A']=0;

		//5
		cnt[5]=alpha['F'-'A'];
		alpha['I'-'A']-=alpha['F'-'A'];
		alpha['V'-'A']-=alpha['F'-'A'];
		alpha['E'-'A']-=alpha['F'-'A'];
		alpha['F'-'A']=0;

		//7
		cnt[7]=alpha['V'-'A'];
		alpha['E'-'A']-=alpha['V'-'A'];
		alpha['S'-'A']-=alpha['V'-'A'];
		alpha['E'-'A']-=alpha['V'-'A'];
		alpha['N'-'A']-=alpha['V'-'A'];
		alpha['V'-'A']=0;

		//1
		cnt[1]=alpha['O'-'A'];
		alpha['N'-'A']-=alpha['O'-'A'];
		alpha['E'-'A']-=alpha['O'-'A'];
		alpha['O'-'A']=0;

		//9
		cnt[9]=alpha['I'-'A'];
		alpha['N'-'A']-=alpha['I'-'A'];
		alpha['N'-'A']-=alpha['I'-'A'];
		alpha['E'-'A']-=alpha['I'-'A'];
		alpha['I'-'A']=0;
		
		cout << "Case #" << p << ": ";
		for(int i=0;i<=9;i++)
		{
			while(cnt[i])
			{
				cout<<i;
				cnt[i]--;
			}
		}
		cout << endl;
	}	
	
	return 0;
}

