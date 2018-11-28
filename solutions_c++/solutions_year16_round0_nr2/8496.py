#include<bits/stdc++.h>
using namespace std;
#define fs first
#define sc second
#define p 1000000007
#define pb push_back
#define mp make_pair
typedef long long Int;
typedef pair<Int,Int> pii;
typedef vector<Int> vi;
typedef vector<pii> vii;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
    Int T;
    cin>>T;
    for (Int k=1;k<=T;++k)
    {
        Int ans=0;
        string S,A;
        cin>>A;
        S.pb(A[0]);
        for (Int i=1;i<A.size();++i)
        {
            if (A[i]==A[i-1])
                continue;
            S.pb(A[i]);
        }
        if (S[0]=='-')
            ans+=1;
        for (Int i=1;i<S.size();++i)
        {
            if (S[i]=='-')
                ans+=2;
        }
        cout<<"Case #"<<k<<": ";
        cout<<ans<<"\n";
    }
    return 0;
}
