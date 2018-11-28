/*
USER: Mukesh 
TASK: 
ALGO: 
*/
#include <stdio.h>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <queue>
#include <sstream>
#include <iomanip>
#include <limits>
#include <time.h>
using namespace std;
//cout << fixed << setprecision(4);
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef istringstream iss; // >>
typedef ostringstream oss; //<<
#define geti(n) int n;scanf("%d",&n)
#define getl(n) long long n;cin >> n
#define getc(c) char c;cin >> c
#define rep(i,n) for(int i=0;i<n;i++)
#define puti(n) printf("%d\n",n)
#define ll long long
#define pb push_back
#define mem(p,q) memset(p,q,sizeof(p))
#define fu(i,a,n) for(int i=a;i<n;i++)
#define fd(i,n,a) for(int i=n;i>=a;i--)
#define mp make_pair
#define popcount __builtin_popcount
#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()
//#define max(x,y) ( x ^ ((x ^ y) & -(x < y)))
#define min(x,y) (y ^ ((x ^ y) & -(x < y)))
#define TRACE
using namespace std;
#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
#else
#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)
#endif
int main()
{ 
         /*#ifdef _WIN32 
    {freopen("A-large.in", "r", stdin);
     freopen("codejam.txt","w",stdout);}
   	#endif // LOCAL_USER
    */
    geti(T);
    int t = 1 ; 
    while(t<=T)
    {   string str ; 
    	geti(len);
    	cin>>str;
    	int people = (int)(str[0]-'0');
    	int ans = 0 ; 
    	for(int i=1;i<=len;i++)
    	{
    	  int num = (int)(str[i] - '0');
    	  if(num==0)
    	    	continue; 	
           if(i<=people)
           	  people+=num;
           	else
           	  {   
           	  	ans+= i-people;
           	  	people+=num + (i-people);
           	  }
    	}
    cout<<"Case #"<<t<<": "<<ans<<endl;	
    t++;
   }       
  
return 0 ; 
}