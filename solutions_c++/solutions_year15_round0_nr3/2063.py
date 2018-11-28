/*
 Problem name :
 Algorithm : Not Sure Yet
 Contest/Practice :
 Source :
 Comment : Whenever you start to believe  yourself, people also start to believe in you
 Date : --
 Last Update : 25-Mar-2015
*/

/*
"
    তোমার জন্যে পাপ করব
.................................

    ভাবছি,
    সজ্ঞানে তোমার সাথে আমি একটা পাপ করবো।
    জানতে চাও কেনো?
    তাহলে আমাকে আর স্বর্গে যেতে হবে না;
    স্বর্গে গেলেই তো পড়বো হুরপরীদের খপ্পরে।
    তুমিতো জানোই আমি মানুষ,
    ওদের ঐ ভীষণ রূপ
    আমাকে ভাসিয়ে নিয়ে যাবে
    তোমার থেকে দূরে, অনেক দূরে।
    তারচেয়ে বরং নরকের আগুনে অনন্তকাল জ্বলতে জ্বলতে
    তোমাকে যদি মিস করি,
    তোমার কাছে কি সেটাই বেশি রোমান্টিক নয়?
    তাই ভাবছি এবার সত্যি সত্যি তোমার সাথে একটা পাপ করবো ।
*/

#include<bits/stdc++.h>

#define pause           system("pause");
#define FOR(s,e,inc)    for(int i=s;i<=e;i+=inc)
#define mod             1000000007
#define inf             1<<30
#define pb              push_back
#define ppb             pop_back
#define F               first
#define S               second
#define sz(x)           ((int)x.size())
#define sqr(x)          ( (x)* (x) )
#define eps             1e-9
#define lcm(x,y)        (abs(x) /gcd(x,y))* abs(y)
#define on(x,w)         x|(1<<w)
#define check(x,w)      (x&(1<<w))
#define all(x)          (x).begin(),(x).end()
#define pf              printf
#define pi              acos(-1.0)
#define reset(x,v)      memset(x,v,sizeof(x));
#define AND             &&
#define OR              ||
#define what_is(x)      cerr<<#x<<" is "<<x<<"\n";

typedef long long ll;
typedef unsigned long long llu;

using namespace std;


template<class T>
inline T mod_v(T num)
{
    if(num>=0)
        return num%mod;
    else
        return (num%mod+mod)%mod;
}
template<class T>
inline T gcd(T a,T b)
{
    a=abs(a);
    b=abs(b);

    while(b)
    {
        a=a%b;
        swap(a,b);
    }

    return a;
}

template<class T>
T fast_pow(T n , T p)
{
    if(p==0) return 1;
    if(p%2)
    {
        T g=mod_v ( mod_v(n) * mod_v(fast_pow(n,p-1)) );
        return g;
    }
    else
    {
        T g=fast_pow(n,p/2);
        g=mod_v( mod_v(g) * mod_v(g) ) ;
        return g;
    }
}

template<class T>
inline T modInverse(T n)
{
    return fast_pow(n,mod-2);
}

template<class T>
inline void debug(string S1,T S2,string S3)
{
    cout<<S1<<S2<<S3;
}

bool equalTo ( double a, double b ){ if ( fabs ( a - b ) <= eps ) return true; else return false; }
bool notEqual ( double a, double b ){if ( fabs ( a - b ) > eps ) return true; else return false; }
bool lessThan ( double a, double b ){ if ( a + eps < b ) return true; else return false; }
bool lessThanEqual ( double a, double b ){if ( a < b + eps ) return true;   else return false;}
bool greaterThan ( double a, double b ){if ( a > b + eps ) return true;else return false;}
bool greaterThanEqual ( double a, double b ){if ( a + eps > b ) return true;else return false;}


template<class T>
inline T in()
{
    register char c=0;
    register T num=0;
    bool n=false;
    while(c<33)c=getchar();
    while(c>33){
        if(c=='-')
            n=true;
        else num=num*10+c-'0';
        c=getchar();
    }
    return n?-num:num;
}

/******* ! Code start from here ! *******/



map<pair<string,string>,string>mp;

string s;
bool got;

int dp[10009][5][2][130];
int done[10009][5][2][130]={0};

int cross[5][5]=
{ 0,0,0,0,0,
  0,1,2,3,4,
  0,2,-1,4,-3,
  0,3,-4,-1,2,
  0,4,3,-2,-1
};
int cc=1;


int re(int p,int c,int d,int v)
{
  //  printf("%d %d %d %d\n",p,c,d,v);pause
    if(p==sz(s)+1)
    {
        if(c==3)
        {
            return 1;
        }
        return 0;
    }
    if(c==3)
    {
        return 0;
    }


    if(done[p][c][d][v]==cc) return dp[p][c][d][v];

    done[p][c][d][v]=cc;

    dp[p][c][d][v]=0;

    if(c==0 && v==2 && !d)
        dp[p][c][d][v]=max(dp[p][c][d][v],re(p+1,c+1,0,s[p]-'0')) ;
    else if(c==1 && v==3 && !d)
        dp[p][c][d][v]=max(dp[p][c][d][v],re(p+1,c+1,0,s[p]-'0')) ;
    else if(c==2 && v==4 && !d)
        dp[p][c][d][v]=max(dp[p][c][d][v],re(p+1,c+1,0,s[p]-'0')) ;
    if(d==0)
    {
        int get=cross[v][s[p]-'0' ];
        if(get<0)
        {
            dp[p][c][d][v]=max(dp[p][c][d][v],re(p+1,c,1,abs(get))) ;
        }
        else
            dp[p][c][d][v]=max(dp[p][c][d][v],re(p+1,c,0,abs(get))) ;
    }
    else
    {
        int get=cross[v][s[p]-'0' ];
        if(get>0)
        {
            dp[p][c][d][v]=max(dp[p][c][d][v],re(p+1,c,1,abs(get))) ;
        }
        else
            dp[p][c][d][v]=max(dp[p][c][d][v],re(p+1,c,0,abs(get))) ;
    }


    return dp[p][c][d][v];

}
int main()
{
     std::ios_base::sync_with_stdio(false);

    #ifndef ONLINE_JUDGE
      // freopen ( "in.txt", "r", stdin );
      //  freopen ( "out.txt", "w", stdout );
    #endif




    string x;

    int t,tcase=1;
    int n,k;

    cin>>t;

    while(t--)
    {
//        n=in<int>();
//        k=in<int>();

        cin>>n>>k;

        cin>>x;
        s.clear();

      //

        for(int i=0;i<n;i++)
        {
            if(x[i]=='i')
                x[i]='2';
            else if(x[i]=='j')
                x[i]='3';
            else if(x[i]=='k')
                x[i]='4';
        }

        for(int i=1;i<=k;i++)
            s+=x;

//        printf("Case #%d: ",tcase++);

        cout<<"Case #"<<tcase++<<": ";

        if(re(1,0,0,s[0]-'0'))
            cout<<"YES\n";
        else
            cout<<("NO\n");
        cc++;
    }

    return 0;
}


