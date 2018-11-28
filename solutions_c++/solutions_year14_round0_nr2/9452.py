#include<iostream>
#include<sstream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<climits>
#include<iomanip>
#include<cstdlib>
#include<ctype.h>
#include<algorithm>
#include<numeric>
#include<vector>
#include<list>
#include<set>
#include<bitset>
#include<map>
#include<queue>
#include<deque>
#include<stack>
#define PI acos(-1)
#define EPS 1e-8
#define INF 2147483647
#define INIT(x,y) memset(x,y,sizeof(x))
#define INITip(x,y,n) memset(x,y,n*sizeof(int))
#define INITbp(x,y,n) memset(x,y,n*sizeof(bool))
#define Readfile(x) freopen(x,"r",stdin)
#define Writefile(x) freopen(x,"w",stdout)
typedef long long LL;
typedef long double LD;
using namespace std;
#define N 10005

double C,F,X;
double sum[N];

double cal(int k) {
    return sum[k]+X/(2+(k+1)*F);
}

/*int TSearch(int l,int r) {
    while(l+1<r) {
        int mid=(l+r)/2;
        int mmid=(mid+r)/2;
        if(cal(mid)<cal(mmid))
            r=mmid;
        else
            l=mid;
    }
    return (cal(l)<cal(r)?l:r);
}*/

int main() {
    ios_base::sync_with_stdio(false);
    //Readfile("in.txt");
    Readfile("B-small-attempt2.in");
    Writefile("B-small-attempt2.out");
    int t;
    cin>>t;
    for(int k=1;k<=t;++k) {
        cin>>C>>F>>X;
        INIT(sum,0);
        sum[0]=C/2;
        for(int i=1;i<N;++i)
            sum[i]=sum[i-1]+C/(2+i*F);
        //int x=TSearch(0,1000);
        int x=(X/C-2/F>EPS?(int)(X/C-2/F):0);
        double ans=min(X/2,cal(x-1));
        cout<<"Case #"<<k<<": "<<setprecision(7)<<fixed<<ans<<endl;
    }
    return 0;
}
