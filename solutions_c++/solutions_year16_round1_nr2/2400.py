//==================================================================//
// Name        : flash7even                                         //
// Author      : Tarango Khan                                       //
// Codeforces  : flash_7                                            //
// Topcoder    : flash_7                                            //
// Hackerrank  : flash_7                                            //
// Email       : tarangokhan77@gmail.com                            //
// Facebook    : tarango.khan                                       //
//==================================================================//

//==================================================================//
#include <bits/stdc++.h>                                            //
using namespace std;                                                //
#define read(nm)        freopen(nm, "r", stdin)                     //
#define write(nm)       freopen(nm, "w", stdout)                    //
#define pb              push_back                                   //
#define mp              make_pair                                   //
#define F               first                                       //
#define S               second                                      //
#define eps             1e-9                                        //
#define FABS(x)         ((x)+eps<0?-(x):(x))                        //
#define pf              printf                                      //
#define sf              scanf                                       //
#define pi              acos(-1.0)                                  //
#define SZ(x)           ((int)(x).size())                           //
#define mems(x,v)       memset(x,v,sizeof(x))                       //
#define fills(v,n)      fill(v.begin(), v.end(), n)                 //
#define vsort(v)        sort(v.begin(),v.end())                     //
#define asort(v,n)  	sort(a,a+n)                                 //
#define LL              long long                                   //
#define LLU             long long unsigned int                      //
#define debug1(v1)      cout<<"1@ Debug Val 1 = "<<v1<<endl;        //
#define debug2(v2)      cout<<"   2@ Debug Num 2 = "<<v2<<endl;     //
#define debug3(v3)      cout<<"      3@ Debug Res 3 = "<<v3<<endl;  //
#define UB(v,a)   upper_bound(v.begin(),v.end(),a)-v.begin()        //
#define LB(v,a)   lower_bound(v.begin(),v.end(),a)-v.begin()        //
#define fast_cin ios_base::sync_with_stdio(false);cin.tie(NULL)     //
//==================================================================//

//==================================================================//
void make_unique(vector<int> &a){ sort(a.begin(), a.end());         //
     a.erase(unique(a.begin(), a.end()), a.end()); }                //
void printDouble(double f,int p){ cout << fixed;                    //
     cout << setprecision(p) << f <<endl; }                         //
LL  Set(LL N,LL cur)
{
    return N = N | (1LL<<cur);    //
}
int  Reset(int N,int cur)
{
    return N = N & ~(1<<cur);    //
}
bool Check(LL N,LL cur)
{
    return (bool)(N & (1LL<<cur));    //
}
LL   GCD(LL a,LL b){ if(b == 0) return a; return GCD(b,a%b);}       //
LL   LCM(LL a,LL b){ return a*b/GCD(a,b);}                          //
LL   POW(LL a,LL p){ LL res = 1,x = a;while(p){if(p&1)              //
     res = (res*x); x = (x*x);p >>= 1;} return res;}                //
//==================================================================//

//==================================================================//
//int knightDir[8][2] = {{-2,1},{-1,2},{1,2},{2,1},                 //
//                      {2,-1},{-1,-2},{1,-2},{-2,-1}};             //
//int dir8[4][2]      = {{-1,0},{0,1},{1,0},{0,-1},                 //
//                      {-1,-1},{1,1},{1,-1},{-1,1}};               //
//int dir4[4][2]      = {{-1,0},{0,1},{1,0},{0,-1}};                //
//==================================================================//
//=======// Done With The Shortcut Stuffs! Now Let's Code! //=======//

#define INF (1<<30)
#define MOD 1000000007

int N;
int A[105][105];
vector<int> Graph[205];
//int G[105][105];

void make_Graph(){
    //mems(G,0);
    for(int i = 0;i<2*N-1;i++){
        for(int j = 0;j<2*N-1;j++){
            if(i == j) continue;
            bool f = true;
            for(int c = 0;c<N;c++){
                if(A[j][c]<=A[i][c]){
                    f = false;
                    break;
                }
            }
            if(f == true){
                Graph[i].pb(j);
                //G[i][j] = 1;
            }
        }
    }
    return;
    for(int i = 0;i<2*N-1;i++){
        pf("Adj of i: %d =",i);
        int Sz = Graph[i].size();
        for(int c = 0;c<Sz;c++) pf(" %d",Graph[i][c]);
        pf("\n");
    }
}

bool resf = false;
vector<int> rs;
int mask[105];
int taken[105];

bool ok(int p){
    for(int i = 0;i<2*N-1;i++){
        if(taken[i] == 1) continue;
        bool f = true;
        for(int j = 0;j<N;j++){
            if(A[mask[j]][p] != A[i][j]){
                f = false;
                break;
            }
        }
        if(f == true){
            //pf("Matched at row: %d\n",i);
            return true;
        }
    }
    return false;
}

void call(int cur,int cnt){
    //pf("At cur: %d , cnt: %d\n",cur,cnt);
    if(resf == true) return;
    if(cnt == N){
        //pf("Cur selected:");
        //for(int i = 0;i<cnt;i++) pf(" %d",mask[i]);
        //pf("\n");
        int cnt2 = 0;
        for(int c = 0;c<N;c++){
            if(ok(c) == false){
                //pf("Not found: %d\n",c);
                cnt2++;
                if(cnt2>1) return;
                rs.clear();
                for(int i = 0;i<N;i++){
                    rs.pb(A[mask[i]][c]);
                }
            }
            //pf("Found: %d\n",c);
        }
        if(cnt2 == 1){
            for(int i = 0;i<N;i++){
                if(i != 0) cout<<" ";
                cout<<rs[i];
            }
            cout << endl;
            resf = true;
        }
        return;
    }
    if(cur == 2*N-1) return;
    if(cnt == 0){
        mask[cnt] = cur;
        taken[cur] = 1;
        call(cur,cnt+1);
        if(resf == true) return;
        taken[cur] = 0;
        call(cur+1,cnt);
        return;
    }
    int Sz = Graph[cur].size();
    for(int i = 0;i<Sz;i++){
        int nCur = Graph[cur][i];
        mask[cnt] = nCur;
        taken[nCur] = 1;
        call(nCur,cnt+1);
        if(resf == true) return;
        taken[nCur] = 0;
        call(nCur,cnt);
    }
}

void solve(){
    mems(taken,0);
    mems(mask,0);
    rs.clear();
    make_Graph();
    resf = false;
    call(0,0);
}

int main(){
    read("input_B.txt");
    write("output_B.txt");
    fast_cin;
    int nCase;
    cin >> nCase;
    for(int cs = 1;cs<=nCase;cs++){
        cin >> N;
        for(int i = 0;i<N*2-1;i++){
            Graph[i].clear();
            for(int j = 0;j<N;j++){
                cin >> A[i][j];
            }
        }
        cout << "Case #" << cs << ": ";
        solve();
    }
    return 0;
}
