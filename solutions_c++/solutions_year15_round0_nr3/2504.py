/**
                                                ooooooo
                                                o         ooooooo   ooooooo   o ooooo  ooooooo
                                                ooooooo    oooooo    oooooo    o    o  o
                                                      o    o    o    o    o    o    o  o
                                                ooooooo    ooooooo   ooooooo   o    o  ooooooo
*/

#include<bits/stdc++.h>
using namespace std;
#define loop(i,n) for(i=0;i<n;i++)
#define loop1(i,n) for(i=1;i<=n;i++)
#define loop3(i,n,k) for(i=n;i<=k;i++)
#define loopr(i,n,k) for(i=n;i>=k;i--)
#define pvn(n) cout<<n<<"\n"
#define pvw(n) cout<<n<<" "
#define pvpn(n,x) cout<< std::fixed;cout<< std::setprecision(x)<<n<<"\n"
#define pvpw(n,x) cout<< std::fixed;cout<< std::setprecision(x)<<n<<" "
#define pw cout<<" "
#define pn cout<<"\n"
#define TZ(n) __builtin_ctz(n)
#define LZ(n) __builtin_clz(n)
#define CSB(n) __builtin_popcount(n)

#define MAX 1000000007
#define pi  3.1415926535
#define exp  2.7182818284

typedef long long int LL;
typedef long int L;
typedef double D;
typedef unsigned long long int ULL;
typedef vector<LL> VLL;
typedef vector<L> VL;
typedef vector<int> VI;
typedef vector<char> VC;
typedef vector<string> VS;
typedef vector<float> VF;
typedef vector<double> VD;
typedef pair<LL,LL> PLL;

const LL INF=1000000000;
LL mul[5][5]={{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
string s,ori;
LL decode(char p)
{
    if(p=='i')
        return 2;
    else if(p=='j')
        return 3;
    else
        return 4;
}

int main()
{
    std::ios::sync_with_stdio(false);
    LL i,j,t,k=0,l,n,x,y,ans;
    cin>>t;
    while(t--)
    {
        ori.clear();
        k++;
        bool flag0=0,flag1=0,flag2=0;
        cin>>l>>x>>s;
        n=l*x;
        ori.resize(n+1);
        loop(i,n)
        ori[i]=s[i%l];
        i=0;
        ans=1;
        while(i<n)
        {
            if(ans<0)
                ans=(-1)*mul[abs(ans)][decode(ori[i])];
            else
                ans=mul[ans][decode(ori[i])];
            if(ans==2&&(!flag0)&&(!flag1)&&(!flag2))
            {
                flag0=1;
                ans=1;
            }
            if(ans==3&&(flag0)&&(!flag1)&&(!flag2))
            {
                flag1=1;
                ans=1;
            }
            if(ans==4&&(flag0)&&(flag1)&&(!flag2)&&i==n-1)
            {
                flag2=1;
            }
            i++;
        }
        if(flag0&&flag1&&flag2)
            cout<<"Case #"<<k<<": YES"<<endl;
        else
            cout<<"Case #"<<k<<": NO"<<endl;
    }
    return 0;
}
