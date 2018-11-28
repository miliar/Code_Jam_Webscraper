#include <vector>
#include <unistd.h>
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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>

using namespace std;

#define PI 3.141592653589
#define DEG2RAD(deg) (deg * PI / 180)
const int INF = 2000000000;

typedef vector <int> VI ;
typedef vector <double> VD ;
typedef pair<int,int> PII;

#define fi(i,a,b) for(int i = a ; i < b ; i++)
#define fd(i,a,b) for(int i = a ; i > = b ; i--)
#define REP(i,n) fi(i,0,n)
#define pb push_back
#define ALL(a) (a).begin(),(a).end()
#define SORT(a) sort(ALL(a))
#define SZ(a) (int) (a).size()
#define VS vector <string> 
#define prnt(a,n) REP(i,n) cout<<a[i] << " " ; cout << endl

int main()
{
	int T=0,c=1;
	long long int arr[]= {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,	125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
	scanf("%d",&T);
	while(T--)
	{
		long long int A=0,B=0;
		scanf("%lld%lld",&A,&B);
		int count=0;
		REP(i,39)
		{
			if(arr[i]>= A && arr[i] <= B)
				count++;
			if(arr[i] > B)
				break;
		}
		printf("Case #%d: %d\n",c,count);
		c++;
	}
	return 0;
}
