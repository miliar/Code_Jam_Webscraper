#include<iostream>
#include<sstream>
#include<vector>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<functional>
#include<climits>
#include<utility>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pi;

#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define FORB(i,s,e,st) for (int i = int(s); i < int(e); i+=(int(st)))
#define FOR(i,s,e) FORB(i,s,e,1)
#define REP(i,x) FOR(i,0,x)
#define CLR(a) memset((a), 0 ,sizeof(a))


const int MOD = 1000000007;
const double PI  = acos(-1.0);

bool avoid[100][100][4];
        int r,c;

char dir[4]={'<','>','^','v'};

int main(){

    int T;
    cin>>T;
    REP(t,T){
        cout<<"Case #"<<(t+1)<<": ";

        cin>>r>>c;
        string str;
        vector<string> map;
        REP(i,r){
            cin>>str;
            map.push_back(str);
        }

        CLR(avoid);
        REP(i,r){
            REP(j,c){
                if(map[i][j]!='.'){
                    avoid[i][j][0]=true;
                    break;
                }
            }
            for(int j=c-1;j>=0;j--){
                if(map[i][j]!='.'){
                    avoid[i][j][1]=true;
                    break;
                }
            }
        }
        REP(i,c){
            REP(j,r){
                if(map[j][i]!='.'){
                    avoid[j][i][2]=true;
                    break;
                }
            }
            for(int j=r-1;j>=0;j--){
                if(map[j][i]!='.'){
                    avoid[j][i][3]=true;
                    break;
                }
            }
        }
        
        int ret=0;
        REP(i,r){
            REP(j,c){
                bool flag=true;
                REP(k,4){
                    flag=flag&avoid[i][j][k];
                    if(avoid[i][j][k]&&map[i][j]==dir[k]) ret++;
                }
                if(flag) ret-=1000000;
            }
        }
        if(ret<0) cout<<"IMPOSSIBLE\n";
        else cout<<ret<<"\n";
        
    }
}
