//Aditya Dixit
#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <functional>
#include <algorithm>
#include <cstdlib>
#include <iomanip>
#include <stack>
#include <queue>
#include <deque>
#include <limits>
#include <cmath>
#include <numeric>
#include <set>

using namespace std;

#define gx getchar_unlocked
#define px putchar_unlocked
#define ps putchar_unlocked(' ')
#define pn putchar_unlocked('\n')
#define LIM
#define MOD 1000000009
#define pb push_back
#define mp make_pair
#define MEM(a, b) memset(a, (b), sizeof(a))
#define CLR(a) memset(a, 0, sizeof(a))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define DBG(vari) cerr<<#vari<<" ==> "<<(vari)<<endl;

const int INF = 2000000000;

typedef long long int i64;
typedef long int i32;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector <PII> VPII;

int main()
{
	//freopen("B-small-attempt0.in","r",stdin);
	freopen("B-large.in","r",stdin);
	freopen("aaout.txt","w",stdout);
	
	
	//std::ios_base::sync_with_stdio(false);
	int t,tt = 0;
	scanf("%d",&t);

	while(t--)
	{
		tt++;
		double c,f,x;
		
		double ans = 0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		
		double rate=2.0;
		double current,previous;
		if(x<=c)
		{
			current =x/rate;
			printf("Case #%d: %0.7lf\n",tt,current);
		    continue;
		}
		
		else
		{
			previous=x/rate;
			current=x/rate;
			
			ans=c/rate;
			
			while( current <= previous )
			{	
				rate=rate+f;
				previous=current;			
				current = ans + x/rate;
				ans +=c/rate;			
			    
			}
			
		}
		
		printf("Case #%d: %.7lf\n",tt,previous);
		
	}
	
    return 0;
}




