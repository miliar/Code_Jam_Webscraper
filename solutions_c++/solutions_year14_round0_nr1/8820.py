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
	freopen("cjin1.txt","r",stdin);
	freopen("cjout1.txt","w",stdout);
	int T,ans1,ans2;
	si(T);
	for(int t=1;t<=T;t++)
	{
		si(ans1);
		int m1[4][4],m2[4][4];
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				si(m1[i][j]);
			}
		}
		si(ans2);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				si(m2[i][j]);
			}
		}
		int c=0,p=0;ans1--;
		ans2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(m1[ans1][i]==m2[ans2][j])c++,p=i;
			}
		}
		printf("Case #%d: ",t);
		if(c==1)
		{
			cout<<m1[ans1][p]<<endl;
		}
		else if(c>1)
		{
			cout<<"Bad magician!"<<endl;
		}
		else cout<<"Volunteer cheated!"<<endl;
	}
}
