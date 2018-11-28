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
int freq[10];
int mini=9999;
void call(int i,int j)
{

    if(i==0)
    {
        return ;
    }

    if(freq[i]==0)
    {
        call(i-1,j);
        return ;
    }

    mini=min(mini,j+i);
    for(int k=1; k<i; k++)
    {
        freq[k]+=freq[i];
        freq[i-k]+=freq[i];
        call(i-1,j+freq[i]);
        freq[k]-=freq[i];
        freq[i-k]-=freq[i];
    }
}


int main()
{
    READ("codejam23.txt");
    WRITE("codejam2.txt");
    int test;
    cin>>test;
    for(int kase=1; kase<=test; kase++)
    {
        int d,p;

        sc(d);
        memset(freq,0,sizeof(freq));

        for(int i=1; i<=d; i++)
        {
            sc(p);
            freq[p]++;
        }

        call(9,0);
        cout<<"Case #"<<kase<<": "<<mini<<endl;
        mini=9999;
    }
   return 0;
}

