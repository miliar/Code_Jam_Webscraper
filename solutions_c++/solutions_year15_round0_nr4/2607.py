#include <bits/stdc++.h>
#define INF         0x7fffffff
#define ull         unsigned long long
#define ll          long long
#define vi          vector <ll>
#define pii         pair <ll,ll>
#define pb          push_back
#define NUM(x)      x-'0'
#define TEST        ll t,T;cin>>T;for(t=1;t<=T&&cout<<"Case #"<<t<<": ";t++)
#define X           first
#define Y           second

using namespace std;


int main()
{
    ios_base::sync_with_stdio(0);
    freopen("input.in","r",stdin);
    //freopen("output.out","w",stdout);

    TEST
    {

    int x, r, c;
    bool f;
    cin>>x>>r>>c;

    if(r>c)swap(r,c);

    if(((r*c)%x)||(x>c))
    {
        cout<<"RICHARD"<<endl;
        continue;
    }
    if(r<=x-2)
    {
        cout<<"RICHARD"<<endl;
        continue;
    }
    else
        cout<<"GABRIEL"<<endl;
    }

}
