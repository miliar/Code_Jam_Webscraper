#include<algorithm>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<deque>
#include<iostream>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define ITER(i,a) for(typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define MOD 1000000007

typedef pair<double,double> ii;
typedef long long int ll;
typedef vector<int> vi;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int l=1;l<=T;l++){
        double C,F,X;
        cin>>C>>F>>X;
        double A[100010];
        double ans;
        A[0]=X/2.0;
        A[1]=C/2.0 + X/(2.0+F);
        for(int i=2;i<=100000;i++){
            A[i]=A[i-1]-X/(2+(i-1)*F)+C/(2+(i-1)*F)+X/(2+i*F);
        }
        sort(A,A+100000);
        for(int i=0;i<=100000;i++){
            if(A[i]>0) { printf("Case #%d: %.7lf\n",l,A[i]); break;}
        }
    }
return 0;
}
