/****************************************************************************
 *                                                                          *
 *                    ==>> BG_PeaceMind(BISHAL)                             *
 *                   try=0; while(!success) try++;                          *
 ****************************************************************************/
#include<bits/stdc++.h>
#define PI acos(-1.0)
#define nl puts("")
#define SZ(x) x.size()
#define pb(x) push_back(x)
#define X first
#define Y second
#define pii pair<int,int>
#define S(a) scanf("%d",&a)
#define P(a) printf("%d",a)
#define SL(a) scanf("%lld",&a)
#define S2(a,b) scanf("%d%d",&a,&b)
#define S3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define SL2(a,b) scanf("%lld%lld",&a,&b)
#define SL3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define all(v) v.begin(),v.end()
#define clr(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define fr(i,a,n) for(i=a;i<=n;i++)
#define rf(i,n,a) for(i=n;i>=a;i--)
#define LB(v,k) lower_bound(v.begin(),v.end(),k)
#define _cin ios_base::sync_with_stdio(0),cin.tie(0)
#define ct(x) cerr<<__LINE__<< ":: "<<#x<<"= "<<x<<endl
#define fi(it,n) for(__typeof(n.begin()) it=n.begin();it!=n.end();it++)
using namespace std;
typedef long long ll;
/// atoi( str.c_str() ); // char string to int
/// sprintf(str,"%d",num);// num to char string
///int month[]={-1,31,28,31,30,31,30,31,31,30,31,30,31}; //Not Leap Yr
///int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Dir
///int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 Dir
///int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight
/************************************************************************
 * /////////////////////////////////////////////////////////////////////*
 ************************************************************************/
/// [ Look at my code below, My code is so amazing !! :P ]
///  Digit    0123456789
#define MX    20
#define inf   2000005

int n,r,c,Sz[5];
bool ar[MX+2][MX+2],vis[MX+5];
vector< vector<pii> >v[5];
vector< pii >vp;

void precal( ) {

    vp.clear();
    vp.pb( pii(0,0) );
    v[1].pb(vp);

    ///#2
    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    v[2].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    v[2].pb(vp);

    ///#3
    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+2,0) );
    v[3].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(0,+2) );
    v[3].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(0,+1) );
    v[3].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+1,+1) );
    v[3].pb(vp);

    vp.clear();
    vp.pb( pii(0,0));
    vp.pb( pii(0,+1));
    vp.pb( pii(+1,+1));
    v[3].pb(vp);

    vp.clear();
    vp.pb( pii(0,0));
    vp.pb( pii(+1,0));
    vp.pb( pii(+1,-1));
    v[3].pb(vp);

    /// #4
    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(0,+2) );
    vp.pb( pii(0,+3) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+2,0) );
    vp.pb( pii(+3,0) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+1,+1) );
    vp.pb( pii(0,+1) );
    v[4].pb(vp);
    ///
    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+2,0) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(+1,+1) );
    vp.pb( pii(+2,+1) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+2,0) );
    vp.pb( pii(+2,-1) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+2,0) );
    vp.pb( pii(+2,+1) );
    v[4].pb(vp);

    ///add
    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(0,+2) );
    vp.pb( pii(+1,0) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(0,+2) );
    vp.pb( pii(+1,+2) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(0,+2) );
    vp.pb( pii(-1,0) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(0,+2) );
    vp.pb( pii(-1,+2) );
    v[4].pb(vp);


    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+2,0) );
    vp.pb( pii(+1,+1) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+2,0) );
    vp.pb( pii(+1,-1) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(0,+2) );
    vp.pb( pii(+1,+1) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(0,+2) );
    vp.pb( pii(-1,+1) );
    v[4].pb(vp);
    ///
    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+1,+1) );
    vp.pb( pii(+2,+1) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+1,-1) );
    vp.pb( pii(+2,-1) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(+1,+1) );
    vp.pb( pii(+1,+2) );
    v[4].pb(vp);

    vp.clear();
    vp.pb( pii(0,0) );
    vp.pb( pii(0,+1) );
    vp.pb( pii(+1,0) );
    vp.pb( pii(+1,-1) );
    v[4].pb(vp);

    for(int i=1; i<=4; i++) {
        Sz[i]=SZ( v[i] );
        //cout<< "size: "<<Sz[i]<<endl;
    }
}

bool dn,fvis[MX+5];
void go(int s) {
    if(dn) return;
    int i,j;
    bool ok=1;
    fr(i,0,r-1) {
        fr(j,0,c-1) {
            if(!ar[i][j]) {
                ok=0;
                break;
            }
        }
        if(!ok)break;
    }
    if(ok) {
        for(int i=0; i<Sz[n]; i++ ) {
            fvis[i]|=vis[i];
        }
        bool fst=0;
        if(n==1 && fvis[0]==1)fst=1;
        else if(n==2) {
            if(fvis[0]+fvis[1])fst=1;
        } else if(n==3) {
            if( (fvis[0]+fvis[1]) && ( fvis[2]+fvis[3]+fvis[4]+fvis[5] ) )fst=1;
        }
        if(fst) {
            dn=1;
        }
        return;
    }
    if(dn) return;
    bool insd=0;
    for(int x=0; x<r; x++) {
        for(int y=0; y<c; y++) {

            if( ar[x][y] )continue;

            for(int i=0; i<Sz[n]; i++) {

                vector<pii>p=v[n][i];

                bool cn=1;

                int sz=SZ(p);

                for(int j=0; j<sz; j++) {

                    int px=x+p[j].X;
                    int py=y+p[j].Y;

                    if(px<0 ||px>=r || py<0 || py>=c || ar[px][py]==1 ) {
                        cn=0;
                        break;
                    }
                }

                if(cn) {

                    for(int j=0; j<sz; j++) {
                        int px=x+p[j].X;
                        int py=y+p[j].Y;

                        ar[px][py]=1;
                    }

                    vis[ i ]=1;
                    insd=1;
                    go(s+1);
                    vis[ i ]=0;
                    for(int j=0; j<sz; j++) {

                        int px=x+p[j].X;
                        int py=y+p[j].Y;

                        ar[px][py]=0;
                    }
                }
            }
        }
    }
    if(!insd) return;
}

void test(int n) {
    int i,j,k,x=3,y=3;
    for(int i=0; i<Sz[n]; i++) {
        clr(ar);
        vector<pii>p=v[n][i];
        int sz=SZ(p);
        for(int j=0; j<sz; j++) {
            int px=x+p[j].X;
            int py=y+p[j].Y;
            ar[px][py]=1;
        }
        cout<< "No : "<<i<<endl;
        fr(j,0,6) {
            fr(k,0,6) {
                if(!ar[j][k])cout<< " ";
                else cout<<"#";
            }
            nl;
        }
        nl;
    }
}

int main() {
    int tc,cs=1,i,j,k;
    freopen("D-small-attempt4.in", "r", stdin);
    freopen("Output_DLaastt.txt", "w", stdout);
    precal();
    //fr(i,1,4)test(i);
    S(tc);
    while(tc--) {
        clr(ar);
        clr(vis);
        clr(fvis);
        S(n);
        S2(r,c);

//        if(n==4) {
//            if(r!=4 || c!=4) {
//                printf("Case #%d: RICHARD\n",cs++);
//                continue;
//            }
//        }

        dn=0;
        // fr(i,0,r-1)fr(j,0,c-1)ar[i][j]=0;
        go(0);

        if(dn) {
            printf("Case #%d: GABRIEL\n",cs++);
            continue;
        }
        int fst=0;
        if(n==1 && fvis[0]==1)fst=1;
        else if(n==2) {
            if(fvis[0]+fvis[1])fst=1;
        } else if(n==3) {
            if( (fvis[0]+fvis[1]) && ( fvis[2]+fvis[3]+fvis[4]+fvis[5] ) )fst=1;
        } else {

            bool al=1;
            bool vl=0;
            fr(i,0,1)vl|=fvis[i];
            al=(al&vl);

            vl=0;
            fr(i,2,2)vl|=fvis[i];
            al=(al&vl);

            vl=0;
            fr(i,3,10)vl|=fvis[i];
            al=(al&vl);

            vl=0;
            fr(i,11,14)vl|=fvis[i];
            al=(al&vl);

            vl=0;
            fr(i,15,18)vl|=fvis[i];
            al=(al&vl);

            if(al)fst=1;
        }

        if(fst) {
            printf("Case #%d: GABRIEL\n",cs++);
        } else {
            printf("Case #%d: RICHARD\n",cs++);
        }
    }
    return 0;
}
