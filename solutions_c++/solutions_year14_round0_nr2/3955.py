/*===============*\
|  ID: TMANDZU    |
|    LANG: C++    |
\*===============*/
//Tornike Mandzulashvili
//#pragma comment(linker,"/STACK:256000000")
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <stack>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iostream>
#include <set>
#include <cstring>

#define deb(x) cout << "> " << #x << " : " << (x) << endl;
#define EPS 0.000000001
#define Pi 3.1415926535897932384626433832795028841971
#define hash1 1000003
#define hash2 1000033
#define md 1000000007
#define INF 1000000500ll
#define mp make_pair
#define pb push_back
#define S size()
#define MX(aa,bb) (aa>bb?aa:bb)
#define MN(aa,bb) (aa<bb?aa:bb)
#define fi first
#define se second
#define PI pair < int,int >
#define REP(i,a,n) for(i=a;i<n;i++)
#define sc scanf
#define pt printf
#define big long long
#define VI vector <int>
#define DID (long long)
#define ll long long
#define AL(a) (a).begin(),(a).end()
#define INFF DID INF*INF


using namespace std;

const int T=20 + 5;

double get(double C,double F,double X){
    double answer=DID INF*INF;
    double have=2.0;
    double timee=0;
    while (1){
        answer=min(answer,timee+X/have);
        timee+=C/have;
        have+=F;
        if (timee>answer)
            break;
    }
    return answer;
}

main(){
    #ifndef ONLINE_JUDGE
            freopen("text.in","r",stdin);  freopen("text.out","w",stdout);
    #endif

    int tt,t;
    cin>>t;
    tt=t;
    while (t--){
        double C,F,X;
        cin>>C>>F>>X;
        double answer=get(C,F,X);
        printf("Case #%d: %.8lf\n",tt-t,answer);
    }
}
