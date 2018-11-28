#include<bits/stdc++.h>
using namespace std;
//int arrr[1000005];
// inhortcuts for "common" data types in contests
typedef long long li;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
#define rep(i, a, b) for(li i=a; i<b; i++)
#define ALL(c) c.begin(), c.end()
#define rloop(i, a, b) for(int i=b-1; i>=a; i--)
#define loopinc(i, a, b, inc) for(int i=a; i<b; i+=inc)
/*Use like- 
rep(i,0,n - 1)
*/

template<class T> T pwr(T b, T p){T r=1,x=b;while(p){if(p&1)r*=x;x*=x;p=(p>>1);}return r;}
 
#define     inf             (0x7f7f7f7f)
const int MAXN = 5e6;
#define MOD 1000000007
li modPow(li a, li x, li p) {
    //calculates a^x mod p in logarithmic time.
    li res = 1;
    while(x > 0) {
        if( x % 2 != 0) {
            res = (res * a) % p;
        }
        a = (a * a) % p;
        x /= 2;
    }

    return res;
}
class CompareDist
{
public:
    bool operator()(pair<long long,long long> n1,pair<long long,long long> n2) {
        return n1.second>n2.second;
    }
};
class CompareDist1
{
public:
    bool operator()(pair<long long,long long> n1,pair<long long,long long> n2) {
        return n1.second<n2.second;
    }
};
long long mulmod(long long a, long long b) {
    long long res = 0;
    while (a != 0) {
        if (a & 1) res = (res + b) % MOD;
        a >>= 1;
        b = (b << 1) % MOD;
    }
    return res;
}
void primeFactors(long long n,vector<long long int>& kl)
{
    while (n%2 == 0)
    {
        kl.push_back(2);
        n = n/2;
    }
 
    for (long long i = 3; i <= sqrt(n); i = i+2)
    {
        while (n%i == 0)
        {
        kl.push_back(i);
            n = n/i;
        }
    }
 
    if (n > 2)
        kl.push_back(n);
}
int main()
{
    int start_s=clock();
    // the code you wish to time goes here
    
    //freopen("inpq.txt","r",stdin);
    //freopen("outputq.txt","w",stdout);
    long long K,NO;
    cin>>NO>>K;
    long long zzz=NO;
    vector< pair<long long,long long> > a;
    long long a1[NO];
    for(long long i=0;i<NO;i++)
    {
        long long t;
        cin>>t;
        a1[i]=t;
        a.push_back(make_pair(i,t));
    }
    vector<long long> pw;
    pw.push_back(1);
    for(long long j=2;j<=K;j++)
    {
        vector<long long > pr;
        primeFactors(j,pr);
        unordered_map<long long,long long> mp; 
        for(long long int i=0;i<pr.size();i++)
        {
            mp[pr[i]]++;
        }
        long long  mx=-1;
        for(long long int i=0;i<pr.size();i++)
        {
            mx=max(mx,mp[pr[i]]);
        }
        int te=0;
        for(long long int i=0;i<pr.size();i++)
        {
            if(mp[pr[i]]==mx)
                {
                    te=pr[i];
                    break;
                }

        }

      /* fill_n(p, MAXN+1, 0); 
       fill_n(q, MAXN+1, 0); 
    long long N=j;
    for(long long i=2;i<=lim;i++)
        if(N%i==0){
            p[sz]=i;
            while(N%i==0)
                {
                    N/=i;
                    q[sz]++;
                }
            sz++;
        }
    if(N>1){p[sz]=N; q[sz]=1; sz++;}
    long long ss = sizeof(p)/sizeof(p[0]);
    long long mx=-1;
    for(long long i=0;i<ss;i++)
    {
        mx=max(mx,q[i]);
    	//cout<<p[i]<<"^"<<q[i]<<"*";
    }
    long long te;
    for(long long i=0;i<ss;i++)
    {
        if(q[i]==mx)
        {
            te=p[i];
            break;
        }
    }*/
    pw.push_back(te);
}
cout<<"hi";
   /* for(long long i=0;i<pw.size();i++)
    {
        cout<<pw[i]<<" ";
    }*/

    //cout<<endl<<endl;
    cout<<"hi";
    sort(a1,a1+NO);
    deque<long long> dq;
    cout<<"hi";
    for(long long i=0;i<NO;i++)
    {
        dq.push_back(a1[i]);
    }
    cout<<"hi";
    for(long long i=1;i<=K;i++)
    {
        if(i==1 || ((pw[i-1]%i)%2!=0) )
        {
            long long int kk=dq.back();
            dq.pop_back();
            kk=mulmod(kk,2);
            dq.push_back(kk);
        }
        else
        {
            long long kk=dq.front();
            kk=kk/2;
            dq.pop_front();
            if(kk==0)
            {
                zzz--;
                continue;
            }
            else
            {
                dq.push_front(kk);
            }
        }
    }
    cout<<zzz<<endl;
    for (std::deque<long long>::iterator it = dq.begin(); it!=dq.end(); ++it)
    std::cout<< *it<<" ";

}