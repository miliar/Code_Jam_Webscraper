/*  AMAN MITTAL
    Computer Science and Engineering Sophomore
    M.N.N.I.T. Allahabad
    INDIA   */
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cassert>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <numeric>
#include <bitset>
#include <cstdio>
#include <cstring>
#include <limits>

using namespace std;

#define LL long long int
#define LLU long long unsigned int
#define FOR(i,n) for(int i=0;i<n;i++)
#define TEST(t) while(t--)
#define pb push_back
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define getcx getchar_unlocked
#define clr(a,b) memset(a,b,sizeof(a))
#define MAXAR 1100000
#define MOD 1000000007
#define X first
#define Y second

const int mini = numeric_limits<int>::min();
const LL minl = numeric_limits<LL>::min();
const int maxi = numeric_limits<int>::max();
const LL maxl = numeric_limits<LL>::max();
const LL maxd = numeric_limits<double>::max();

typedef pair<int, int> pii;
typedef pair<int,float> pif;
typedef vector<int>vi;

int gcd(int a,int b){
    if(b==0) return a;
    else return gcd(b,a%b);}

int main()
{
	int i,t,tst,j,rem;
	double c,x,f,ans,ansf,rat;
	cin>>t;
	for(tst=1;tst<=t;tst++)
	{
		cin>>c>>f>>x;
		ansf=100000;
		rat=2.0;
		i=-1;
		rem=0;
		ans=100000;
		while(ans<=ansf)
		{
			ansf=ans;
			ans=0;
			rat=2.0;
			i++;
			for(j=0;j<i;j++)
			{
				ans+=(c/rat);
				rat+=f;
			}
			ans+=(x/rat);
			//cout<<ans<<endl;
		}
		printf("Case #%d: %.7lf\n",tst,ansf);
	}
	return 0;
}
