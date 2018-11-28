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

int n=32,m=500,ta,at;
int x[40];
vector<int> y,z;

int main(){
    printf("Case #1:\n");
    F2(a,1,m){
        memset(x,0,sizeof(x));
        x[n/2]=1;
        x[n-1]=1;
        ta=a;
        at=n-2;
        while(ta){
            x[at--]=ta%2;
            ta/=2;
        }
        F1(b,0,n/2)x[b]=x[b+n/2];
        F1(b,0,n)printf("%d",x[b]);
        F2(b,2,10){
            y.clear();
            y.pb(1);
            F1(c,0,n/2){
                z.clear();
                ta=at=0;
                while(ta||at<y.size()){
                    if(at<y.size())ta+=y[at]*b;
                    z.pb(ta%10);
                    ta/=10;
                    at++;
                }
                y=z;
            }
                z.clear();
                ta=at=0;
                ta=1;
                while(ta||at<y.size()){
                    if(at<y.size())ta+=y[at];
                    z.pb(ta%10);
                    ta/=10;
                    at++;
                }
                y=z;
            printf(" ");
            F4(c,y.size()-1,0)printf("%d",y[c]);
        }
        printf("\n");
    }
	return 0;
}