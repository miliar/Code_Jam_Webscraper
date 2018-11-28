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
//vi A,B,Mark;
stack <char> Brkt;
vector<char> Aao;
string str;
int main()
{
	int t,tc;
	cin>>t;
	for(tc=1; tc<=t; tc++)
	{
		cin>>str;
		int i,len;

		len = str.length();

		string Ans = "";
		Ans = Ans+str[0];
		char chk = str[0];
		for(i=1; i<len; i++)
		{
			if(str[i]>=Ans[0])
			{
				Ans = str[i] + Ans;
			}
			else
			{
				Ans = Ans + str[i];
			}
		}

		printf("Case #%d: ",tc);
		cout<<Ans<<endl;

	}
	return 0;
}
