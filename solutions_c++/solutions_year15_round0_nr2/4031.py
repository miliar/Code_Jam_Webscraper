
//Author : Ujjawal Dixit  , ABV-IIITM
//Task : GCA QUESTION 3

#include <bits/stdc++.h>
#define MOD 1000000007
#define MAX 1e9
#define MIN -1e9
using namespace std;
typedef double ld;
typedef long long ll;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define getcx getchar
#define FOR(i,n,m) for(int i=0;i<n;i+=m)
#define For(i,n,m) for(int i=1;i<=n;i+=m)
#define max(a,b)    (a>=b?a:b)
//#define min(a,b)    (a<b?a:b)
#define countbits(num)   __builtin_popcount(num)
#define countbitsll(num)   __builtin_popcountll(num)
#define s(a) scanf("%d",&a)
#define sll(a) scanf("%lld",&a)
#define p(a) printf("%d",a)
#define f(i,a,b) for(int i=a;i<b;i++)
#define pll(a) printf("%lld",a)
#define pln()  printf("\n")
#define getstr(in) getline(cin,in)
#define getc() getchar()
#define uj() int t; scanf("%d",&t); while(t--)
template<typename T> T gcd(T a, T b) {
    if(!b) return a;
    return gcd(b, a % b);
}
template<typename T> T lcm(T a, T b) {
    return a * b / gcd(a, b);
}
inline void in(int &n)
{
    n=0; int ch = getcx(); int sign = 1;
    while(ch < '0' || ch > '9') { if(ch == '-') sign=-1; ch = getcx(); }
    while(ch >= '0' && ch <= '9') { n = (n << 3) + (n << 1) + ch - '0', ch = getcx(); }
    n = n * sign;
}

int Size,arr[1003];
int Fsize,frr[1003];
bool func(int special,int mid)
{
    //printf("sp and mid are %d %d\n",special,mid);
    Fsize=0;
    for(int i=1; i<=Size; i++)
    {
        if(arr[i]<=mid)
        {
            //ok...all pancakes can be finished within "mid" minutes
        }
        else if(arr[i]>mid)
        {
            //To be transferred
            int diff=arr[i]-mid;
            Fsize++;
            frr[Fsize]=diff;
            //printf("pushing %d\n",diff);
        }
    }
    int idx=1;
    while( idx<=Fsize )
    {
        if(frr[idx]>0 && special==0)
        {
            return false;
        }
        if(mid>=frr[idx])
        {
            idx++;
            special--;
            //you have done this part
        }
        else
        {
            frr[idx]-=mid;
            special--;
        }
    }
    return true;
}
int main()
{
    int t,D,P,c;
    in(t);//scanf("%d",&t);
    c=0;
    while(t--)
    {
        c++;
        Size=0;
        in(D);//scanf("%d",&D);
        for(int i=1; i<=D; i++)
        {
            in(P);//scanf("%d",&P);
            Size++;
            arr[Size]=P;
        }
        int ans=1000006;
        bool fnd;
        for(int special=0; special<=1000; special++)
        {
            int low=1;
            int up=1000;
            int mid;
            while(low<up)
            {
                mid=low+(up-low)/2;

                //Can mid be my answer ie can we have atmost "mid" non special minutes
                fnd=func(special,mid);
                //printf("special is %d mid is %d and fnd is %d\n",special,mid,fnd);
                if(fnd==false)
                {
                    low=mid+1;
                }
                else
                {
                    up=mid;
                }
            }//EndOfBinarySearch
            //printf("special %d low %d\n",special,low);
            if(special+low<ans)
            {
                ans=special+low;
            }
        }//EndOfSpecialLoop
        printf("Case #%d: %d\n",c,ans);
        //write<<"Case #"<<c<<": "<<ans<<"\n";
    }
    return 0;
}
  