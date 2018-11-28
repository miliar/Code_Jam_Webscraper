#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
typedef pair<long long,long long> pll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define ll long long
int GCD(int a, int b)
{
    return b? GCD(b,a%b) : a;
}
bool chk(string first, string second)
{
    string t1 = first + second;
    string t2 = second + first;
    return t1 < t2;
}
struct sort_pred
{
    bool operator()(const pair<int,int> &left, const pair<int,int> &right)
    {
        return left.second < right.second;
    }
};
long long POW(long long Base, long long Exp)
{
    long long y,ret=1;
    y=Base;
    while(Exp)
    {
        if(Exp&1)
            ret=(ret*y)%MOD;
        y = (y*y)%MOD;
        Exp/=2;
    }
    return ret%MOD;
}
vi A,B,Mark;
stack <char> Brkt;
vector<char> Aao;
void fun(int l, string str)
{
	string lwr="";
	for(int j=0; j<l; j++)
	{
		lwr = lwr + "0";
	}

	string upr="";

	for(int j=0; j<l-4; j++)
	{
		upr = upr + "1";
	}
	upr = upr + "3098";

	if(str>=lwr && str<=upr)
	{
		str = "1" + str;
	}
	cout<<str<<endl;
}

string str,str1;
int mark[26];
int main()
{
    int t;
    cin>>t;
    for(int tc=1; tc<=t; tc++)
    {
    	cin>>str;

    	int len=str.length();
    	memset(mark,0,sizeof mark);
    	int i,tmp;

    	for(i=0; i<len; i++)
    	{
    		mark[str[i]-'A']++;
    	}

    	if(mark['Z'-'A'])
        {
           int ct=mark['Z'-'A'];
           for(int i=0;i<ct;i++)
                        A.pb(0);
           mark['E'-'A']-=ct;
           mark['R'-'A']-=ct;
           mark['O'-'A']-=ct;
           mark['Z'-'A']-=ct;
        }
        if(mark['W'-'A'])
        {
           int ct=mark['W'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(2);
           mark['T'-'A']-=ct;
           mark['W'-'A']-=ct;
           mark['O'-'A']-=ct;
        }
        if(mark['U'-'A'])
        {
           int ct=mark['U'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(4);
           mark['F'-'A']-=ct;
           mark['O'-'A']-=ct;
           mark['U'-'A']-=ct;
           mark['R'-'A']-=ct;
        }
        if(mark['X'-'A'])
        {
           int ct=mark['X'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(6);
           mark['S'-'A']-=ct;
           mark['I'-'A']-=ct;
           mark['X'-'A']-=ct;
        }
        if(mark['G'-'A'])
        {
           int ct=mark['G'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(8);
           mark['E'-'A']-=ct;
           mark['I'-'A']-=ct;
           mark['G'-'A']-=ct;
           mark['H'-'A']-=ct;
           mark['T'-'A']-=ct;
        }
        if(mark['F'-'A'])
        {
           int ct=mark['F'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(5);
           mark['F'-'A']-=ct;
           mark['I'-'A']-=ct;
           mark['V'-'A']-=ct;
           mark['E'-'A']-=ct;
        }
        if(mark['V'-'A'])
        {
           int ct=mark['V'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(7);
           mark['S'-'A']-=ct;
           mark['E'-'A']-=ct;
           mark['V'-'A']-=ct;
           mark['E'-'A']-=ct;
           mark['N'-'A']-=ct;
        }
        if(mark['I'-'A'])
        {
           int ct=mark['I'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(9);
           mark['N'-'A']-=ct;
           mark['I'-'A']-=ct;
           mark['N'-'A']-=ct;
           mark['E'-'A']-=ct;
        }
        if(mark['O'-'A'])
        {
           int ct=mark['O'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(1);
           mark['O'-'A']-=ct;
           mark['N'-'A']-=ct;
           mark['E'-'A']-=ct;
        }
        if(mark['H'-'A'])
        {
           int ct=mark['H'-'A'];
           for(int i=0;i<ct;i++)
            A.pb(3);
           mark['T'-'A']-=ct;
           mark['H'-'A']-=ct;
           mark['R'-'A']-=ct;
           mark['E'-'A']-=ct;
           mark['E'-'A']-=ct;
        }
        sort(A.begin(),A.end());
    	printf("Case #%d: ",tc);
    	for(i=0; i<A.size(); i++)
    					cout<<A[i];
    	cout<<endl;
    	A.clear();
    }
    return 0;
}
