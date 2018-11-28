#include<cstdio>
#include<cstdlib>
#include<time.h>
#include<cmath>
#include<cstring>
#include<string>
#include<iostream>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>

//#include<bits/c++std.h>

#define Size 1000005
#define inf 2e9
#define INF 2e18
#define LL long long int
#define i64 __int64
#define ULL unsigned long long
#define Mod 1000000007
#define pi 4*atan(1)
#define eps 1e-8
#define lson now*2,l,l+(r-l)/2
#define rson now*2+1,l+(r-l)/2+1,r
#define Max(a,b) (a)>(b)?(a):(b)
using namespace std;
int n,m,k;
int ql,qr,pos;

int main()
{
    #ifndef ONLINE_JUDGE
//        freopen("input.txt","r",stdin);
//        freopen("output.txt","w",stdout);
    #endif // ONLINE_JUDGE
    int t;
    int x,y,z;
    srand(time(NULL));
    int Case=0;
    cin>>t;
    string s;
//    deque<char> q;
    char arr[5000];
    while(t--)
//    while(scanf("%d",&n)==1)
    {
        cin>>s;
//        while(!q.empty())
//            q.pop();
        memset(arr,0,sizeof(arr));
        arr[2400] = s[0];
        int p1 = 2400;
        int p2 = 2400;
        for(int i=1;i<s.size();++i)
        {
            if(s[i] >= arr[p1])
                arr[--p1] = s[i];
            else
            {
                arr[++p2] = s[i];
            }
        }
        printf("Case #%d: ",++Case);
        for(int i=p1;i<=p2;++i)
            printf("%c",arr[i]);
        cout<<endl;
    }
    return 0;
}

