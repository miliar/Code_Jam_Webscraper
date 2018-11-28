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

int t,n;
set<int> s;

LL f1(int a){
    s.clear();
    for(LL b=a;;b+=a){
        LL c=b;
        while(c){
            s.insert(c%10);
            c/=10;
        }
        if(s.size()==10){
             return b;
        }
    }
}


int main(){
	scanf("%d",&t);
	F2(a,1,t){
	    scanf("%d",&n);
	    if(n)printf("Case #%d: %lld\n",a,f1(n));
	    else printf("Case #%d: INSOMNIA\n",a);
	}
	return 0;
}