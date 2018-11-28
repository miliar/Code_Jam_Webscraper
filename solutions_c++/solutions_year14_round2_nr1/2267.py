//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)

//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

string s[101];
class data{
public:
	char c;
	int countc;
};

vector< data > vd[101];

int main()
{
  int test,t,n,count_=0,ans=0;
  float sum=0;
  int mean;
  char c;
  int len;
  freopen("input.txt","r",stdin);
  freopen("output.txt","w+",stdout);
  cin >> test;
  t = test;
  bool lost=false;
  data temp;
  while(test--)
  {
  	cin >> n;
  	repi(i,0,n)
  		cin >> s[i];
  	lost = false;
  	ans=0;
  	mean=0;
  	sum=0;
  	repi(i,0,n)
			vd[i].clear();
  	repi(i,0,n)
  	{
  		count_=1;
  		c = s[i][0];
  		len=s[i].length();
  		repi(j,1,len)
  		{
  			if(s[i][j]==s[i][j-1])
  				count_++;
  			else if(s[i][j]!=s[i][j-1])
  			{
  				temp.c = c;
  				temp.countc = count_;
  				vd[i].push_back(temp);
  				count_=1;
  				c = s[i][j];
  			}
  		}
  		temp.c = c;
			temp.countc = count_;
			vd[i].push_back(temp);
  	}

		repi(i,0,vd[0].size())
		{
			sum=0;
			repi(j,0,n)
			{
				if(vd[0][i].c==vd[j][i].c && vd[0].size()==vd[j].size())
				{
					sum+=vd[j][i].countc;
				}
				else
				{
					lost = true;
					break;
				}
			}
			if(lost)
				break;
			mean = nearbyint(sum/n);
			repi(j,0,n)
			{
				ans+=abs(mean-vd[j][i].countc);
			}
		}
		if(lost)
			printf("Case #%d: Fegla Won\n",t-test);
		else
			printf("Case #%d: %d\n",t-test,ans);
  }
  return 0;
}