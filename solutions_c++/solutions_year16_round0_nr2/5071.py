#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<bitset>
#include<ctime>
#include<complex>
#define ft first
#define sd second
#define pb push_back
#define mkp make_pair
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)<(b)?(b):(a))
using namespace std;
typedef long long LL;
typedef pair<int,int> Pair;
const int inf=0x3f3f3f3f;
const double eps=1e-6;
const int mod=1e9+7;
const int maxn=110;
int n;
char a[maxn];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%s",a+1);
        int len=strlen(a+1);
        int ans=0;
        int p=2;
        char ch=a[1];
        while(a[p]==ch) p++;
        while(p<=len)
        {
            while(a[p]!=ch&&p<=len) p++;
            ans++;
            ch=(ch=='-'?'+':'-');
        }
        if(ch=='-') ans++;
        printf("Case #%d: %d\n",kase,ans);
    }
}
