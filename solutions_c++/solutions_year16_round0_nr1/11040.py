/***********************************\
        BOXTROLL
        Sakibhossain.nstu@gmail.com
/************************************/
#include <bits/stdc++.h>
using namespace std;
#define ff first
#define ss second
#define vip(A) vector<pair<int,int> >A
#define ulta(A) reverse(all(A))
#define pai(A) pair<int,int>A
#define mkp(x,y) make_pair(x,y)
#define ll long long int
#define ull unsigned long long int
#define re(x) return x
#define repa(i,j) for(i=1;i<=j;i++)
#define rep(i,j) for( i=0;i<j;i++)
#define pob pop_back()
#define per(i,j) for(int i=j;i>=0;i--)
#define po(i,j) pow(i+0.0,j)
#define pb(x) push_back(x)
#define ppb(x,y) push_back(pair<int, int>(x,y))
#define pf printf
#define sf scanf
#define all(x) x.begin(), x.end()
#define clr(x) x.erase(all(x))
#define sum(x) accumulate(all(x),0)
#define vi(x) vector<int>x
#define vs(x) vector<string>x
#define fimax(A) max_element(all(A))
#define fimin(A) min_element(all(A))
#define ca(x) pf("Case %d: ",x)
#define show(A) for(int i=0;i<A.size();i++){cout<<A[i]<<endl;}
#define ok pf("ok\n")
#define SET(x) memset(x, 0, sizeof(x))
#define CLR(x) memset(x, -1, sizeof(x))
#define FAST ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
template <class T> T Max(T a, T b) { return a>b?a:b;}
template <class T> T Min(T a, T b) { return a<b?a:b;}
bool stb(const string &a,const string &b) ///sorting from small to big size///
{
    return a.size()<b.size();
}
bool bts(const string &a,const string &b)  ///sorting from big to small size///
{
    return a.size()>b.size();
}
bool pas(const pair< int,int > &a,const pair <int,int> &b) ///Sort by Second elements of Pair ///
{
    return a.ss<b.ss;
}
int A[10];
///Main Code Starting From Here///
int main()
{
SET(A);
FILE *in,*ou;
in=fopen("codin.txt","r");
ou=fopen("codou.txt","w");
long long int t,i,p,n,j;
fscanf(in,"%I64D",&t);
for(i=0;i<t;i++)
{
    SET(A);
    fscanf(in,"%I64D",&n);
    if(n==0)
    {
        fprintf(ou,"Case #%I64d: INSOMNIA\n",i+1);
    }
    else
    {
        int j=1;long long c,d;
        while(1)
        {
            c=n*j;
            d=c;
            while(c)
            {
                int r=c%10;
                A[r]=1;
                c/=10;
            }
            int s=A[0]+A[1]+A[2]+A[3]+A[4]+A[5]+A[6]+A[7]+A[8]+A[9];
            if(s==10)
                break;
            j++;
        }
        fprintf(ou,"Case #%I64d: %I64d\n",i+1,d);
    }
}
return 0;
}
///Never Give Up///

