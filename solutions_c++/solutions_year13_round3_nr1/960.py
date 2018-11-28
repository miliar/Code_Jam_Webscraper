
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
#define fk(b,e) for (k)=b;(k)<(e);(k)++)
typedef long long LL;
//typedef __int64   LL;
typedef vector<int>vi;
typedef vector<string>vs;
typedef pair<int,int>pri;
typedef map<string,int>msi;
typedef map<vector<int>,int>mvi;
inline bool iseq(double x,double y){if(fabs(x-y)<eps)return true;return false;}
template<typename T>inline T hpt(T x1,T y1,T x2,T y2){return hypot(x1-x2,y1-y2);}
template<typename T>inline T gcd(T a,T b){if(!b)return a;else return gcd(b,a%b);}
template<typename T>inline void extended_euclid(T a,T b,T &x,T &y){if(a%b==0)x=0,y=1;else{extended_euclid(b,a%b,x,y);T temp=x;x=y;y=-y*(a/b)+temp;}}
template<typename T>inline T bigmod(T b,T p,T m){if(!p)return 1;else if(!(p%2)){T x=bigmod(b,p/2,m);return x*x;}else return ((b%m)*bigmod(b,p-1,m))%m;}
#define PS 5
int prime[PS/32+1];
void setbit(int i){int p=i>>5,q=i&31;prime[p]|=(1<<q);}
bool checkbit(int i){int p=i>>5,q=i&31;return prime[p]&(1<<q)?true:false;}
void buildprime(int n){int i,j,k=sqrt(double(n));prime[0]=3;for(i=4;i<n;i+=2)setbit(i);for(i=3;i<=k;i+=2){if(!checkbit(i)){int ii=i+i;for(j=i*i;j<n;j+=ii)setbit(j);}}}


int sum,r,n,t,N,R,C,txt;
#define S 1000505
char ch[S];
LL val[S];
bool isVowel(char c)
{
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}
int main(){
	freopen("1.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k;
	scanf("%d",&t);
	while(t--)
    {
        scanf("%s%d",ch,&n);
        //cout << n << " " << ch << endl;
        LL tot = 0, cur = 0;
        int len = strlen(ch);
        LL last = 0;
        for(int i = 0; i < len; ++i)
        {
            if(isVowel(ch[i]))val[i] = 0;
            else val[i] = last + 1;
            last = val[i];
            //cout << val[i] << " ";
        }
        //cout << endl;
        LL extra = 0;
        for(int i = 0; i < len; ++i)
        {
            if(val[i] < n)extra ++;
            else
            {
                if(cur) tot += extra * cur;
                extra = 0;

                LL left = i - n + 1;
                cur = left + 1;
                tot += cur;
            }
        }
        if(cur > 0) tot += extra * cur;
        printf("Case #%d: %lld\n", ++txt, tot);
    }
	return 0;
}
