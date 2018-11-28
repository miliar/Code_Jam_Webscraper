#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>

using namespace std;
#define For(a,b,c) for(a = b;a < c; a++)
#define rep(a,b) for(int a=0;a<b;a++)
typedef vector<double> vi;

int main()
{
    freopen ("D-large.in","r",stdin);
    freopen ("data.out","w",stdout);
    int t,n,aux1,aux2,res;
    cin>>t;
    double v1[1001],v2[1001];
    rep(T,t)
    {
        cout<<"Case #"<<T+1<<": ";
        cin>>n;
        rep(i,n) scanf("%lf",&v1[i]);//naomi´s
        rep(i,n) scanf("%lf",&v2[i]);//ken's
        sort(v1,v1+n);
        sort(v2,v2+n);
//        rep(i,n) cout<<v1[i]<<" ";
//        cout<<endl;
//        rep(i,n) cout<<v2[i]<<" ";
//        cout<<endl;
        aux2 = 0;
        res = 0;
        rep(i,n)
        {
            if(v1[i] > v2[aux2])
            {
                res++;
                aux2++;
            }
        }
        cout<<res<<" ";
        res = 0;
        aux1 = 0;
        aux2 = n-1;
        for(int i=n-1;i>=0;i--)
        {
            if(v1[i] > v2[aux2])
            {
                aux1++;
                res++;
            }
            else
            {
                aux2--;
            }
        }
        cout<<res<<endl;
    }
}
