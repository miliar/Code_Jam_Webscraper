#include<bits/stdc++.h>
using namespace std;
#define     ll                      long long
#define     ull                     unsigned long long
#define     mems(a,b)               memset(a,b,sizeof(a))
#define     mp                      make_pair
#define     pii                     pair<int,int>
#define     pdd                     pair<double,double>
#define     fs                      first
#define     sc                      second
#define     VI                      vector<int>
#define     clr(a)                  a.clear()
#define     pb                      push_back
#define     eps                     1E-5
#define     sf                      scanf
#define     pf                      printf
#define     all(a)                  a.begin(),a.end()
#define     fread(name)             freopen(name,"r",stdin)
#define     fwrite(name)            freopen(name,"w",stdout)
#define     sz(a)                   (int)a.size()
#define     cone                    __builtin_popcountll
#define     fastIO                  ios_base::sync_with_stdio(false)
#define     cintie                  cin.tie(NULL)
#define     endl                    "\n";
#define     PI                      (acos(-1.0))
#define     linf                    (1LL<<62)
#define     inf                     (0x7f7f7f7f)
#define     sqr(a)                  ((a)*(a))
#define     lcm(a,b)                ({(a)/__gcd(a,b)*(b);})
#define     is_set(mask,pos)        ((mask)&(1LL<<pos))
#define     rset(mask,pos)          ((mask)&(~(1LL<<pos)))
#define     set(mask,pos)           ((mask)|(1LL<<pos))
#define     flip(mask,pos)          ((mask)^(1LL<<pos))
#define     debv(v)                 for(int i=0;i<sz(v);++i)(!i?cout<<v[i]:cout<<" "<<v[i]);cout<<endl;
#define     deba(arr,l)             for(int i=0; i<l; i++)(!i?cout<<arr[i]:cout<<" "<<arr[i]);cout<<endl;
#define     deb(a...)               {cerr<<"#"<<__LINE__<<" -> ";dbg,a; cerr<<endl;}
struct debugger { template<typename T> debugger& operator , (const T v) { cerr<<v<<" "; return *this; } } dbg;

///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//int X[]={1,1,2,2,-1,-1,-2,-2},Y[]={2,-2,1,-1,2,-2,1,-1};
//int X[]={0,-1,-1,-1,0,1,1,1},Y[]={-1,-1,0,1,1,1,0,-1};
//int X[]={-1,0,1,0},Y[]={0,1,0,-1};
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//int bigMod(int a,int x,int p){int r=1;while(x>0){if(x%2!=0){r=(r*a)%p;}a=(a*a)%p;x=(x>>1);}return r;}
//int modInverse(int a, int p){return bigMod(a,p-2,p);}
//int extGcd(int a,int b,ll& x,ll& y){if(b==0){x=1;y=0;return a;}else{int g=extGcd(b,a%b,y,x);y-=a/b*x;return g;}}
//template<class T> T pwr(T b, T p){T r=1,x=b;while(p){if(p&1)r*=x;x*=x;p=(p>>1);}return r;}
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//struct triple{double f,s,t;triple() {} triple(double a,double b,double c){f=a,s=b,t=c;}};
//int cross_product(triple a,triple b){int v=a.f*(b.s-b.t)-a.s*(b.f-b.t)+a.t*(b.f-b.s);return (v==0?0:(v>0?+1:-1));}
//triple make_vector(triple s,triple e){triple a;a.f=e.f-s.f;a.s=e.s-s.s;a.t=e.t-s.t;return a;}
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//double pdis(pdd a,pdd b){return sqrt((double)sqr(a.fs-b.fs)+sqr(a.sc-b.sc));}
//template<class T> double rAng(T a,T b,T c){double d=(sqr(a)+sqr(b)-sqr(c))/(a*b*2);d=(d<-1?-1:(d>1?1:d));return acos(d);}
///~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//template<class T> string to_string(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
//int to_int(string s){int r=0;istringstream sin(s);sin>>r;return r;}
///HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
#define LM 2007
char line[LM];
map<char,int>frq;

string str[] =  {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int count(string ss,char c)
{
    int ans = 0;
    for(int i = 0;i<ss.size();++i)
    {
        if(ss[i]==c)ans++;
    }
    return ans;
}

int main()
{
    fread("input.in");
    fwrite("output.out");
    int T,t=1;
    sf("%d",&T);

    while(T--)
    {
        frq.clear();
        sf(" %s",line);
        int l = strlen(line);
        for(int i=0;i<l;++i)
        {
            frq[line[i]]++;
        }

        string ans = "";


        pf("Case #%d: ",t++);

        while(frq['Z']>0)
        {
            ans+="0";
            for(int i=0;i<str[0].size();++i)
            {
                frq[str[0][i]]--;
            }
        }


        while(frq['X']>0)
        {
            ans+="6";
            for(int i=0; i<str[6].size(); ++i)
            {
                frq[str[6][i]]--;
            }
        }

        while(frq['S']>0)
        {
            ans+="7";
            for(int i=0; i<str[7].size(); ++i)
            {
                frq[str[7][i]]--;
            }
        }

        while(frq['V']>0)
        {
            ans+="5";
            for(int i=0; i<str[5].size(); ++i)
            {
                frq[str[5][i]]--;
            }
        }


        while(frq['F']>0)
        {
            ans+="4";
            for(int i=0; i<str[4].size(); ++i)
            {
                frq[str[4][i]]--;
            }
        }

        while(frq['R']>0)
        {
            ans+="3";
            for(int i=0; i<str[3].size(); ++i)
            {
                frq[str[3][i]]--;
            }
        }

        while(frq['W']>0)
        {
            ans+="2";
            for(int i=0; i<str[2].size(); ++i)
            {
                frq[str[2][i]]--;
            }
        }

        while(frq['W']>0)
        {
            ans+="2";
            for(int i=0; i<str[2].size(); ++i)
            {
                frq[str[2][i]]--;
            }
        }

        while(frq['O']>0)
        {
            ans+="1";
            for(int i=0; i<str[1].size(); ++i)
            {
                frq[str[1][i]]--;
            }
        }

        while(frq['N']>0)
        {
            ans+="9";
            for(int i=0; i<str[9].size(); ++i)
            {
                frq[str[9][i]]--;
            }
        }

        while(frq['E']>0)
        {
            ans+="8";
            for(int i=0; i<str[8].size(); ++i)
            {
                frq[str[8][i]]--;
            }
        }

        sort(ans.begin(),ans.end());

        printf("%s\n",ans.c_str());

    }

    return 0;
}
