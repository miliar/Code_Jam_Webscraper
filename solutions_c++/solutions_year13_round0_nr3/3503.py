#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <bitset>
#include <sstream>
#include <string>

#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>

#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define FILL(arr,n) memset(arr,n,sizeof(arr))
#define FORUP(i,m,n) for(int i=(m); i<(n); i++)
#define FORDOWN(i,m,n) for(int i=(m)-1; i>=(n); i--)

#define PB push_back
#define MP make_pair
#define F first
#define S second

#define INF 2000000000
#define EPS 1e-11
#define PI acos(-1.0)
#define MAX_N 1000005
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;

int isFairSquare[10000005];

bool isPalindrome(long long num)
{
	 long long n = num;
	 long long digit = 0LL;
	 long long rev = 0LL;
     do
     {
         digit = num%10;
         rev = (10LL * rev) + digit;
		 num = num/10;
     }while (num!=0);

     if (n == rev)return true;
	 else return false;
}

int
main()
{
	isFairSquare[0] = 0;
	for(int i = 1;i <= 10000000;i++)
	{
		if(isPalindrome((long long)i) && isPalindrome((long long)(i*i)))isFairSquare[i] = isFairSquare[i-1] + 1;
		else isFairSquare[i] = isFairSquare[i-1];
		
		//if(i == 10 || i == 9)printf("%d : %d\n",i,isFairSquare[i]);
	}

	int T;
	scanf("%d", &T);
	for(int tc = 1;tc <= T;tc++)
	{
		long long A,B;
		cin >> A >> B;
		double As,Bs;
		As = sqrt((double)A);
		Bs = sqrt((double)B);
		int Aint = (int)As;
		int Bint = (int)Bs;
		int ans = isFairSquare[Bint] - isFairSquare[Aint];
		//printf("bef %d after %d\n",isFairSquare[Aint-1],isFairSquare[Aint]);
		if(As -(double)Aint < 1e-3 && isFairSquare[Aint] != isFairSquare[Aint-1])ans++;
		//printf("Aint %d Bint %d isAint %d isBint %d\n",Aint,Bint,isFairSquare[Aint],isFairSquare[Bint]);
		printf("Case #%d: %d\n",tc,ans);
	}
return 0;
}