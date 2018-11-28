#include <bits/stdc++.h>
#define f first
#define s second
#define ll long long
#define pii  pair<int,int>
#define pli pair<ll,int>
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define mod 1000000007

using namespace std;
int read()
{
    int  x;
    scanf("%d",&x);
    return x;
}
bool cmp(pair <int, pii > a, pair <int, pii > b)
{
    return a.f > b.f;
}

int string_num(string s)
{
    int ans =s[0]-'0';
    for(int i=1;i<s.length();i++)
    {
        ans*=10;
        ans +=(s[i]-'0');

    }
    return ans;
}

void add_set(int a, set<int> &q)
{
    while(a)
    {
        int rem = a%10;
        q.insert(rem);
        a/=10;
    }
}
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out2.txt","w",stdout);
    int t = read();
    for(int x=1;x<=t;x++)
    {
       int k = read(),c=read(),s=read();

        printf("Case #%d: ",x);
        for(int i=1;i<=k;i++)
        {
            printf("%d ", i);

        }
        printf("\n");
    }
    return 0;
}
