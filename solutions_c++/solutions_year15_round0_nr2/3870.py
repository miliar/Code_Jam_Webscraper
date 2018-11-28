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

int n;
list<int> p;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,tt=1;
    get(t);
    while(t--)
    {

        get(n);
        int max_p=-1;
        p.clear();
        for(int i=1;i<=n;++i)
        {
            int x;
            get(x);
            p.push_back(x);
            if(x>max_p)
                max_p=x;
        }
        int max_v=max_p;
        int ans=max_p;
        list<int>::iterator it=p.begin();
        while(it!=p.end())
        {
            if(*it==max_p)
                break;
            ++it;
        }
        p.erase(it);
        int next_max=-1;
        it=p.begin();
        while(it!=p.end())
        {
            if(*it>next_max)
            next_max=*it;
                ++it;
        }

        if((max_p==9&&next_max==-1)||(max_p==9&&(next_max<=3||next_max==6)))
        {
            p.push_back(3);
            p.push_back(6);
        }
        else
        {
            if(max_p&1)
            {
                p.push_back(max_p/2);
                p.push_back(max_p/2+1);
            }
            else
            {
                p.push_back(max_p/2);
                p.push_back(max_p/2);
            }

        }


        int sp=0;
        while(sp<=max_v)
        {
            ++sp;
            list<int>::iterator it=p.begin();
            list<int>::iterator it1;
            max_p=-1;
            while(it!=p.end())
            {
                if(*it>max_p)
                {
                    max_p=*it;
                    it1=it;
                }
                ++it;
            }
            int new_ans=sp+max_p;
            /*if(new_ans>ans)
                break;
            ans=new_ans;*/
            ans=min(ans,new_ans);

            p.erase(it1);
            next_max=-1;
            it=p.begin();
            while(it!=p.end())
            {
                if(*it>next_max)
                next_max=*it;
                ++it;
            }


            if((max_p==9&&next_max==-1)||(max_p==9&&(next_max<=3||next_max==6)))
            {
                p.push_back(3);
                p.push_back(6);

            }
            else
            {
                if(max_p&1)
                {
                    p.push_back(max_p/2);
                    p.push_back(max_p/2+1);
                }
                else
                {
                    p.push_back(max_p/2);
                    p.push_back(max_p/2);
                }
            }
        }
        printf("Case #%d: %d\n",tt,ans);
        ++tt;
    }
    return 0;
}
