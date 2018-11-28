#include <bits/stdc++.h>
using namespace std;
 
typedef unsigned long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<iii> viii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;
//typedef vector<bool> vb;
typedef vector<string> vstr;
#define IOS std::ios_base::sync_with_stdio(false)
#define EPS 1e-07
#define PI (2*acos(0.0))
//struct point { double x, y; };
//struct line { double a, b, c; }; // ax + by + c = 0 
//funciones
ll gcd(ll a, ll b) { return (b == 0) ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

double dabs(double a)
{
	return (a < 0) ? (a * -1) : a;
}

int dcomp (double a, double b) {
	if (a - b > EPS) return 1;// a > b
	else if (b - a > EPS) return -1; // a < b
	return 0; // a == b
}
char pal[1010];
char temp[3010];
char last[1010];
char t2[1010];
int n;
bool comp()
{
	int sz = n;
	//printf("%s \n", t2);
	bool isL = false;
	for(int i = 0; i < sz; i++)
	{
		if(t2[i] == last[i])
			continue;
		if(t2[i] > last[i])
			isL = true;
		else
			isL = false;
		break;
	}
	
	if(isL)
		for(int i = 0 ; i < sz; i++)
		{
			last[i] = t2[i];
		}
	//printf("%s  -  %d\n", t2, isL);
	return false;
}
int le = 1500;
int ri = 1501;

void rec(int pos, bool lef)
{
	if(pos == n)
	{
		//printf("entra %d %d  ", le , ri);
	
		for(int i = le+1; i <= ri-1; i++)
		{
			//printf("%c", temp[i]);
			t2[i-(le+1)] = temp[i];
		}
		//printf("\n");
		comp();
		
		return;
	}
	
	temp[le] = pal[pos];
	//printf("%c", pal[pos]);
	le--;
	rec(pos+1, true);
	le++;
	
	temp[ri] = pal[pos];
	ri++;
	rec(pos+1, false);
	ri--;
}


int main()
{
	
	
	int casos;
	scanf("%d", &casos);
	
	for(int cas = 0; cas < casos; cas++)
	{
		scanf("%s", pal);
		n = strlen(pal);
		memset(last, 0, sizeof last);
		for(int i = 0; i < n; i++)
			last[i] = pal[i];
		rec(0, 0);
		
		
		printf("Case #%d: %s\n", cas+1, last);
		
	}
	
	return 0;
}

