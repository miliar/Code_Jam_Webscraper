/*
 ONLY FOR SMALL INPUT
 */



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



int main(){
    int T;
    cin>>T;
    REP(t,T){
        cout<<"Case #"<<(t+1)<<": ";
        int x,r,c;
        cin>>x>>r>>c;
        if((r*c)%x!=0){
            cout<<"RICHARD\n";
        }else{
            switch(x){
                case 1:
                case 2:
                    cout<<"GABRIEL\n";
                    break;
                case 3:
                    if(r==1||c==1) cout<<"RICHARD\n";
                    else cout<<"GABRIEL\n";
                    break;
                case 4:
                    if(r<=2||c<=2) cout<<"RICHARD\n";
                    else cout<<"GABRIEL\n";
                    break;
                case 5:
//                    break;
                case 6:
//                    break;
                default:
                    cout<<"RICHARD\n";
                    break;
            }
        }
    }
}