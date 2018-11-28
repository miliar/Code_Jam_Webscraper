#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
//#define LL "%lld"
#define RLL(x) scanf(LL,&(x))

string control = "FGNORSUWXZ";

int coef[10][11];

string numbers[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void adstr(int I, int J, int cI, int cJ)
{
	for(int k = 0; k < 11; ++k)
		coef[I][k] = coef[I][k] * cI + coef[J][k] * cJ;
}

void output()
{
	
	for(int i = 0; i < 10; ++i)
	{
		for(int j = 0; j < 11; ++j)
		{
			cerr<<coef[i][j]<<" ";
		}
		cerr<<"\n";
	}
	cerr<<"\n";
}

void gauss()
{
	for(int i = 0; i < 10; ++i)
		for(int j = i + 1; j < 10; ++j)
		{
			if(coef[i][i] == 0)
				adstr(i, j, 1, 1);
			if(coef[j][i] != 0)
				adstr(j, i, coef[i][i], -coef[j][i]);
		}
	//output();
	for(int i = 9; i >= 0; --i)
	{
		coef[i][10] /= coef[i][i];
		for(int j = i - 1; j >= 0; --j)
			coef[j][10] -= coef[j][i] * coef[i][10];
	}
}

void buildMatr()
{
	cl(coef);
	for(int i = 0; i < 10; ++i)
		for(int j = 0; j < 10; ++j)
			for(int k = 0; k < numbers[j].size(); ++k)
				if(numbers[j][k] == control[i])
					++coef[i][j];
}

void test(int T)
{
	buildMatr();
	string s;
	cin>>s;
	for(int i = 0; i < s.size(); ++i)
		for(int j = 0; j < 10; ++j)
			if(control[j] == s[i])
				++coef[j][10];
	gauss();
	printf("Case #%d: ", T);
	for(int i = 0; i < 10; ++i)
	{
		if(coef[i][10] < 0)
			throw -1;
		for(int j = 0; j < coef[i][10]; ++j)
			printf("%d",i);
	}
	printf("\n");
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int n;
	cin>>n;
	for(int i = 0; i < n; ++i)
		test(i+1);
    return 0;
}