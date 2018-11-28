#include<iostream>
#include <stdlib.h>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<utility>
#include<iomanip>
#include<queue>

using namespace std;

#define INF (1<<29)
#define SET(a) memset(a,-1,sizeof(a))
#define ALL(a) a.begin(),a.end()
#define CLR(a) memset(a,0,sizeof(a))
#define FILL(a,v) memset(a,v,sizeof(a))
#define PB push_back
#define FOR(i,n) for(int i = 0;i<n;i++)
#define PI acos(-1.0)
#define EPS 1e-9
#define MP(a,b) make_pair(a,b)
#define min3(a,b,c) min(a,min(b,c))
#define mai3(a,b,c) mai(a,mai(b,c))
#define READ freopen("input.tit", "r", stdin)
#define WRITE freopen("output.tit", "w", stdout)
#define LL long long
#define Mi 1000000005

#define F first
#define S second
#define pii pair<int,int>
#define p(i) printf("%d",i)
#define inp(i) scanf("%d",&i)
#define inpll(i) scanf("%lld",&i)
#define getci getchar_unlocked
/*inline void inp( int &n )
 {
 n=0;
 int ch=getci();int sign=1;
 while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getci();}
 
 while(  ch >= '0' && ch <= '9' )
 n = (n<<3)+(n<<1) + ch-'0', ch=getci();
 n=n*sign;
 }*/

using namespace std;
map<char,int> mm;
map<string,int> m;
int stateTransfer[9][4] = { {0,0,0,0},{0,8,3,6},{0,7,8,1},{0,2,5,8},{0,1,2,3},
                                      {0,4,7,2},{0,3,4,5},{0,6,1,4},{0,5,6,7} };

void init(){
    mm.insert(MP('i', 1));
    mm.insert(MP('j', 2));
    mm.insert(MP('k', 3));
    
    
    
    m.insert(MP("i", 1));
    m.insert(MP("j", 2));
    m.insert(MP("k", 3));
    m.insert(MP("1", 4));
    m.insert(MP("-i", 5));
    m.insert(MP("-j", 6));
    m.insert(MP("-k", 7));
    m.insert(MP("-1", 8));
    
}

int arr[10001], store[10001][10001];
bool check[10001][10001] = {0};

int getState(int x,int y){
//    if(check[x][y])
        return store[x][y];
//    int result=arr[x];
//    for(int i=x+1;i<y;i++){
//        result = stateTransfer[result][arr[i]];
//    }
//    store[x][y] = result;
//    check[x][y] = 1;
//    return result;
}

int main(){
    init();
    int t;
    inp(t);
    for(int i=0;i<t;i++){
        m.size();
        int l,x;
        inp(l);
        inp(x);
        string s,resulting;
        cin>>s;
        for(int j=0;j<x;j++)
            resulting.append(s);
        
        l = resulting.length();
        
        for(int j=0;j<l;j++){
            arr[j] = mm[resulting[j]];
            store[j][j] = arr[j];
        }
        
        bool ans = 0;
        for(int j=0;j<l;j++){
            for(int k=j+1;k<l;k++){
                store[j][k] = stateTransfer[ store[j][k-1] ][ arr[k] ];
            }
        }
        for(int j=1;j<l-1;j++){
            if(ans)
                break;
            for(int k=j+1;k<l;k++){
//                cout<<j<<" "<<k<<endl;
                int state1 = getState(0,j-1);
                if(state1 == 1){
                    int state2 = getState(j,k-1);
                    if(state2 ==2){
                        int state3 = getState(k,l-1);
                        if(state3 == 3)
                            ans=1;
                    }
                }
                
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(ans)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
}