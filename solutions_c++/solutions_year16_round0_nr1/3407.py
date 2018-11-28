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
	freopen("/home/chetan/Documents/inp.txt","r",stdin);
	freopen("/home/chetan/Documents/out1.txt","w",stdout);
	int t,tc;
	cin>>t;
	for(tc=1; tc<=t; tc++)
	{
		long long n,i,Ans,j;
		cin>>n;

		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",tc);
			continue;
		}

		int Count[10];
		for(i=0; i<10; i++)
		{
			Count[i]=0;
		}
		ll tmp1,not_found=0;
		for(i=1; i<101; i++)
		{
			tmp1 = i*n;
			not_found=0;
			//printf("tmp1: %lld\n",tmp1);
			while(tmp1)
			{
				ll tmp2 = tmp1%10;
				Count[tmp2]++;
				tmp1/=10;
			}
			//printf("tmp1: %lld\n",tmp1);

			for(j=0; j<10; j++)
			{
				if(!Count[j])
				{
					not_found=1;
					break;
				}
			}
			if(!not_found)
			{
				Ans = n*i;
				break;
			}
		}
		printf("Case #%d: %lld\n",tc,Ans);

	}
	return 0;
}
