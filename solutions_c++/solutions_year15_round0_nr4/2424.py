///This  code is created by Samar Singh Holkar
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include<list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define sd(x) scanf("%d",&x)
#define sfd(x) scanf("%d",&x)
#define sfld(x) scanf("%lld",&x
#define pf printf

#define LL long long
#define ll long long
#define LD long double
#define ld long double
#define PB push_back
#define pb push_back
#define MP make_pair
#define mp make_pair
#define F first
#define S second

#define pii pair<int,int>
#define vi vector<int>
#define fr(i,n) for( int i=0; i<=n; i++)
#define frm(i,m,n) for(int i=m; i<=n; i++)
#define N 200000

int main(){

    int p=1,t; cin>>t;

    while(p<=t){

        int x,r,c; cin>>x>>r>>c;

        if(x==1){cout<<"Case #"<<p<<": GABRIEL\n";}

        else if(x==2){

            if((r*c)%2==0){cout<<"Case #"<<p<<": GABRIEL\n";}

            else cout<<"Case #"<<p<<": RICHARD\n";
        }

        else if(x==4){

            if((r==3 && c==4)||(r==4 && c==3)||(r==4&&c==4)){

                cout<<"Case #"<<p<<": GABRIEL\n";
            }

            else {

                cout<<"Case #"<<p<<": RICHARD\n";
            }
        }
        else{

            int k = min(r,c);

            int l = r*c;

            if(k>=2 && l%3==0){cout<<"Case #"<<p<<": GABRIEL\n";}

            else{cout<<"Case #"<<p<<": RICHARD\n";}

        }
        p++;
    }
}
