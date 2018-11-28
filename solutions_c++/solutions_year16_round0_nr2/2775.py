#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <functional>
#include <climits>
#include <list>
#include <ctime>
#include <complex>

#define F1(x,y,z) for(int x=y;x<z;x++)
#define F2(x,y,z) for(int x=y;x<=z;x++)
#define F3(x,y,z) for(int x=y;x>z;x--)
#define F4(x,y,z) for(int x=y;x>=z;x--)
#define pb push_back
#define LL long long
#define co complex<double>

#define MAX 100005
#define AMAX 1500
#define MOD 1000000007

#define f(c,d) ((1<<(c))*(d))

using namespace std;

int t,n,ans,ta;
char x[105];
bool y[105];

int main(){
	scanf("%d",&t);
	F2(a,1,t){
	    memset(x,0,sizeof(x));
	    n=ans=0;
	    scanf("%s",x);
	    while(x[n])n++;
	    F1(b,0,n)y[b]=(x[b]=='+');
	    //printf("%d [%s]\n",n,x);
	    n--;
	    while(n){
	        if(y[n])n--;
	        else{
	            if(y[0]){
	                ta=n;
	                while(!y[ta])ta--;
	                reverse(y,y+ta+1);
	                F2(b,0,ta)y[b]^=1;
	                ans++;
	            }else{
	                reverse(y,y+n+1);
	                F2(b,0,n)y[b]^=1;
	                n--;
	                ans++;
	            }
	        }
	    }
	    if(!y[0])ans++;
	    printf("Case #%d: %d\n",a,ans);
	}
	return 0;
}