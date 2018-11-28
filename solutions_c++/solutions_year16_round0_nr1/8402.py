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
    freopen("A-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
    Int T;
    cin>>T;
    for (Int k=1;k<=T;++k)
    {
        Int N,temp,i;
        cin>>N;
        set<Int>S;
        for (i=1;i<=1000;++i)
        {
            temp=i*N;
            while (temp!=0)
            {
                S.insert(temp%10);
                temp=temp/10;
            }
            if (S.size()==10)
                break;
        }
        cout<<"Case #"<<k<<": ";
        if (S.size()==10)
            cout<<i*N<<"\n";
        else
            cout<<"INSOMNIA\n";
    }
    return 0;
}
