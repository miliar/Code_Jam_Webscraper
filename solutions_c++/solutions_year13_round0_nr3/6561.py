/*************************************
******** Team : BUBT_HIDDEN **********
**************************************
*********** Shipu Ahamed *************
*************************************/

#include<algorithm>
#include<iostream>
#include<iterator>
#include<cassert>
#include<sstream>
#include<fstream>
#include<cstdlib>
#include<cstring>
#include<utility>
#include<complex>
#include<string>
#include<cctype>
#include<cstdio>
#include<vector>
#include<bitset>
#include<stack>
#include<queue>
#include<cmath>
#include<deque>
#include<list>
#include<set>
#include<map>

#define ll long long
#define sc scanf
#define pf printf
#define pi 2*acos(0.0)

#define ft first
#define se second
#define st(s) s.size();
#define intput freopen("in.txt","r",stdin)
#define output freopen("out.txt","w",stdout)
#define maxall(v) *max_element(v.begin(),v.end())
#define minall(v) *min_element(v.begin(),v.end())
#define Sort(v) sort(v.begin(),v.end())
#define un(v) Sort(v), v.erase(unique(v.begin(),v.end()),v.end())
#define cover(a,d) memset(a,d,sizeof(a))
using namespace std;
int pl(int p)
{
    int n=p;
    int s=0;
    while(n!=0)
    {
        s=s*10+(n%10);
        n/=10;
    }
    if(s==p)
    return 1;

    return 0;
}
int sq(int n)
{
    int c=sqrt(n);
    if(c*c==n)
    return 1;

    return 0;
}
int main()
{
//    intput;
//    output;
    int t,no=0;
    cin>>t;
    while(t--)
    {
        int a,b;
        cin>>a>>b;
        int c=0;
        for(int i=a;i<=b;i++)
        {
            if(pl(i))
            {
                if(sq(i))
                {
                    int s=sqrt(i);
                    if(pl(s))
                        c++;
                }
            }
        }
        pf("Case #%d: %d\n",++no,c);
    }

    return 0;
}

