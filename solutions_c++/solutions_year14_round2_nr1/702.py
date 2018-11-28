/*
Bismillahir Rahmanir Rahim
Coder: Ahmad Faiyaz
*/

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <fstream>
#include <ctime>


# define FOR(i, a, b) for (int i=a; i<b; i++)
# define REP(i, a) FOR(i,0,a)

#define EPS 1e-11
#define inf 1234567891
#define LL long long

#define abs(x) (((x)< 0) ? (-(x)) : (x))
#define all(x) (x).begin(), (x).end()
#define ms(x, a) memset((x), (a), sizeof(x))

#define pb push_back
#define FORIT(i,m) for(__typeof((m).begin()) i=(m).begin();i!=(m).end();i++)
#define pii pair<int,int>
#define UNIQUE(c) (c).resize( unique( all(c) ) - (c).begin() )

#define READ(f) {ifstream infile(f) ;if(infile.good()) freopen(f, "r", stdin);}
#define WRITE(f) freopen(f, "w", stdout)
#define CIN ios_base::sync_with_stdio(0);
///int rrr[]={1,0,-1,0};int ccc[]={0,1,0,-1}; //4 Direction
///int rrr[]={1,1,0,-1,-1,-1,0,1};int ccc[]={0,1,1,1,0,-1,-1,-1};//8 direction
///int rrr[]={2,1,-1,-2,-2,-1,1,2};int ccc[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
///int rrr[]={2,1,-1,-2,-1,1};int ccc[]={0,1,1,0,-1,-1}; //Hexagonal Direction
///int month[]={31,28,31,30,31,30,31,31,30,31,30,31}; //month

using namespace std;



int check (string a, string b){
    int idx = 0;
    vector <string> va, vb;
    char lst ='\0';
    string sofar = "";
    for(int i=0;i<a.size();i++){
        if(a[i]==lst){
            sofar += a[i];
        }else{
            va.pb(sofar);
            lst = a[i];
            sofar = "";
            sofar += a[i];
        }
    }
    if(sofar != "")
    va.pb(sofar);
    lst ='\0';
    sofar = "";
    for(int i=0;i<b.size();i++){
        if(b[i]==lst){
            sofar += b[i];
        }else{
            vb.pb(sofar);
            lst = b[i];
            sofar = "";
            sofar += b[i];
        }
    }
    if(sofar != "")
    vb.pb(sofar);
    int cnt = 0;
    for(int i=0;i<va.size();i++){
        //cout<<va[i]<<" "<<vb[i]<<endl;
        cnt += abs((int)va[i].size() - (int)vb[i].size());
    }
    return cnt;
}


int main(){
    #if defined( faiyaz_pc )
        READ("A-small-attempt0.in");
        WRITE("small.txt");
    #endif

    int t, chk = 1;
    cin>>t;
    while(t--){
        cout<<"Case #"<<chk++<<": ";
        int n;
        string a, b;
        cin>>n;
        cin>>a>>b;

        string tmpa = a;
        string tmpb = b;

        UNIQUE(tmpa);
        UNIQUE(tmpb);

        if(tmpa != tmpb){
            cout<<"Fegla Won\n";
        }else{
            cout<<min(check(a, b), check(b, a))<<"\n";
        }
    }

    return 0;
}
