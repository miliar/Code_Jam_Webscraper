#include<iostream> 
#include<algorithm>
#include<queue>
#include<stack>
#include<numeric>
#include<vector>
#include<set>
#include<sstream>
#include<cstring>
#include<string>
#include<stdio.h>
#include<cmath>
#include<cstdlib>
#include<map>
using namespace std;
#define eps 1e-8
#define inf (1<<30)
#define pi (2*acos(0.0))
#define all(a) a.begin(),a.end()
#define mem(a,v) memset(a,v,sizeof(a))
#define rep(i,b,e) for((i)=b;(i)<(e);(i)++)
#define rev(i,b,e) for((i)=e-1;(i)>=(b);(i)--)
#define fi(b,e) for((i)=b;(i)<(e);(i)++)
#define fj(b,e) for((j)=b;(j)<(e);(j)++)
typedef long long LL;
typedef vector<int>vi;
typedef vector<string>vs;
typedef pair<int,int>pri;
template<typename T>inline T gcd(T a,T b){if(!b)return a;else return gcd(b,a%b);}
template<typename T>inline void extended_euclid(T a,T b,T &x,T &y){if(a%b==0)x=0,y=1;else{extended_euclid(b,a%b,x,y);T temp=x;x=y;y=-y*(a/b)+temp;}}
int sum,r,n,t,txt,N;

int val[20];
int mp[200];
int L, X;
void initialize(){
    val[0] = '1';val[1] = 'i';val[2] = 'j'; val[3] = 'k';
    mp['i'] = 1;mp['j'] = 2;mp['k'] = 3;mp['1'] = 0;
}



char getValue(char c1, char c2, int &neg){
    if(c1 == '1')return c2;
    else if(c2 == '1')return c1;
    else if(c1 == c2){
        neg = neg ^ 1;
        return '1';
    }else {
        int a = mp[c1];
        int b = mp[c2];
        int c = 6 - (a + b);
        char c3 = val[c];
        
        int mx = max(a, b);
        int mn = min(a, b);
        
        if(mx == a && mn == b)neg = neg ^ 1;
        if(mn == 1 && mx == 3)neg = neg ^ 1;
        return c3;
    }
}


#define S 10005
int dp[S][6][6][3];
int cases[S][6][6][3];
string ss;
int doit(int pos, int cc, int k, int neg){
    int &ret = dp[pos][cc][k][neg];
    if(cases[pos][cc][k][neg] == txt)return ret;
    cases[pos][cc][k][neg] = txt;
    char c = val[cc];
    if(pos == L * X){
        if(cc == 0 && k == 4 && neg == 0)return 1;
        else return 0;
    }

    if(k == 4)return 0;

    ret = 0;
    //check current one
    int neg2 = neg;
    char rc = getValue(c, ss[pos], neg2);
    //printf("current ss[pos] = %c c = %c value = %c index = %d\n", c, ss[pos], rc,  mp[rc]);
    //do noting
    //
    ret = doit(pos + 1, mp[rc], k, neg2);

    if(ret)return ret;
    if(neg2 == 0 && mp[rc] == k){
        ret = doit(pos + 1, 0, k + 1, 0);
        if(ret)return ret;
    }
    return ret = 0;
    
}
int main() {
	int i,j,k;
    initialize();
    freopen("c_small.in", "r", stdin);
    freopen("c_small.out", "w", stdout);
    scanf("%d",&t);
    while(t--){
        ++txt;
        scanf("%d%d",&L, &X);
        string sa = "";
        cin >> sa;
        ss = sa;
        for(int i = 1; i < X; ++i)ss += sa;
        //printf("total string = \n");
        //cout << ss << endl;
        int res = doit(0, 0, 1, 0);
        printf("Case #%d: ", txt);
        if(res)puts("YES");
        else puts("NO");        
    }
	return 0;
}








