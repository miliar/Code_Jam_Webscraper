//MJRT
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
//////////////////////
#include<iostream>
#include<algorithm>
#include<string>
#include <iterator>
#include<sstream>
#include<functional>
#include<numeric>
///////////////////////
#include<vector>
#include<map>
#include <stack>
#include<queue>
#include<set>
#include <bitset>
#include <list>
///////////////////////
//#include<ext/pb_ds/priority_queue.hpp> //pd_bs库,hdu&&poj不支持
using namespace std;
#define lowbit(x) ((x)&(-x))
static int INDEX = 0,BUGs = 0;
template <class T1, class T2>inline void gmax(T1 &a, T2 b) { if (b>a)a = b; }
template <class T1, class T2>inline void gmin(T1 &a, T2 b) { if (b<a)a = b; }
template<class T> T MAX(T a, T b) { return a > b ? a : b; }
template<class T> T MIN(T a, T b) { return a < b ? a : b; }
template<class T> T GCD(T a, T b) { return b ? GCD(b, a%b) : a; }
template<class T> T LCM(T a, T b) { return a / GCD(a,b) * b;    }
#define BUG() cout << "There is BUG No." << BUGs++ <<endl
#define Whats(x)          cout << "{ "<< #x << " }" << " is " << "*** "<< x << " ***" << "  index:" << INDEX++ <<endl
#define Show(x,s,l)      {cout << #x << ": "; for(int i = s ; i < s+l ; i++) cout << x[i] << " ";  cout << "\n";}
#define Show2(x,s,l,h)   {cout << #x << ": " << l-s << "*" <<h-s <<"\n"; for(int j = s ; j < s+h ; j++){for(int i = s ; i < s+l ; i++) cout << x[j][i] << " ";cout << "\n";};  cout << "\n";}

typedef  long long int LL;
const int INF = 0x3f3f3f3f;

const int N = 5 + 100;
bool vis[N];
char s[N];


int main()
{
    //ios::sync_with_stdio(false);
//#ifndef ONLINE_JUDGE
//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif
    int Case,tot = 1;
    scanf("%d",&Case);
    while(Case--)
    {
        memset(vis,0,sizeof(vis));
        scanf("%s",s);
        int l = strlen(s);

        for(int i = 0 ; i < l ; i++)
        {
            if(s[i] == '-') vis[i] = 0;
            else            vis[i] = 1;
        }

        int cnt = 0;
        for(int i = 0 ; i < l-1 ; i++)
        {
            if(vis[i]^vis[i+1])
            {
                cnt++;
                for(int j = 0 ; j <= i ; j++)
                {
                    vis[j] ^= 1;
                }
            }
        }

        if(!vis[l-1]) cnt++;

        printf("Case #%d: %d\n",tot++,cnt);
    }
    return 0;
}

