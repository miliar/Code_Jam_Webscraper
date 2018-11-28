#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define scanl(a) scanf("%lld",&a)
#define scanii(a,b) scanf("%d%d",&a,&b)
#define scaniii(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define scanll(a,b) scanf("%lld%lld",&a,&b)
#define scanlll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define scani(a) scanf("%d",&a)
#define clr(a) memset(a,0,sizeof(a))
#define clr_(a) memset(a,-1,sizeof(a))
#define pb(a) push_back(a)
#define siz 1001
#define pii pair<int,int>
#define sqr(a) a*a
#define eps 1e-9
#define inf 1e9
#define pi acos(-1.0)
#define x first
#define y second
#define INF 1e18
int strTOint(string s)
{
    stringstream ss;
    int x;
    ss<<s;
    ss>>x;
    return x;
}
double geo_dist(int a,int b,int c,int d)
{
    double dd=(double)(a-c)*(a-c)+(b-d)*(b-d);
    double r=sqrt(dd)+eps;
    return r;
}
int fx[]={0,0,-1,1,-1,1,1,-1};
int fy[]={1,-1,0,0,1,1,-1,-1};
///FOR KNIGHT MOVE
///int fx[]={2,1,-1,-2,-2,-1,1,2};
///int fy[]={1,2,2,1,-1,-2,-2,-1};
map<string,int>mp;
map<char,int>mpc;
vector<pii>adj[1000];
vector<int>v;
map<int,int>mpi;
string ss[]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int main()
{
    ///freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scani(t);
    for(int k=1;k<=t;k++)
    {
        string s;
        mpc.clear();
        mpi.clear();
        cin>>s;
        int x=s.length();
        for(int i=0;i<x;i++)
        {
            mpc[s[i]]++;
        }
        int p;
        p=mpc['Z'];
///cout<<p<<endl;
        mpi[0]=p;
        mpc['Z']-=p;
        mpc['E']-=p;
        mpc['R']-=p;
        mpc['O']-=p;
        p=mpc['X'];
   ///     cout<<p<<endl;
        mpi[6]=p;
        mpc['I']-=p;
        mpc['S']-=p;
        mpc['X']-=p;
        p=mpc['G'];
      ///  cout<<p<<endl;
        mpi[8]=p;
        mpc['E']-=p;
        mpc['I']-=p;
        mpc['G']-=p;
        mpc['H']-=p;
        mpc['T']-=p;
        p=mpc['S'];
        mpi[7]=p;
       /// cout<<p<<endl;
        mpc['S']-=p;
        mpc['E']-=p;
        mpc['E']-=p;
        mpc['V']-=p;
        mpc['N']-=p;
        p=mpc['H'];
        mpi[3]=p;
        ///cout<<p<<endl;
        mpc['T']-=p;
        mpc['H']-=p;
        mpc['R']-=p;
        mpc['E']-=p;
        mpc['E']-=p;
        p=mpc['T'];
        mpi[2]=p;
       /// cout<<p<<endl;
        mpc['T']-=p;
        mpc['W']-=p;
        mpc['O']-=p;
         p=mpc['U'];
///         cout<<p<<endl;

        mpi[4]=p;
        mpc['F']-=p;
        mpc['O']-=p;
        mpc['R']-=p;
        mpc['U']-=p;
         p=mpc['V'];
   ///      cout<<p<<endl;
        mpi[5]=p;
        mpc['F']-=p;
        mpc['I']-=p;
        mpc['V']-=p;
        mpc['E']-=p;
         p=mpc['O'];
      ///   cout<<p<<endl;
        mpi[1]=p;
        mpc['O']-=p;
        mpc['N']-=p;
        mpc['E']-=p;
        mpi[9]=mpc['I'];
      ///  cout<<mpi[9]<<endl;
        printf("Case #%d: ",k);
        for(int i=0;i<=9;i++)
        {
            int pq=mpi[i];
            while(pq--)
                cout<<i;
        }
        cout<<endl;
        /*string sss="";
        for(int i=0;i<=9;i++)
        {
            string temp=ss[i];
            int sz=temp.length();
            int y=inf;
            for(int j=0;j<sz;j++)
            {
                int r=mpc[temp[j]];
                if((j==3 || j==7) && temp[j]=='E')r/=2;
                y=min(y,r);
            }
            for(int j=0;j<y;j++)
            {
                sss+=i+48;
            }
             for(int j=0;j<sz;j++)
            {
                mpc[temp[j]]-=y;
            }
        }
        printf("Case #%d: ",k);
        cout<<sss<<endl;*/
    }
    return 0;
}

