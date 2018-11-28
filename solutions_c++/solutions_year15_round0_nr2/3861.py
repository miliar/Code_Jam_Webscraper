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
LL calc(vector<LL> v,LL n)
{
    LL i,flag=0,k;
    vector<LL> v1=v;LL maxi=INT_MIN;
    loop(i,n)
    {
        if(v[i]>0)
        {
            v1[i]=v[i]-1;
            flag=1;
        }
        if(maxi<v[i])
        {
            maxi=v[i];
            k=i;
        }
    }
    if(flag==0)
        return 0;
    else if(maxi==1)
       return 1;
    else if(maxi==2)
    {
        v[k]=1;
        v.push_back(1);
        return 1+min(calc(v1,n),calc(v,n+1));
    }
    else if(maxi==3)
    {
        v[k]=1;
        v.push_back(2);
        return 1+min(calc(v1,n),calc(v,n+1));
    }
    else if(maxi==4)
    {
        v[k]=2;
        v.push_back(2);
        return 1+min(calc(v1,n),calc(v,n+1));
    }
    else if(maxi==5)
    {
        v[k]=2;
        v.push_back(3);
        return 1+min(calc(v1,n),calc(v,n+1));
    }
    else if(maxi==6)
    {
        v[k]=3;
        v.push_back(3);
        return 1+min(calc(v1,n),calc(v,n+1));
    }
    else if(maxi==7)
    {
        v[k]=3;
        v.push_back(4);
        return 1+min(calc(v1,n),calc(v,n+1));
    }
    else if(maxi==8)
    {
        v[k]=4;
        v.push_back(4);
        return 1+min(calc(v1,n),calc(v,n+1));
    }
    else if(maxi==9)
    {
        v[k]=3;
        v.push_back(6);
        return 1+min(calc(v1,n),calc(v,n+1));
    }
}
int main()
{
    std::ios::sync_with_stdio(false);
    LL i,j,t,k=0,l,n,x,y,ans;
    cin>>t;
    while(t--)
    {
        k++;
        cin>>n;
        vector<LL> v;
        loop(i,n)
        {
            cin>>l,v.push_back(l);
        }
         cout<<"Case #"<<k<<": "<<calc(v,n)<<endl;
    }
    return 0;
}

