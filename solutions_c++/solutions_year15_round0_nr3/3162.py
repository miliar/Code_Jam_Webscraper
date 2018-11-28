#include<bits/stdc++.h>
#define F first
#define S second
#define mp(x,y) make_pair(x,y)
#define popb(x) pop_back(x)
#define pushb(x) push_back(x)
#define popf(x) pop_front(x)
#define pushf(x) push_front(x)
#define ALL(x) x.begin(),x.end()
#define INIT(x,y) memset(x,y,sizeof x)
#define fori(x,y) for(i=x;i<y;i++)
#define forj(x,y) for(j=x;j<y;j++)
#define INF 1e9
#define EPS 1e-9
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
ll n,x;
string s;
int mul(int a,int b)
{
    if(a==1)return b;
    if(a==5)return b+4;
    if(a==2)
    {
        if(b==2)return 5;
        if(b==3)return 4;
        if(b==4)return 7;
    }
    if(a==3)
    {
        if(b==2)return 8;
        if(b==3)return 5;
        if(b==4)return 2;
    }
    if(a==4)
    {
        if(b==2)return 3;
        if(b==3)return 6;
        if(b==4)return 5;
    }
    if(a==6)
    {
        if(b==2)return 1;
        if(b==3)return 8;
        if(b==4)return 3;
    }
    if(a==7)
    {
        if(b==2)return 4;
        if(b==3)return 1;
        if(b==4)return 6;
    }
    if(a==8)
    {
        if(b==2)return 7;
        if(b==3)return 2;
        if(b==4)return 1;
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w+",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,tt,i,sta,temp;
    cin>>tt;
    for(t=1;t<=tt;t++)
    {
        cin>>n>>x>>s;
        sta=1;
        temp='i';
        for(i=0;i<n*x;i++)
        {
            sta=mul(sta,s[i%n]-'i'+2);
            if(temp==sta+'i'-2)
            {
                temp++;
                sta=1;
                if(temp=='l')break;
            }
        }
        //cout<<"               "<<temp-'i'<<endl;
        for(i++;i<n*x;i++)sta=mul(sta,s[i%n]-'i'+2);
        if(temp=='l'&&sta==1)cout<<"Case #"<<t<<": YES\n";
        else cout<<"Case #"<<t<<": NO\n";
    }
    return 0;
}
