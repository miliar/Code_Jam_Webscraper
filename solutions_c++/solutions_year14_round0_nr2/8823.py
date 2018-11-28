#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

/*typedef long long int64;
typedef unsigned long long uint64;*/
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
const double pi=acos(-1.0);
const double eps=1e-11;
/*template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
template<class T> inline T sqr(T x){return x*x;}*/
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define LENGTH(A) ((int)A.length())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ll long long int
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%lld",&x)
#define pi(x) printf("%d",x)
#define nl printf("\n")
#define pl(x) printf("%lld",x)

int main()
{
	freopen("cjin2.txt","r",stdin);
	freopen("cjout2.txt","w",stdout);
	double curr=0.0,mark=2.0,C,F,X;
	int T;
	si(T);
	for(int t=1;t<=T;t++)
	{
		cin>>C>>F>>X;
		mark=2.0;
		curr=0.0;
		while(1)
		{
			double temp=C/mark;
			double time=X/mark;
			mark+=F;
			double temp_curr=X/mark;
			if(time>temp_curr+temp)
			{
				curr+=temp;
			}
			else
			{
				curr+=time;break;
			}
		}
		printf("Case #%d: %0.7lf\n",t,curr);
	}
}
