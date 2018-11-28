#include <bits/stdc++.h>
#include <time.h>
#define min(a,b)    (a<b?(a):(b))
#define max(a,b)    (a>b?(a):(b))
#define lli         long long
#define clr(a,b)    memset(a,b,sizeof(a))
#define getcx       getchar_unlocked    
#define S(a)        scanf("%d",&a);
#define SL(a)       scanf("%lld",&a);
#define SS(a)       scanf("%s",a);
#define PV(v)       { for(int i=0;i<v.size();i++) printf("%d ",v[i]);printf("\n"); }
#define FOR(i,n)    for(int i=0;i<n;i++)
#define REP(i,j,n)  for(int i=j;i<n;i++)

void fscani(int *x)
{
    int n=0;int sign=1;char c=getcx();
    while(c<'0' || c>'9'){if(c=='-') sign=-1;c=getcx();}
    while(c>='0' && c<='9'){n=(n<<1)+(n<<3)+(c-'0');c=getcx();}
    n=n*sign;*x=n;
}
void fscanl(lli *x)
{
    lli n=0;int sign=1;char c=getcx();
    while(c<'0' || c>'9'){if(c=='-') sign=-1;   c=getcx();}
    while(c>='0' && c<='9') {n=(n<<1)+(n<<3)+(c-'0');c=getcx();}
    n=n*sign;*x=n;
}




//Constants
#define INF     int(2e9)
#define INFL    ((lli)(9e18))
#define MOD     int(1e9 + 7)

//General STL
#define tr(cont,it)     for(typeof(cont.begin()) it = cont.begin();it!=cont.end();it++)

//Bitwise
#define chkbit(s, b)    (s & ((lli)1<<b))
#define setbit(s, b)    (s |= ((lli)1<<b))
#define clrbit(s, b)    (s &= ~(1<<b))

//Vector
#define vi vector<int>
#define vii vector<pair<int,int> >
#define pb push_back

//Pair
#define ii pair<int,int>
#define lili pair<long long,long long>
#define mp make_pair

//Error Check
#define chk(a)      cout << #a << " : " << a << endl
#define chk2(a,b)   cout << endl << #a << " : " << a << "\t" << #b << " : " << b << endl
#define chk3(a,b,c)     cout << endl << #a << " : " << a << "\t" << #b << " : " << b << "\t" << #c << " : " << c << endl
#define chk4(a,b,c,d)   cout << endl << #a << " : " << a << "\t" << #b << " : " << b << "\t" << #c << " : " << c << "\t" << #d << " : " << d << endl
#define gc      getchar();

//Directions in a matrix 
int dx4[][2] = {{0,1},{0,-1},{1,0},{-1,0}};
int dx8[][2] = {{0,1},{0,-1},{1,1},{1,-1},{1,0},{-1,0},{-1,1},{-1,-1}};


#define in(x) freopen(x,"r",stdin)
#define out(x) freopen(x,"w",stdout)

using namespace std;
lli _pow(lli base, lli expo)
{
    if(expo == 0)
        return 1;
    lli temp = _pow(base, expo/2);
    temp = (temp * temp) ;
    if(expo & 1)
        return (temp * base);
    return temp;
}

int main(int argc,char *argv[])
{
    if(argc>1)
        in(argv[1]);
    if(argc>2)
        out(argv[2]);
    int n,J;
    int t;S(t);
    cin >> n >> J;
    int c = 0;
    printf("Case #1:\n");
    for(int i=(1<<(n-1))+1;i<(1<<n);i+=2) {
        lli x;
        bool can = true;
        vi v;
        for(int j=2;j<=10;j++) {
            x=0;
            for(int k=0;k<n;k++) {
                if(chkbit(i,k))
                    x =x+ _pow(((lli)j),k);
            }
            bool can2 = false;
            lli k;
            for(k=2;k*k<=x;k++) {
                if((x%k)==0){
                    can2 = true;
                    break;
                }
            }
            if(can2)
                v.pb(k);
            if(can2==false){
                can = false;
                break;
            }
        }
        if(can == true) {
            for(int j=n-1;j>=0;j--)
                printf("%d", (chkbit(i,j)?1:0));
            printf(" ");
            FOR(j,v.size())
                printf("%d ",v[j]);
            cout << endl;
            c++;
            if(c==J)
                break;
        }
    }
    return 0;
}


