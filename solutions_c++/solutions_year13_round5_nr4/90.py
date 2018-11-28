//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int n;
char str[447];
double memo[1<<21];

double prob(int state){
    if (memo[state] > -1.0) return memo[state];
    if (state==(1<<n)-1) return memo[state] = 0.0l;
    double res = 0.0l;
    For(i,n){
        int j = i;
        int l = n;
        while(state & (1<<j)) {
            j=(j+1)%n;
            l--;
        }
        int mynext = state | (1<<j);
//        printf("call %d %d %lf\n",j, mynext, prob(mynext));
        res += 1.0l/double(n) * (double(l)+prob(mynext));
    }
//    printf("st %d %d %lf\n",n, state, res);
    return memo[state] = res;
}

int extra(){
    scanf(" %s",str);
    n = strlen(str);
    int state = 0;
    For(i,n) state |= ((str[i]=='X')<<i);
    For(i,(1<<n+1)) memo[i] = -5.;
    printf("%.12lf\n",prob(state));
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
