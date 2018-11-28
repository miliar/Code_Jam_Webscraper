#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <algorithm>
#include <list>
#include <ctime>
#include <cstdio>
#include <stack>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <functional>
#include <sstream>
#include <map>
#include <set>

#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-8
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
typedef long long ll;
typedef pair<int, int> pii;
int n, k;
vector<double> in;
double p[MAXN];

double calc()
{
	vector<int> yes;
	Rep(i, k/2) yes.push_back(0);
	Rep(i, k/2) yes.push_back(1);
	double sum = 0;
	do
	{
		double cur = 1;
		Rep(i, k) if(yes[i] == 0) cur *= 1.- in[i];
		else cur *= in[i];
		sum += cur;
	} while (next_permutation(ALL(yes)));
	return sum;
}

int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cas= 1;
	cin>>tc;
	while (tc--)
	{
		cin>>n>>k;
		Rep(i, n) cin>>p[i];
		vector<int> choose;
		Rep(i, k) choose.push_back(1);
		Rep(i, n-k) choose.push_back(0);
		Sort(choose);
		double ans = 0;
		do
		{
			in.clear();
			Rep(i, n) if(choose[i] == 1) in.push_back(p[i]);
			double tmp = calc();
			ans = max(ans, tmp);
		} while (next_permutation(ALL(choose)));
		PF("Case #%d: %.8lf\n", cas++, ans);
	}
	return 0;
}