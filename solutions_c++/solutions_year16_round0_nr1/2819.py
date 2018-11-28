#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define mod 1000000007
#define reset(s,val) memset(s,val,sizeof(s))
#define eps 1e-9
#define pi acos(-1)
#define sqr(x) (x)*(x)
#define two(x) (1<<(x))

int n,t,vst[10],cnt;

void f(int x)
{
    int k;
    while(x)
    {
        k=x%10;
        x/=10;
        if(!vst[k])
        {
            vst[k]=1;
            cnt--;
        }
    }
}

int main( ){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin>>t;
    For(cas,1,1+t)
    {
        cout<<"Case #"<<cas<<": ";
        cnt=10;
        reset(vst,0);
        cin>>n;
        if(!n)
        {
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        bool flag=false;
        For(i,1,1000)
        {
            f(n*i);
            if(!cnt)
            {
                cout<<n*i<<endl;
                flag=true;
                break;
            }
        }
        if(!flag) cout<<"INSOMNIA"<<endl;
    }
}
