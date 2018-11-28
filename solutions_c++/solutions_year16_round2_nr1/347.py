#include<bits/stdc++.h>
#include<cstdlib>   
#define sf(x) scanf("%d",&x)
#define pf(x) printf("%d ",x)
#define sf2(x,y) scanf("%d %d",&x,&y)
#define pf2(x,y) printf("%d %d ",x,y)
#define sf3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf3(x,y,z) printf("%d %d %d ",x,y,z)
#define sfc(c) scanf(" %c",&c)
#define pfc(c) printf("%c",c)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define INF 2000000000
#define ENDL puts("")


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef unsigned int uint;
typedef long double ld;



int cnt[256];
unordered_map<int, string> s;
int num[]={0,2,4,6,8,5,7,1,3,9};
char qwe[]={'Z','W','U','X','G','F','V','O','T','N'};


void rem(int k)
{
	string tmp=s[k];
	for(int i=0; i<tmp.size(); i++)
	{
		cnt[tmp[i]]--;
	}
}


int main()
{
    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);      
    /**/
	s[0]="ZERO";
	s[1]="ONE";
	s[2]="TWO";
	s[3]="THREE";
	s[4]="FOUR";
	s[5]="FIVE";
	s[6]="SIX";
	s[7]="SEVEN";
	s[8]="EIGHT";
	s[9]="NINE";
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	string s;
    	cin>>s;
    	memset(cnt,0,sizeof(cnt));
    	for(int i=0; i<s.size(); i++)
    	{
    		cnt[s[i]]++;
    	}
    	string res;
    	for(int i=0; i<10; i++)
    	{
    		while(cnt[qwe[i]]!=0)
    		{
    			rem(num[i]);
    			res.pb(num[i]+'0');
    		}
    	}
    	sort(res.begin(),res.end());
    	printf("Case #%d: %s\n",t,res.c_str());
    }
    
    
    
    return 0;
}











