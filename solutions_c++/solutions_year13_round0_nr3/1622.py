/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull unsigned long long
#define M 1000000007

bool ispal(string a)
{
    int i=0;
    int j=a.size()-1;
    while(i<j)
    {
        if(a[i]!=a[j])return false;
        i++;
        j--;
    }
    return true;
}

bool check(ll n)
{
    string str;
    while(n)
    {
        int x=n%10;
        str=str+(char)(x+'0');
        n=n/10;
    }
    reverse(str.begin(),str.end());
    return ispal(str);
}
int main()
{
    #ifndef ONLINE_JUDGE
	in("in.txt");
	out("out.txt");
    #endif
    int cnt=0;
    vector<ll>PLs;
    for(ll i=1;i<=10000000;i++)
    {
        if(i*i>100000000000000)continue;
        if(check(i) && check(i*i))
        {
            PLs.push_back(i*i);
        }
    }
    int t,caseno=1;
    cin>>t;
    while(t--)
    {
        ll a,b;
        scanf("%lld %lld",&a,&b);
        vector<ll>::iterator up1,up2;
        int ai,bi;

        up1=lower_bound(PLs.begin(),PLs.end(),a);
        up2=lower_bound(PLs.begin(),PLs.end(),b);
        ai=(int)(up1-PLs.begin());
        bi=(int)(up2-PLs.begin());

        if(binary_search(PLs.begin(),PLs.end(),b))
            bi++;
//        cout<<PLs[ai]<<" "<<PLs[bi]<<endl;
        printf("Case #%d: %d\n",caseno++,bi-ai);
    }
	return 0;
}
