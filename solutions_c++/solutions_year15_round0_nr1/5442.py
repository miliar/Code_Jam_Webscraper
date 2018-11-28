#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define READ(filename)  freopen(filename, "r", stdin);
#define WRITE(filename)  freopen(filename, "w", stdout);
#define aov(a) a.begin(),a.end()
#define LB(a,x) (lower_bound(aov(a),x)-a.begin())
#define UB(a,x) (upper_bound(aov(a),x)-a.begin())
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)

template <class T> inline T bigmod(T p,T e,T M)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    }
    return (T)ret;
}
template <class T> inline T gcd(T a,T b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}
template <class T> inline T modinverse(T a,T M)
{
    return bigmod(a,M-2,M);    // M is prime
}
template <class T> inline T bpow(T p,T e)
{
    ll ret = 1;
    for(; e > 0; e >>= 1)
    {
        if(e & 1) ret = (ret * p);
        p = (p * p);
    }
    return (T)ret;
}

int toInt(string s)
{
    int sm;
    stringstream ss(s);
    ss>>sm;
    return sm;
}
int toLlint(string s)
{
    long long int sm;
    stringstream ss(s);
    ss>>sm;
    return sm;
}

///int month[]={-1,31,28,31,30,31,30,31,31,30,31,30,31};  //Not Leap Year
///int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
///int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int dx[]={-1,-1,+0,+1,+1,+0};int dy[]={-1,+1,+2,+1,-1,-2}; //Hexagonal Direction
///const double eps=1e-6;

int main()
{
    READ("codejam.txt");
    WRITE("codejam1.txt");

    int test,n,sum,cnt;
    string s1;
    sc(test);
    for(int kase=1;kase<=test;kase++)
    {
        sum=0,cnt=0;
        sc(n);
        cin>>s1;
        if(n==0) cout<<"Case #"<<kase<<": 0"<<endl;
        else
        {
            sum=sum+s1[0]-'0';

            for(int i=1;i<=n;i++)
            {
                if(i>sum)
                {
                    cnt+=(i-sum);

                    sum=sum+(i-sum)+s1[i]-'0';
                }
                else
                {
                    sum=sum+s1[i]-'0';
                }
            }
            cout<<"Case #"<<kase<<": "<<cnt<<endl;
        }

    }
    return 0;
}
