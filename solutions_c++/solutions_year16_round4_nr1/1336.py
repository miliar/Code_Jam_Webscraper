//#define WYTE
#include<bits/stdc++.h>
#define X first
#define Y second
#define mp(x,y) make_pair((x),(y))
#define pb(x) push_back(x)
#define ALL(x) (x).begin(),(x).end()
#define INIT(x,y) memset((x),(y),sizeof(x))
#define PQ priority_queue
#define IT iterator
#define INF 1e9
#define EPS 1e-9
#define MOD 1000000007
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

int n,r,p,s;
string gen(string start)
{
    string v=start;
    while(v.size()!=(1<<n))
    {
        string tmp="";
        for(int i=0;i<v.size();i++)
        {
            if(v[i]=='R')
            {
                tmp+='R';
                tmp+='S';
            }
            else if(v[i]=='P')
            {
                tmp+='P';
                tmp+='R';
            }
            else
            {
                tmp+='S';
                tmp+='P';
            }
        }
        v=tmp;
    }
    return v;
}
bool valid(string x)
{
    int R=0,P=0,S=0,i;
    for(i=0;i<x.size();i++)
    {
        if(x[i]=='R')R++;
        else if(x[i]=='P')P++;
        else S++;
    }
    return R==r&&P==p&&S==s;
}
string part(string x,int st,int ed)
{
    string res="";
    for(int i=st;i<=ed;i++)
    {
        res+=x[i];
    }
    return res;
}
void cpy(string &source,string &dest,int idx)
{
    for(int i=0;i<source.size();i++)
    {
        dest[i+idx]=source[i];
    }
}
string eiei(string x)
{
    int ii,i;
    for(ii=1;ii<=n;ii++)
    {
        for(i=0;i<x.size();i+=(1<<ii))
        {
            //i->i+(1<<ii)-1
            string a,b;
            a=part(x,i,i+(1<<(ii-1))-1);
            b=part(x,i+(1<<(ii-1)),i+(1<<ii)-1);
            if(b<a)
            {
                cpy(b,x,i);
                cpy(a,x,i+(1<<(ii-1)));
            }
        }
    }
    return x;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t,ii;
    cin>>t;
    for(ii=1;ii<=t;ii++)
    {
        cin>>n>>r>>p>>s;
        cout<<"Case #"<<ii<<": ";
        string x;
        vector<string> v;
        x=gen("R");
        if(valid(x))
        {
            v.pb(eiei(x));
        }
        x=gen("P");
        if(valid(x))
        {
            v.pb(eiei(x));
        }
        x=gen("S");
        if(valid(x))
        {
            v.pb(eiei(x));
        }
        if(v.size()==0)
        {
            cout<<"IMPOSSIBLE\n";
        }
        else
        {
            sort(ALL(v));
            cout<<v[0]<<"\n";
        }
    }
}
