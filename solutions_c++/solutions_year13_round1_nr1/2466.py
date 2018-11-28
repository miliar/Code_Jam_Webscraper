using namespace std;
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define rep(i,n) for(i=1;i<=n;++i)
#define max(a,b) ((a)>(b))?(a):(b)
typedef  long long int ull;

// (2*x+1)
//2*r+1 2(r+2)+1 + 2*(r+4)+1
// n+2*r*n +2(n)(n-1) >=t
// 
// 2*n^2 -2*n  +n +2*r*n >=t
//2*n^2 +n(2*r-1) -t =0
//2*50*50 +50(2*9999999999999999 -1)= 1000000000000000000


 



int main()
{
	
//	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	int tt,tc=1;
    double r1,r,t,b,d,check;
	cin>>tt;
	while(tt--)
	{
		
      cin>>r>>t;
      b=2*r-1;
      d=b*b+8.0*t;
      d=sqrt(d);
      r1=(d-(double)b)/4.0;
      r1=floor(r1);
      check=2*r1*r1 + r1*(2*r-1);
      if(check>t)r1--;
      
      
      printf("Case #%d: %0.0lf\n",tc++,r1);
    }
	return 0; 


//
}

