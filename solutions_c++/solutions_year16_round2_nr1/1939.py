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

string s;
int n,t,a,b,c;
int tab[30];
int lit;
int ile[10];
int main()
{
	cin>>t;
	FOR(tt,1,t)
	{
		printf("Case #%d: ",tt);
		cin>>s;
		lit=SIZE(s);
		REP(i,30)
		tab[i]=0;
		REP(i,10)
		ile[i]=0;
		
		REP(i,SIZE(s))
		{
			s[i]=tolower(s[i]);
			tab[s[i]-'a']++;
		}
		//0
		REP(i,tab['z'-'a'])
		{
			tab['e'-'a']--;
			tab['r'-'a']--;
			tab['o'-'a']--;
			lit-=4;
			printf("0");
		}
		tab['z'-'a']=0;
		//6
		REP(i,tab['x'-'a'])
		{
			tab['i'-'a']--;
			tab['s'-'a']--;
			lit-=3;
			ile[6]++;
			//printf("0");
		}
		tab['x'-'a']=0;
		
		//7
		REP(i,tab['s'-'a'])
		{
			tab['e'-'a']-=2;
			tab['v'-'a']--;
			tab['n'-'a']--;
			lit-=5;
			ile[7]++;
			//printf("0");
		}
		tab['s'-'a']=0;
		//5
		REP(i,tab['v'-'a'])
		{
			tab['f'-'a']--;
			tab['i'-'a']--;
			tab['e'-'a']--;
			lit-=4;
			ile[5]++;
			//printf("0");
		}
		tab['v'-'a']=0;
		//4
		REP(i,tab['f'-'a'])
		{
			tab['o'-'a']--;
			tab['u'-'a']--;
			tab['r'-'a']--;
			lit-=4;
			ile[4]++;
			//printf("0");
		}
		tab['f'-'a']=0;
		//2
		REP(i,tab['w'-'a'])
		{
			tab['t'-'a']--;
			tab['o'-'a']--;
			
			lit-=3;
			ile[2]++;
			//printf("0");
		}
		tab['w'-'a']=0;
		
		//1
		REP(i,tab['o'-'a'])
		{
			tab['n'-'a']--;
			tab['e'-'a']--;
			
			lit-=3;
			ile[1]++;
			//printf("0");
		}
		tab['o'-'a']=0;
		//3
		REP(i,tab['r'-'a'])
		{
			tab['t'-'a']--;
			tab['h'-'a']--;
			tab['e'-'a']-=2;
			
			lit-=5;
			ile[3]++;
			//printf("0");
		}
		tab['r'-'a']=0;
		//8
		REP(i,tab['h'-'a'])
		{
			tab['e'-'a']--;
			tab['i'-'a']--;
			tab['g'-'a']--;
			tab['t'-'a']--;
			
			lit-=5;
			ile[8]++;
			//printf("0");
		}
		tab['h'-'a']=0;
		//9
		REP(i,tab['i'-'a'])
		{
			tab['n'-'a']-=2;
			//tab['i'-'a']--;
			tab['e'-'a']--;
			//tab['t'-'a']--;
			
			lit-=4;
			ile[9]++;
			//printf("0");
		}
		tab['i'-'a']=0;
		FOR(i,0,((int)('z'-'a')))
		{
			if(tab[i]!=0)
			{
				cerr<<"case "<<tt<<" nierowne tab dla"<<i<<endl;
			}
		}
		if(lit!=0)
		{
			cerr<<"case "<<tt<<"nierowne litery"<<endl;
		}
		FOR(i,1,9)
		{
			REP(p,ile[i])
			{
				printf("%d",i);
			}
		}
		printf("\n");
	}

}






