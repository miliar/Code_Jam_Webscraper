/*
 * File:     main.cpp
 * Author:   Hrayr [HarHro94]
 * Problem:  
 * IDE:      Visual C++ 2008
 */
//#pragma comment(linker, "/STACK:66777216")
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <cstring>
#include <cstdio>
#include <string>
#include <Vector>
#include <ctime>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
#define sz(v) (int)(v).size()
#define LL long long
#define LD long double

const int SIZE = 200;
class Bigint
{
public:
    int  n, dig[SIZE];
   
    Bigint()
    {
        n=1;
        memset(dig, 0, sizeof dig);
    }

    Bigint(const char *st)
    {
        memset(dig, 0, sizeof dig);
        n=strlen(st);
        for(int i=n-1;i>=0;--i)
        {
            dig[n-1-i]=st[i]-'0';
        }
    }

    Bigint(LL num)
    {
        memset(dig, 0, sizeof dig);
        if (num==0)
        {
            dig[0]=0;
            n=1;
            return;
        }
        n=0;
        while(num)
        {
            dig[n++]=num%10;
            num/=10;
        }
    }

    Bigint operator + (const Bigint &ot) 
    {
        Bigint ret;
        int i, c=0;
        ret.n=max(n, ot.n);
        for(i=0;i<ret.n;++i)
        {
            ret.dig[i]=dig[i]+ot.dig[i]+c;
            c=ret.dig[i]/10;
            ret.dig[i]%=10;
        }
        while(c)
        {
            ret.dig[ret.n++]=c%10;
            c/=10;
        }
        return ret;
    }

    Bigint operator * (const Bigint &ot)
    {
        Bigint ret;
        int i, j, c=0;
        ret.n=ot.n+n;
        for(i=0;i<n;++i)
        {
            for(j=0;j<ot.n;++j)
            {
                ret.dig[i+j]+=dig[i]*ot.dig[j];
            }
        }
        for(i=0;i<ret.n;++i)
        {
            ret.dig[i]+=c;
            c=ret.dig[i]/10;
            ret.dig[i]%=10;
        }
        while(c)
        {
            ret.dig[ret.n++]=c%10;
            c/=10;
        }
        while(ret.n>1 && ret.dig[ret.n-1]==0)
        {
            ret.n--;
        }
        return ret;
    }

    Bigint operator + (const LL &num)
    {
        Bigint ot(num);
        return *this+ot;
    }

    Bigint operator * (const LL &num)
    {
        Bigint ot(num);
        return *this*ot;
    }

    Bigint operator += (const LL &num)
    {
        Bigint ot(num);
        return (*this+=ot);
    }

    Bigint operator += (const Bigint &ot)
    {
        *this=(*this+ot);
        return *this;
    }

    bool operator == (const Bigint &ot) const 
    {
        if (n!=ot.n)
        {
            return false;
        }
        for(int i=0;i<n;++i)
        {
            if (dig[i]!=ot.dig[i])
            {
                return false;
            }
        }
        return true;
    }

    bool operator < (const Bigint &ot) const
    { 
        if (n<ot.n)
        {
            return true;
        }
        for(int i=n-1;i>=0;--i)
        {
            if (dig[i]<ot.dig[i])
            {
                return true;
            }
            if (dig[i]>ot.dig[i])
            {
                return false;
            }
        }
	    return false;
    }

    Bigint sqrt() const
    {
	    Bigint b;
	    int i, j;
	    b.n=(n+1)/2;
	    for(i=b.n-1;i>=0;i--)
	    {
		    for(j=0;j<=9;j++)
		    {
			    b.dig[i]=j;
			    if (*this<b*b)
			    {
				    break;
			    }
		    }
		    b.dig[i]=j-1;
	    }
	    return b;
    }
} a, b, A, B;
vector<Bigint> goods;
int res;

ostream& operator << (ostream &os, const Bigint &num)
{
    for(int i=num.n-1;i>=0;--i)
    {
        os << num.dig[i];
    }
    return os;
}

istream& operator >> (istream &is, Bigint &num)
{
    char st[SIZE];
    is >> st;
    num=Bigint(st);
    return is;
}

Bigint make2002(int len) // len>=2
{
    Bigint ret;
    ret.n=len;
    for(int i=0;i<ret.n;++i)
    {
        if (i==0 || i==ret.n-1)
        {
            ret.dig[i]=2;
        }
        else 
        {
            ret.dig[i]=0;
        }
    }
    return ret;
}

Bigint make20102(int len) // len=2*k+1, k>=1
{
    Bigint ret;
    ret.n=len;
    for(int i=0;i<ret.n;++i)
    {
        if (i==0 || i==ret.n-1)
        {
            ret.dig[i]=2;
        }
        else if (i==len/2)
        {
            ret.dig[i]=1;
        }
        else 
        {
            ret.dig[i]=0;
        }
    }
    return ret;
}

inline bool ok(const Bigint &num)
{
    return ((num==a || a<num) && (num==b || num<b));
}

void rec(int r, int cur, int p, int len, char *st)
{
    if (cur>9)
    {
        return;
    }
    if (r==0)
    {
        goods.pb(Bigint(st));
        return;
    }
    st[p]='0';
    st[len-1-p]='0';
    rec(r-1, cur, p+1, len, st);
    st[p]='1';
    st[len-1-p]='1';
    rec(r-1, cur+2, p+1, len, st);
}

void precalc()
{
    goods.pb(Bigint(1));
    goods.pb(Bigint(2));
    goods.pb(Bigint(3));
    for(int len=2;len<53;++len)
    {
        goods.pb(make2002(len));
        if (len%2)
        {
            goods.pb(make20102(len));
            char st[107];
            st[0]='1';
            st[len-1]='1';
            st[len]='\0';
            
            st[len/2]='0';
            rec((len-2)/2, 2*1+0, 1, len, st); // 10..0..01
            
            st[len/2]='1';
            rec((len-2)/2, 2*1+1, 1, len, st); // 10..1..01
            
            st[len/2]='2';
            rec((len-2)/2, 2*1+4, 1, len, st); // 10..2..01
        }
        else 
        {
            char st[107];
            st[0]='1';
            st[len-1]='1';
            st[len]='\0';
            rec((len-2)/2, 2*1, 1, len, st); // 1??..??1
        }
    }
    sort(all(goods));
}

bool check(LL n)
{
    int i, p=0, dig[20];
    while(n)
    {
        dig[p++]=n%10;
        n/=10;
    }
    for(i=0;i<p/2;++i)
    {
        if (dig[i]!=dig[p-i-1])
        {
            return false;
        }
    }
    return true;
}

int main()
{
#ifdef harhro94
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int i, test, testCnt;
/*
    int cnt=0;
    LL good[100];
    for(i=1;i<10000007;++i)
    {
        if (check(i))
        {
            if (check(1LL*i*i))
            {
                good[cnt++]=1LL*i*i;
            }
        }
    }
    cerr << cnt << endl;
    for(i=0;i<cnt;++i)
    {
        cerr << good[i] << " " << int(sqrt(good[i]+0.0)+1e-6) << endl;
    }
    cin >> testCnt;
    for(test=1;test<=testCnt;++test)
    {
        LL a, b;
        int res=0;
        cin >> a >> b;
        for(i=0;i<cnt;++i)
        {
            if (good[i]>=a && good[i]<=b)
            {
                ++res;
            }
        }
        cout << "Case #" << test << ": " << res << endl;
    }
*/
    precalc();
    cin >> testCnt;
    for(test=1;test<=testCnt;++test)
    {
        cin >> A >> B;
        int res=0;
        a=A.sqrt();
        b=B.sqrt();
        if (!(a*a==A))
        {
            a+=Bigint(1LL);
        }
        int l=0;
        int r=sz(goods)-1;
        int L, R;
        while(l<r)
        {
            int m=(l+r)/2;
            if (goods[m]==a || a<goods[m])
            {
                r=m;
            }
            else 
            {
                l=m+1;
            }
        }
        L=l;
        l=0;
        r=sz(goods)-1;
        while(l<r)
        {
            int m=(l+r+1)/2;
            if (goods[m]==b || goods[m]<b)
            {
                l=m;
            }
            else 
            {
                r=m-1;
            }
        }
        R=l;
        if (L>R)
        {
            res=0;
        }
        else 
        {
            res=R-L+1;
        }
        cout << "Case #" << test << ": " << res << endl;
        /*
        int tmp=0;
        for(i=0;i<cnt;++i)
        {
            if (good[i]>=ta && good[i]<=tb)
            {
                ++tmp;
            }
        }
        if (res!=tmp)
        {
            cerr << test << " " << res << " " << tmp << endl;
        }*/
    }

#ifdef harhro94
	cerr << fixed << setprecision(3) << "\nExecution time = " << clock()/1000.0 << "s\n";
#endif
	return 0;
}
