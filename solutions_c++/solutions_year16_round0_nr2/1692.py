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
typedef unsigned long long ll;
typedef pair<int, int> pii;
string st;

bool check()
{
	Rep(i, st.size()) if(st[i] == '-') return 0;
	return 1;
}

void doit(int lst)
{
	lst++;
	string tmp;
	Rep(i, lst) if(st[i] == '-') tmp += '+';
	else tmp += '-';
	reverse(ALL(tmp));
	Rep(i, lst) st[i] = tmp[i];
}

int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc , cas = 1;
	cin>>tc;
	while(tc--)
	{
		PF("Case #%d: ", cas ++);
		cin>>st;
		int ans = 0;
		while(!check())
		{
			int lst_neg;
			for(int i = st.size() - 1; i >= 0; i--)
			{
				if(st[i] == '-')
				{
					lst_neg = i;
					break;
				}
			}
			int lst_pos = -1;
			Rep(i, st.size()) if(st[i] == '-') break;
			else lst_pos = i;

			if(lst_pos != -1)
			{
				doit(lst_pos);
				ans++;
			}
			doit(lst_neg);
			ans++;
		}
		cout<<ans<<endl;
	}
	return 0;
}