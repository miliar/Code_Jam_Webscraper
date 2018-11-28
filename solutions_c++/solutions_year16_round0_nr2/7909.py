//pranjalr34

#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define all(a) a.begin(),a.end()
#define SZ(a) (int)(a.size())
#define fi(i,a,b) for(int i=a;i<b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define n_p next_permutation
#define b_s binary_search
#define min(a,b) ((a<b)?a:b)
#define max(a,b) ((a<b)?b:a)
#define gcd __gcd
#define INF INT_MAX
#define init(a,b) memset(a,b,sizeof(a))
#define INFL LLONG_MAX
#define trace1(x)                cerr <<#x<<": "<<x<<endl;
#define trace2(x, y)             cerr <<#x<<": "<<x<<" | "<<#y<<": "<<y<< endl;
#define trace3(x, y, z)          cerr <<#x<<": "<<x<<" | "<<#y<<": "<<y<<" | "<<#z<<": "<<z<<endl;
#define trace4(a, b, c, d)       cerr <<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl;
#define trace5(a, b, c, d, e)    cerr <<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<<": "<<e<<endl;

using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< PII > VPII;
typedef long long int LL;
typedef pair<LL,LL> PLL;
typedef vector<LL> VLL;
typedef vector< PLL > VPLL;
typedef set<int> SI;
typedef set<LL> SLL;

void FastIO(){ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL);cout.precision(15);}
//LL modpow(LL a,LL b,LL m){LL r = 1;while (b > 0){if (b % 2 == 1)r = (r * a) % m;b = b >> 1;a = (a * a) % m;}return r%m;}
//LL power(LL a, LL p){LL ret=1;while(p){if(p&1)ret=(ret*a);a=(a*a);p/=2;}return ret;}
//xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

int ans=0;
void cal(int l,int r,string &str)
{
    if(r<l)
        return;
    int i;
    int flag1=1,flag2=1;
    for(i=l;i<=r;i++)
    {
        if(str[i]=='-')
            flag1=0;
        if(str[i]=='+')
            flag2=0;
    }
    if(flag1)
        return;
    if(flag2)
    {
        ans++;
        return;
    }
    for(i=r;i>=l;i--)
    {
        if(str[i]=='-')
            break;
        else
            r--;
    }
    for(i=l;i<=r;i++)
    {
        if(str[i]=='-')
            break;
        else
            l++;
    }
    if(l!=0)
    {
        for(l=l-1;l>=0;l--)
            str[l]='-';
        l=0;
        ans++;
    }
    int f=0;
    string str1;
    str1.resize(r+1);
    for(i=l;i<=r;i++)
    {
        str1[i]=str[r-i];
        if(str1[i]=='-')
            str1[i]='+';
        else
            str1[i]='-';
        f=1;
    }
    for(i=l;i<=r;i++)
        str[i]=str1[i];
    if(f)
    ans++;
    cal(l,r,str);
}

int main()
{
    FastIO(); 
    int t,j=0,l;
    string str;
    cin >>t;
    while(j<t)
    {
        cin >>str;
        l=str.length();
        ans=0;
        cal(0,l-1,str);
        cout <<"Case #"<<j+1<<": "<<ans<<"\n";
        j++;
    }
    return 0;
}
