
/*
     If opportunity doesn't knock, build a door.

            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
            |S|.|S|.|R|.|A|.|S|.|A|.|M|.|K|
            +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    Success is how high you bounce when you hit bottom.
*/


#include <bits/stdc++.h>

#define pii              pair <int,int>
#define pll              pair <long long,long long>
#define sc               scanf
#define pf               printf
#define Pi               2*acos(0.0)
#define ms(a,b)          memset(a, b, sizeof(a))
#define pb(a)            push_back(a)
#define MP               make_pair
#define db               double
#define ll               long long
#define EPS              10E-10
#define ff               first
#define ss               second
#define sqr(x)           (x)*(x)
#define D(x)             cout<<#x " = "<<(x)<<endl
#define VI               vector <int>
#define DBG              pf("Hi\n")
#define MOD              1000000007
#define CIN              ios_base::sync_with_stdio(0); cin.tie(0)
#define SZ(a)            (int)a.size()
#define sf(a)            scanf("%d",&a)
#define sfl(a)           scanf("%lld",&a)
#define sff(a,b)         scanf("%d %d",&a,&b)
#define sffl(a,b)        scanf("%lld %lld",&a,&b)
#define sfff(a,b,c)      scanf("%d %d %d",&a,&b,&c)
#define sfffl(a,b,c)     scanf("%lld %lld %lld",&a,&b,&c)
#define stlloop(v)       for(__typeof(v.begin()) it=v.begin();it!=v.end();it++)
#define loop(i,n)        for(int i=0;i<n;i++)
#define REP(i,a,b)       for(int i=a;i<b;i++)
#define RREP(i,a,b)      for(int i=a;i>=b;i--)
#define TEST_CASE(t)     for(int z=1;z<=t;z++)
#define PRINT_CASE       printf("Case %d: ",z)
#define CASE_PRINT       cout<<"Case #"<<z<<": "
#define all(a)           a.begin(),a.end()
#define intlim           2147483648
#define infinity         (1<<28)
#define ull              unsigned long long
#define gcd(a, b)        __gcd(a, b)
#define lcm(a, b)        ((a)*((b)/gcd(a,b)))

using namespace std;


/*----------------------Graph Moves----------------*/
//const int fx[]={+1,-1,+0,+0};
//const int fy[]={+0,+0,+1,-1};
//const int fx[]={+0,+0,+1,-1,-1,+1,-1,+1};   // Kings Move
//const int fy[]={-1,+1,+0,+0,+1,+1,-1,-1};  // Kings Move
//const int fx[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int fy[]={-1,  1, -2,  2, -2,  2, -1,  1}; // Knights Move
/*------------------------------------------------*/

/*-----------------------Bitmask------------------*/
//int Set(int N,int pos){return N=N | (1<<pos);}
//int reset(int N,int pos){return N= N & ~(1<<pos);}
//bool check(int N,int pos){return (bool)(N & (1<<pos));}
/*------------------------------------------------*/

string s1,s2;

int fff,kkk;

struct data
{
    int c, j, diff;
    data()
    {

    }
    data (int a,int b, int c)
    {
        c=a,j=b,diff=c;
    }
};

bool check1(int a, int b)
{
    int xx,yy;
    bool aaaa=0;
    xx=(s1[0]=='?' || s1[0]=='0'+a)? xx=a: aaaa=1;
    yy=(s2[0]=='?' || s2[0]=='0'+b)? yy=b: aaaa=1;

    if(aaaa) return 0;

    fff=xx;
    kkk=yy;
//    if(xx<=yy) return 1;
    return 1;
}

bool check2(int a, int b, int x, int y)
{
    bool aaaa=0;
    int aa,bb,xx,yy;
    aa=(s1[0]=='?' || s1[0]=='0'+a)? aa=a:aaaa=1;
    bb=(s1[1]=='?' || s1[1]=='0'+b)? bb=b:aaaa=1;
    xx=(s2[0]=='?' || s2[0]=='0'+x)? xx=x:aaaa=1;
    yy=(s2[1]=='?' || s2[1]=='0'+y)? yy=y:aaaa=1;
    if(aaaa) return 0;
    fff=aa*10+bb;
    kkk=xx*10+yy;
//    if(aa*10+bb<=xx*10+yy) return 1;
    return 1;
}


bool check3(int a, int b, int c, int x, int y, int z)
{
    int aa,bb,cc,xx,yy,zz;
    bool aaaa=0;
    aa=(s1[0]=='?' || s1[0]=='0'+a)? aa=a:aaaa=1;
    bb=(s1[1]=='?' || s1[1]=='0'+b)? bb=b:aaaa=1;
    cc=(s1[2]=='?' || s1[2]=='0'+c)? cc=c:aaaa=1;
    xx=(s2[0]=='?' || s2[0]=='0'+x)? xx=x:aaaa=1;
    yy=(s2[1]=='?' || s2[1]=='0'+y)? yy=y:aaaa=1;
    zz=(s2[2]=='?' || s2[2]=='0'+z)? zz=z:aaaa=1;

    if(aaaa) return 0;

    fff=aa*100+bb*10+cc;
    kkk=xx*100+yy*10+zz;

//    if(aa*100+bb*10+cc<=xx*100+yy*10+zz) return 1;
    return 1;
}


//bool check1(int a, int b, int c, int x, int y, int x)
//{
//
//}

bool comp(data a, data b)
{
    if(a.diff<b.diff) return 1;
    else if(a.diff>b.diff) return 0;
    else
    {
        if(a.c<b.c) return 1;
        else if(a.c>b.c) return 0;
        else
            {
                return a.j<b.j;
            }
    }
}


int main()
{

     freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    TEST_CASE(t)
    {
        string s3,s4;
        cin>>s3>>s4;
        s1=s3;
        s2=s4;
        vector<data>vv;
        int n1=100000,n2=100000;
        int fuck=100000;
        CASE_PRINT;

        if(SZ(s1)==1)
        {
            loop(i,10)
            loop(j,10)
            {
                if(check1(i,j))
                {
                    int ppp=(abs(kkk-fff));
                    data temp;
                 temp.c=fff;
                 temp.j=kkk;
                 temp.diff=ppp;
                vv.pb(temp);
                }
            }
            sort(all(vv),comp);

//            stlloop(vv) cout<<it->c << " "<<it->j<<" " << it->diff<<endl;

            n1=vv[0].c;
            n2=vv[0].j;
            cout<<n1<<" "<<n2<<endl;
        }

        if(SZ(s1)==2)
        {
            loop(i,10)
            loop(j,10)
            loop(k,10)
            loop(l,10)
            if(check2(i,j,k,l))
            {
                 int ppp=(abs(kkk-fff));
                 data temp;
                 temp.c=fff;
                 temp.j=kkk;
                 temp.diff=ppp;
                vv.pb(temp);
            }
//            cout<<endl;
//            stlloop(vv) cout<<it->c << " "<<it->j<<" " << it->diff<<endl;
             sort(all(vv),comp);


            n1=vv[0].c;
            n2=vv[0].j;
           if(n1<10) cout<<0;
           cout<<n1<<" ";
           if(n2<10) cout<<0;
           cout<<n2<<endl;
        }
        if(SZ(s1)==3)
        {
            loop(i,10) loop(j,10) loop(k,10) loop(l,10) loop(p,10) loop(q,10)
            if(check3(i,j,k,l,p,q))
            {
                 int ppp=(abs(kkk-fff));
                   data temp;
                 temp.c=fff;
                 temp.j=kkk;
                 temp.diff=ppp;
                vv.pb(temp);
            }
             sort(all(vv),comp);
            n1=vv[0].c;
            n2=vv[0].j;
            if(n1<100)cout<<0;
            if(n1<10)cout<<0;
            cout<<n1<<" ";
           if(n2<100) cout<<0;
           if(n2<10) cout<<0;
           cout<<n2<<endl;
        }

    }

    return 0;
}
