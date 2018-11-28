#include <bits/stdc++.h>
#define ll long long
using namespace std;
vector<vector<long long> >ans;
vector<string> anss;
//vector<vector<long long> > ansn;
ll gcd(ll x,ll y){return !y?x:gcd(y,x%y);}
ll mul_mod(ll x,ll y,ll k){
    x%=k,y%=k;
    ll res=0;
    while(y){
        if(y&1){
            res+=x;
            if(res>=k)res-=k;
        }
        x+=x,y>>=1;
        if(x>=k)x-=k;
    }
    return res;
}
ll pow_mod(ll x,ll y,ll k){
    ll res=1;
    while(y){
        if(y&1)res=mul_mod(res,x,k);
        x=mul_mod(x,x,k),y>>=1;
    }
    return res;
}
ll witness(ll a,ll b,ll c){
    if(b==0)return 1;
    ll x,y,t=0;
    while((b&1)==0)
        b>>=1,t++;
    y=x=pow_mod(a,b,c);
    while(t--){
        y=mul_mod(x,x,c);
        if(y==1 && x!=1 && x!=c-1)
            return false;
        x=y;
    }
    return y==1;
}
bool miller_rabin(ll n) {//..质数为true, 非质数为false..
    if(n==2)return true;
    if(n<2 || (n&1)==0)return false;
    for(int i=0;i<3;i++)
        if(witness(rand()%(n-2)+2,n-1,n)!=1)
            return false;
    return true;
}
ll pollard_rho(ll n,ll c = 240){//..随机返回一个 n 的约数..
    if(n%2==0)return 2;
    ll i=1,k=2,x=rand()%n,y=x,d;
    while(1){
        i++;
        x=(mul_mod(x,x,n)+c)%n;
        d=gcd(y-x,n);
        if(d==n)return n;
        if(d!=n && d>1)return d;
        if(i==k) y=x,k<<=1;
    }
}
void dfs(string &s,int k,int n)
{
    if((int)ans.size() == n) return;
    if(k == (int)s.length() - 1)
    {
        bool flag = true;
        vector<long long> tmp;
        //vector<long long> tmpn;
        for(int j = 2; j <= 10; j++)
        {
            long long num = 0;
            long long t = 1;
            for(int i = s.length() - 1; i >= 0; i--)
            {
                if(s[i] == '1')
                    num += t;
                t *= j;
            }
            if(miller_rabin(num))
            {
                flag = false;
                break;
            }
            else
            {
                tmp.push_back(pollard_rho(num));
                //tmpn.push_back(num);
            }
        }
        if(flag)
        {
            ans.push_back(tmp);
            anss.push_back(s);
            //ansn.push_back(tmpn);
        }
        return ;
    }
    dfs(s,k + 1,n);
    s[k] = s[k] == '0' ? '1' : '0';
    dfs(s,k + 1,n);
}
int main()
{
    freopen("C-small-attempt3.in", "r", stdin);
    freopen("C-small-attempt3.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        string s1 = "";
        for(int i = 0; i < n; i++)
            s1 += "1";
        dfs(s1,1,m);
        printf("Case #%d:\n",cas);
        for(int i = 0 ; i < m; i++)
        {
            cout<<anss[i]<<" ";
            for(int j = 0; j < (int)ans[i].size(); j++)
                cout<<ans[i][j]<<" ";
            cout<<endl;
        }
    }
    return 0;
}
