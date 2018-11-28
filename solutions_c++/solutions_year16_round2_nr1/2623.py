#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector < long long > vll;
typedef unsigned long long ull;
typedef pair < long long,  long long > pll;
typedef pair < int,  int > pii;
typedef vector < int > vii;

#define ff first
#define ss second
#define sz size()
#define clr clear()
#define len length()
#define pb push_back
#define mp make_pair
#define finp cin.sync_with_stdio(0);cin.tie(0);
#define test int t;cin>>t;while(t--)
#define rep(i,n) for(int i=0;i<n;i++)
#define frep(i,a,b) for(int i=a;i<=b;i++)
#define brep(i,n) for(int i=n-1;i>0;i--)
#define fbrep(i,a,b) for(int i=a;i>=b;i--)

const int N = 1e5 + 500;
const ll mod = 1e9 + 7;
const ll INF = 1LL << 57LL;

//Fast expo

ll expo(ll a , ll b)
{
    if(b==0)
        return 1;
    else if(b%2==0)
        return expo(a*a,b/2);
    else
        return a*expo(a*a,b/2);
}

//comparing pair wrt to 2nd

/*bool compare2(const pii &i, const pii &j)
{
    return i.ss < j.ss;
}*/

int main()
{
    ifstream infile;
    ofstream outfile;
    infile.open("A-large.in");
    outfile.open("outfile.txt");
    int ca=1;
    finp
    int tt;
    infile>>tt;
    while(tt--)
    {
        string s;
        int a[10]={0};
        vii alpha(26);
        fill(alpha.begin(),alpha.end(),0);
        //cin>>s;
        infile>>s;
        int total=s.size();
        rep(i,s.size())
        {
            alpha[s[i]-'A']++;
        }
        if(alpha['Z'-'A'])
        {
            a[0]=alpha[25];
            alpha[25]=0;
            alpha['E'-'A']-=a[0];
            alpha['R'-'A']-=a[0];
            alpha['O'-'A']-=a[0];
            total-=4*a[0];
        }
        if(total && alpha['W'-'A'])
        {
            a[2]=alpha['W'-'A'];
            alpha['W'-'A']=0;
            alpha['T'-'A']-=a[2];
            alpha['O'-'A']-=a[2];
            total-=3*a[2];
        }
        if(total && alpha['X'-'A'])
        {
            a[6]=alpha['X'-'A'];
            alpha['X'-'A']=0;
            alpha['S'-'A']-=a[6];
            alpha['I'-'A']-=a[6];
            total-=3*a[6];
        }
        if(total && alpha['U'-'A'])
        {
            a[4]=alpha['U'-'A'];
            alpha['U'-'A']=0;
            alpha['F'-'A']-=a[4];
            alpha['O'-'A']-=a[4];
            alpha['R'-'A']-=a[4];
            total-=4*a[4];
        }
        if(total && alpha['F'-'A'])
        {
            a[5]=alpha['F'-'A'];
            alpha['F'-'A']=0;
            alpha['I'-'A']-=a[5];
            alpha['V'-'A']-=a[5];
            alpha['E'-'A']-=a[5];
            total-=4*a[5];
        }
        if(total && alpha['V'-'A'])
        {
            a[7]=alpha['V'-'A'];
            alpha['V'-'A']=0;
            alpha['S'-'A']-=a[7];
            alpha['N'-'A']-=a[7];
            alpha['E'-'A']-=2*a[7];
            total-=5*a[7];
        }
        if(total && alpha['O'-'A'])
        {
            a[1]=alpha['O'-'A'];
            alpha['O'-'A']=0;
            alpha['N'-'A']-=a[1];
            alpha['E'-'A']-=a[1];
            total-=3*a[1];
        }
        if(total && alpha['N'-'A'])
        {
            a[9]=alpha['N'-'A']/2;
            alpha['N'-'A']=0;
            alpha['I'-'A']-=a[9];
            alpha['E'-'A']-=a[9];
            total-=4*a[9];
        }
        if(total && alpha['G'-'A'])
        {
            a[8]=alpha['G'-'A'];
            alpha['G'-'A']=0;
            alpha['E'-'A']-=a[8];
            alpha['I'-'A']-=a[8];
            alpha['H'-'A']-=a[8];
            alpha['T'-'A']-=a[8];
            total-=5*a[6];
        }
        if(total)
        {
            a[3]=alpha['T'-'A'];
        }
        //cout<<"Case #"<<ca<<": ";
        outfile<<"Case #"<<ca<<": ";
        rep(i,10)
        {
            if(a[i])
            {
                rep(j,a[i])
                {
                    //cout<<i;
                    outfile<<i;
                }
            }
        }
        //cout<<endl;
        outfile<<endl;
        ca++;
    }
    return 0;
}
