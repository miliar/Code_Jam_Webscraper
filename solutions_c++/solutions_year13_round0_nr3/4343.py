#include<cstdio>
#include<iostream>
#include<vector>
#include<utility>

using namespace std;
void input();
void solve();
int bins(long long x);
bool pali(long long x);
void solveSlow();


vector<pair<long long, long long> > queries;
long long Max;
vector<long long> all;

int main()
{
input();
solve();
return 0;
}

bool pali(long long x)
{
if(x < 10) return true;
vector<int> v;
int i;
while(x)
	{
	v.push_back(x % 10);
	x /= 10;
	}

for(i = 0; i < v.size() / 2; i++)
	if(v[i] != v[v.size()-1-i]) return false;
return true;
}



void solveSlow()
{

long long i;
int k;

//printf("solve slow\n");
for(i = 0; i*i <= Max; i++)
	if(pali(i) && pali(i*i))
		{
		all.push_back(i*i);
//		printf("%lld squared is %lld\n", i, i*i);
		}
for(i = 0; i < queries.size(); i++)
	{
	long long j;
	int ans = 0;
	for(j = queries[i].first; j <= queries[i].second; j++)
		for(k = 0; k < all.size(); k++)
			if(all[k] == j) { ans++; break; }
	printf("Case #%lld: %d\n", i+1, ans);
	}
}


void solve()
{
long long i;
//printf("solve fast\n");
for(i = 0; i*i <= Max; i++)
	if(pali(i) && pali(i*i))
		{
		all.push_back(i*i);
//		printf("%lld squared is %lld\n", i, i*i);
		}


for(i = 0; i < queries.size(); i++)
	{
//	printf("Query [%lld, %lld]\n", queries[i].first, queries[i].second);
	int x = bins(queries[i].first);
	int y = bins(queries[i].second);

	if(y == all.size() || all[y] != queries[i].second) y--;
//	printf("x = %d, y = %d, y-x+1=%d\n", x, y, y-x+1);
	printf("Case #%lld: %d\n", i+1, y-x+1);
	}
}


int bins(long long x)
{
int L, R, M;
L = 0;
R = all.size();
// invariant: 
// if i < L, then A[i] < A[L]
// if i >= R, then A[i] >= A[R]
while(R != L)
	{
	M = (L+R)/2;
	if(all[M] < x) L = M+1;
	else R = M;
	}
return L;
}

void input()
{
long long x, y;
int Q, i;
scanf("%d", &Q);
Max = 0;
for(i = 0; i < Q; i++)
	{
	cin >> x >> y;
	queries.push_back(make_pair(x, y));
	if(y > Max) Max = y;
	}
}


