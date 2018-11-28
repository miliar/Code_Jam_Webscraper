#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <complex>
#include <iterator>
#include <set>
#include <bitset>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>

using namespace std;
typedef vector<int> VI;
typedef long long LL;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<double> VD;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define PF push_front

int n;
int t,r,p,s,sr,sp,ss;
int ile[1000];
char ene[1000];
vector <string> wyn;
int M;
char tab[(1<<(13+1))];
string gen[(1<<(13+1))];
bool generuj(int x)
{
	if(x>=M)
	return true;
	
	if((tab[x]=='R') || (tab[x]=='S') || (tab[x]=='P'))
	{
		
		tab[2*x]=tab[x];
		tab[2*x+1]=ene[ tab[x] ];
		if((2*x)>=M){
		
		ile[tab[x]]--;
		ile[tab[2*x+1]]--;
		if(ile[tab[x]]<0)
		return false;
		if(ile[tab[2*x+1]]<0)
		return false;
		}
		
		
		return((generuj(2*x))&&(generuj(2*x+1)));
	}
	else
	{
		cerr<<"node " <<x<<"=="<<tab[x]<<" has no letter "<<endl;
		return false;
	}
	
}
void zeruj()
{
	ile['R']=sr;
	ile['P']=sp;
	ile['S']=ss;
	s=sp;
	r=sr;
	s=ss;
}
void dfs(int x)
{
	if(x<M)
	{
		dfs(2*x);
		dfs(2*x+1);
	
	
	if(gen[2*x]<gen[2*x+1])
	{
		gen[x]=(gen[2*x]+gen[2*x+1]);
	}
	else
	{
		gen[x]=(gen[2*x+1]+gen[2*x]);
	}
	}
	//cerr<<"gen["<<x<<"]=="<<gen[x]<<endl;
}
void dobuduj()
{
	string temp;
	temp.clear();
	FOR(i,M,2*M-1)
	{
		temp.clear();
		temp=temp+tab[i];
		gen[i]=temp;
	}
	dfs(1);
	wyn.PB(gen[1]);
}
int main()
{
	ene['R']='S';
	ene['S']='P';
	ene['P']='R';
	cin>>t;
	FOR(tt,1,t)
	{
		wyn.clear();
		
		cin>>n>>sr>>sp>>ss;
		
		
		 M=(1<<n);
		// cerr<<"M=="<<M<<endl;
		/*
		REP(i,(1<<(n+1)))
		tab[i]='a';
		*/
		zeruj();
		tab[1]='R';
		if(generuj(1))
		{
			dobuduj();
		}
		zeruj();
		tab[1]='S';
		if(generuj(1))
		{
			dobuduj();
		}
		zeruj();
		tab[1]='P';
		if(generuj(1))
		{
			dobuduj();
		}
	//	else
	//	{
	//		cout<<"nie wyszlo"<<endl;
	//	}
	//	cerr<<"#"<<gen[1]<<endl;
		printf("Case #%d: ",tt);
		if(SIZE(wyn)>0)
		{
			sort(ALL(wyn));
			//cout<<"#"<<wyn[0]<<"#"<<endl;
			cout<<wyn[0]<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		
	}

}






