#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <numeric> //accumulate(i poczatek,i koniec, wartosc_poczatkowa)
#include <utility> //swap
#include <map>
#include <cmath>
#include <functional> //for greater<>
using namespace std;

typedef vector<int> VI;
typedef long long LL;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
int main (int argc, char * const argv[]) {
#ifndef ONLINE_JUDGE
	if(!freopen("D-small-attempt4.in", "r", stdin)) cout<<"Blad odczytu in.txt"<<endl;
	if(!freopen("outattempt4.txt", "w", stdout)) cout<<"Blad pliku wyjsciowego"<<endl;
#endif
	ios_base::sync_with_stdio(0);
	int t;
    cin>>t;
    FOR(numtestu,1,t){
        int x,r,c;
        cin>>x>>r>>c;
        int maxx=max(r,c);
        r=min(r,c);
        c=maxx;
        //cout<<" r: "<<r<< " c: "<<c<<endl;
        if(r*c%x!=0) cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        else
        if(r==1 and c==1){
            if(x==1) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }
        else if (r==1 and c==2){
            if(x<=2) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }
        else if(r==1 and c==3){
            if(x<=1) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;

        }
        else if(r==1 and c==4){
            if(x<=2) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }
        else if(r==2 and c==2){
            if(x<=2) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }
        else if(r==2 and c==3){
            if(x<=3) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }
        else if(r==2 and c==4){
            if(x<=2) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }
        else if(r==3 and c==3){
            if(x<=3 and x!=2) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }
        else if(r==3 and c==4){
            if(x<=4) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }else if(r==4 and c==4){
            if(x<=4 and x!=3) cout<<"Case #"<<numtestu<<": GABRIEL"<<endl;
            else cout<<"Case #"<<numtestu<<": RICHARD"<<endl;
        }
        
    }
	
	
    return 0;
}