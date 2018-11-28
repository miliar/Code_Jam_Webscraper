#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;


int main()
{
	int t;
	S(t);
	FORE(i,t)
	{
		double x,f,c,score=2.0,max,factor=0;
		cin >> c >> f >> x;
		max = x/score;
		double curr = 1000000.0;
		while(1)
		{
			factor += (c/score);
			curr = x/(score+f)+factor;	
			score += f;
			if(curr < max)
				max = curr;
			else break;
		}
		//cout<<"Case "<<i<<": "<<max<<endl;
		printf("Case #%d: %.7lf\n",i,max);
	}
}
