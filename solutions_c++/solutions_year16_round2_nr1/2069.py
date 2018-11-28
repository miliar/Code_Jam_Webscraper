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
const int maxn=2010;
int n;
char a[maxn];
int cnt[300];
int ans[15];
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small-attempt0.out","w",stdout);
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        memset(cnt,0,sizeof(cnt));
        memset(ans,0,sizeof(ans));
        scanf("%s",a);
        int len=strlen(a);
        for(int i=0;i<len;i++)
            cnt[a[i]]++;

        ans[0]=cnt['Z'];
        cnt['E']-=cnt['Z'];
        cnt['O']-=cnt['Z'];
        cnt['R']-=cnt['Z'];
        cnt['Z']=0;

        ans[2]=cnt['W'];
        cnt['T']-=cnt['W'];
        cnt['O']-=cnt['W'];
        cnt['W']=0;

        ans[4]=cnt['U'];
        cnt['F']-=cnt['U'];
        cnt['O']-=cnt['U'];
        cnt['R']-=cnt['U'];
        cnt['U']=0;

        ans[6]=cnt['X'];
        cnt['S']-=cnt['X'];
        cnt['I']-=cnt['X'];
        cnt['X']=0;

        ans[8]=cnt['G'];
        cnt['E']-=cnt['G'];
        cnt['I']-=cnt['G'];
        cnt['H']-=cnt['G'];
        cnt['T']-=cnt['G'];
        cnt['G']=0;

        ans[5]=cnt['F'];
        cnt['I']-=cnt['F'];
        cnt['V']-=cnt['F'];
        cnt['E']-=cnt['F'];
        cnt['F']=0;

        ans[7]=cnt['V'];
        cnt['S']-=cnt['V'];
        cnt['E']-=cnt['V'];
        cnt['E']-=cnt['V'];
        cnt['N']-=cnt['V'];
        cnt['V']=0;

        ans[9]=cnt['I'];
        cnt['N']-=cnt['I'];
        cnt['N']-=cnt['I'];
        cnt['E']-=cnt['I'];
        cnt['I']=0;

        ans[3]=cnt['H'];
        cnt['T']-=cnt['H'];
        cnt['R']-=cnt['H'];
        cnt['E']-=cnt['H'];
        cnt['E']-=cnt['H'];
        cnt['H']=0;

        ans[1]=cnt['E'];

        printf("Case #%d: ",kase);
        for(int i=0;i<10;i++)
            for(int j=1;j<=ans[i];j++)
                printf("%d",i);
        puts("");
    }
}
