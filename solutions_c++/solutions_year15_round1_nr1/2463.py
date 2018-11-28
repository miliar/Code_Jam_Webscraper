#include <iostream>
#include <cstdio>
#define MAX(x,y) (x)>(y)?(x):(y)
#define MIN(x,y) (x)<(y)?(x):(y)
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,f[1010];
	cin >> T;
	for(int t=1;t<=T;++t) {
	    int n,ans1=0,ans2=0,ratio=0;
	    cin >> n;
	    for(int i=0;i<n;++i) {
            cin >> f[i];
        }
        for(int i=1;i<n;++i) {
            ans2 += MAX(0,f[i-1]-f[i]);
            ratio = MAX(ratio,f[i-1]-f[i]); 
        }
        for(int i=0;i<n-1;++i) {
            ans1 += MIN(f[i],ratio);
        }
        printf("Case #%d: %d %d\n",t,ans2,ans1);
	}
	return 0;
}
