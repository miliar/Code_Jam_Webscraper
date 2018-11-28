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
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;


int extra(){
    char buf[1047];
    int smax, p = 0, vys = 0;
    scanf("%d %s", &smax, buf);
    For(i, smax+1) {
        if (p < i) {
            int diff = i - p;
            p+=diff;
            vys+=diff;
        }
        p+=int(buf[i]-'0');        
    }
    printf("%d\n", vys);
}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
