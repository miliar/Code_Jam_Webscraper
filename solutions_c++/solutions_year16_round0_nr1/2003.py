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
    int tab[10];
    int cnt,tg;
    REP(t,T){
        cout<<"Case #"<<(t+1)<<": ";
        CLR(tab);
        cnt=0;
        tg=0;
        int n;
        cin>>n;
        if(n==0){
            cout<<"INSOMNIA"<<"\n";
        }else{
            while(cnt<10){
                tg+=n;
                int ttg=tg;
                while(ttg){
                    int digit=ttg%10;
                    if(!tab[digit]) cnt++;
                    tab[digit]=1;
                    ttg=ttg/10;
                }
            }
            cout<<tg<<"\n";
        }
    }
}