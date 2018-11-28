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
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;
typedef pair<int, char> pci;
typedef vector<pci> vpci;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
//#define LL "%lld"
#define RLL(x) scanf(LL,&(x))

int mas[3];

string obr = "PRS";

char proc(char a, char b)
{
	if(a == 'P'  && b == 'R' || a == 'R' && b == 'P')
		return 'P';
	if(a == 'P'  && b == 'S' || a == 'S' && b == 'P')
		return 'S';
	if(a == 'S'  && b == 'R' || a == 'R' && b == 'S')
		return 'R';
	return 'D';
}

string getResult(string s)
{
	if(s.length() == 1)
		return s;
	string answ;
	for(int i = 0; i < s.length(); i += 2)
		answ.push_back(proc(s[i], s[i+1]));
	return getResult(answ);
}

string buildFromTwo(int *mas)
{
	if(mas[0]+mas[1]+mas[2] == 2)
	{
		string answ;
		for(int i = 0; i < 3; ++i)
			if(mas[i])
				answ += obr[i];
		return answ;
	}
	int masL[3];
	int masR[3];
	bool ok = true;
	for(int i = 0; i < 3; ++i)
	{
		int l = (mas[i] + ok) / 2;
		if(mas[i]&1)
			ok = false;
		masL[i] = l;
		masR[i] = mas[i] - l;
	}
	return buildFromTwo(masL) + buildFromTwo(masR);
}

void test_slow(int T)
{
	int n;
	scanf("%d",&n);
	for(int i=0; i<3; ++i)
		scanf("%d", mas+i);
	swap(mas[0], mas[1]);
	string s;
	for(int i=0; i<mas[0]; ++i)
		s.push_back('P');
	for(int i=0; i<mas[1]; ++i)
		s.push_back('R');
	for(int i=0; i<mas[2]; ++i)
		s.push_back('S');
	printf("Case #%d: ", T);
	do
	{
		string res = getResult(s);
		if(res[0] != 'D')
		{
			printf("%s\n", s.c_str());
			return;
		}
	}while (next_permutation(s.begin(), s.end()));
	printf("IMPOSSIBLE\n");
}

void test(int T)
{
	int n;
	scanf("%d",&n);
	for(int i=0; i<3; ++i)
		scanf("%d", mas+i);
	swap(mas[0], mas[1]);

	
	printf("Case #%d: ", T);
	if(abs(mas[0] - mas[1]) > 1 || 
	   abs(mas[0] - mas[2]) > 1 ||
	   abs(mas[1] - mas[2]) > 1)
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	string answ = buildFromTwo(mas);
	printf("%s\n", answ.c_str());
	
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

/*

*/