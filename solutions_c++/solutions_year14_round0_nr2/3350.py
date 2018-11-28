#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <set>
#include <iomanip>
#include <algorithm>
#include <string.h>
#include <ctype.h>
#include <math.h>
using namespace std;

#define pb push_back
#define X first
#define Y second
#define ll long long
#define MAX 1000000000
#define fi freopen("B-large.in","r",stdin);

int t;

int main()
{
    fi;
    freopen("out.out","w",stdout);
    cin>>t;
    for(int cas=1;cas<=t;cas++) {
        double C,F,X,R=2.0,T=0.0;
        cout<<"Case #"<<cas<<": ";
        cin>>C>>F>>X;
        while(1) {
            if(X/R <= C/R + X/(R+F)) {
                T=T+X/R;
                break;
            }
            T=T+C/R;
            R=R+F;
        }
        cout<<fixed<<setprecision(7)<<T<<"\n";
    }
}
