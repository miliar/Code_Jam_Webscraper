#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <deque>
#include <ctime>
#define s(n) scanf("%d",&n)
#define ss(n) scanf("%s",n)
#define s2(a,b) scanf("%d%d",&a,&b)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define vi vector<int>
#define ii pair<int,int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define LL long long
#define ULL unsigned long long
#define R freopen("in","r",stdin)
#define W freopen("out","w",stdout)
using namespace std;

int main()
{
    R;W;
    int t;cin>>t;
    int c =0;
    while(t--)
    {
        c++;
        cout<<"Case #"<<c<<": ";
        int n;cin>>n;
        string str;
        cin>>str;
        int tot = 0;
        int num = 0;
        num += (str[0]-'0');
        tot = num;
        for(int i=1;i<=n;i++)
        {
            if(str[i]>'0')
            {
                if(num<i)
                    num = i;
                
                num += (str[i]-'0');
                tot += (str[i]-'0');
            }
        }
        cout<<num-tot<<endl;
        
    }
}