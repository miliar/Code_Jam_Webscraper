#include<bits/stdc++.h>
#define INF 1e9
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define MAXN 30
#define MAXV 30000
#define MOD 1000000007
#define get(a) geta(&a)
#define getw getchar
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define MAX 100
typedef long long lld;
using namespace std;
template<class T>
inline void geta(T* a)
{
    T n=0;
    char p;
    T s=1;
    p=getw();
    if(p=='-')
        s=-1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-')
        p=getw();
    if(p=='-')
        s=-1;
    while(p>='0'&&p<='9')
    {
        n=(n<<3)+(n<<1)+p-'0';
        p=getw();
    }
    *a=n*s;
}

lld no_digits(lld a,lld b)
{
    lld ans=(int)(b*log10(a))+1;
    return ans;
}

lld pow_10(lld d)
{
    lld res=1;
    for(lld i=1;i<=d;++i)
        res*=10;
    return res;
}

lld power(lld a,lld b,lld d)
{
    lld res=1;
    lld rm=pow_10(d);
    //cout<<"pow_10 "<<rm<<endl;
    while(b>0)
    {
        if(b&1)
        {
            res=((res%rm)*(a%rm))%rm;
        }
        a=((a%rm)*(a%rm))%rm;
        b/=2;
    }
    return res;
}

lld gcd(lld a,lld b)
{
    if(a==0)
        return b;
    return gcd(b%a,a);
}

lld gcd2(lld a,lld b)
{
    while(a)
    {
        lld r=b%a;
        b=a;
        a=r;
    }
    return b;
}
string s;

int a[128][128];
int L,X;

map<int,vector<int> > m;




void init()
{
    a[1][1]=1,a[1]['i']='i',a[1]['j']='j',a[1]['k']='k';
    a['i'][1]='i',a['i']['i']=-1,a['i']['j']='k',a['i']['k']=-'j';
    a['j'][1]='j',a['j']['i']=-'k',a['j']['j']=-1,a['j']['k']='i';
    a['k'][1]='k',a['k']['i']='j',a['k']['j']=-'i',a['k']['k']=-1;
}


int mul(int i,int j)
{

    //cout<<"i "<<i<<" j "<<j<<endl;
    int ans=1;
    if(i<0)
    {
        i*=-1;
        ans=-1;
    }
    if(j<0)
    {
        ans*=-1;
        j*=-1;
    }
    //cout<<"mul "<<a[i][j]<<endl;
    ans*=a[i][j];
    //cout<<ans<<endl;
    return ans;
}

void init2()
{
    vector<int> v;
    for(int i=105;i<=107;++i)
    {
        int x=mul(i,105);
        v.push_back(x);
        x=mul(i,106);
        v.push_back(x);
        x=mul(i,107);
        v.push_back(x);
        x=mul(i,-105);
        v.push_back(x);
        x=mul(i,-106);
        v.push_back(x);
        x=mul(i,-107);
        v.push_back(x);
        x=mul(i,1);
        v.push_back(x);
        x=mul(i,-1);
        v.push_back(x);
        m[i]=v;
        v.clear();
    }
    v.clear();
    for(int j=105;j<=107;++j)
    {
        int i=j*-1;
        int x=mul(i,105);
        v.push_back(x);
        x=mul(i,106);
        v.push_back(x);
        x=mul(i,107);
        v.push_back(x);
        x=mul(i,-105);
        v.push_back(x);
        x=mul(i,-106);
        v.push_back(x);
        x=mul(i,-107);
        v.push_back(x);
        x=mul(i,1);
        v.push_back(x);
        x=mul(i,-1);
        v.push_back(x);
        m[i]=v;
        v.clear();
    }
    int i=1;
    int x=mul(i,105);
        v.push_back(x);
        x=mul(i,106);
        v.push_back(x);
        x=mul(i,107);
        v.push_back(x);
        x=mul(i,-105);
        v.push_back(x);
        x=mul(i,-106);
        v.push_back(x);
        x=mul(i,-107);
        v.push_back(x);
        x=mul(i,1);
        v.push_back(x);
        x=mul(i,-1);
        v.push_back(x);
        m[i]=v;
        v.clear();
    i=-1;
    x=mul(i,105);
        v.push_back(x);
        x=mul(i,106);
        v.push_back(x);
        x=mul(i,107);
        v.push_back(x);
        x=mul(i,-105);
        v.push_back(x);
        x=mul(i,-106);
        v.push_back(x);
        x=mul(i,-107);
        v.push_back(x);
        x=mul(i,1);
        v.push_back(x);
        x=mul(i,-1);
        v.push_back(x);
        m[i]=v;
        v.clear();
}

void gen_str()
{
    string tmp=s;
    for(int i=2;i<=X;++i)
    {
        s+=tmp;
    }
    //cout<<s<<endl;
}

vector<int> i_pos,k_pos;

vector<int> dp;


void find_i_pos()
{
    int x=s[0];
    if(s[0]=='i')
        i_pos.push_back(0);
    dp.push_back(x);
    for(int i=1;i<s.size();++i)
    {
        x=mul(x,s[i]);
        dp.push_back(x);
        //cout<<x<<" ";
        if(x==105)
        {
            i_pos.push_back(i);
            //cout<<"i_pos inside\n";
        }

    }
    //cout<<"size of i_pos "<<i_pos.size()<<endl;
    //cout<<"pos of i"<<endl;
    /*for(int i=0;i<i_pos.size();++i)
    {
        cout<<i_pos[i]<<" ";
    }*/
    //cout<<endl;

}


void find_k_pos()
{
    int i=s.size()-1;
    if(s[i]=='k')
        k_pos.push_back(i);
    int x=s[i];
    --i;
    for(;i>=0;--i)
    {
        x=mul(s[i],x);
        //cout<<ch<<" ";
        if(x==107)
        {
           k_pos.push_back(i);
           //cout<<"inside k_pos\n";
           //cout<<"inside k_pos\n";
        }

    }
    sort(k_pos.begin(),k_pos.end());
    /*for(i=0;i<k_pos.size();++i)
        cout<<k_pos[i]<<" ";

    cout<<endl;*/
}


bool pos_j(int l,int r)
{
    int n=s.size();
    if(l<0||r>=n||l>r)
    return 0;
    //int ans;
    int y=dp[r];
    if(l!=0)
    {
        int x=dp[l-1];
        vector<int> v=m[x];
        int i;
        for(i=0;i<v.size();++i)
        {
            if(v[i]==y)
                break;
        }
        if(i==1)
            return true;
        return 0;
    }

    //char ch=x;
    if(y==106)
        return 1;
    else
        return 0;

}


bool solve()
{
    for(int i=0;i<i_pos.size();++i)
    {
        int l=i_pos[i];
        for(int j=0;j<k_pos.size();++j)
        {
            int r=k_pos[j];
            if(l<r)
            {
                if(pos_j(l+1,r-1))
                return true;
            }

        }
    }
    return 0;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    init();
    init2();
    int t,tt;
    get(t);
    for(tt=1;tt<=t;++tt)
    {
        i_pos.clear();
        k_pos.clear();
        dp.clear();
        printf("Case #%d: ",tt);
        cin>>L>>X;
        cin>>s;
        gen_str();
        find_i_pos();
        find_k_pos();
        if(solve())
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}


